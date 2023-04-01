Given a sh script.

# Solution
reading the sh script
```
cat persistence.sh
```

There is a base64 payload being decoded and then saved as a service.

decoding the payload gives the flag.
```
HTB{th3s3_4l13nS_4r3_s00000_b4s1c}
```

One line trick:
```
cat persistence.sh | grep 'echo -e' | awk -F '"' '{print $2}'|base64 -d| grep HTB | awk -F= '{print $2}'
```
