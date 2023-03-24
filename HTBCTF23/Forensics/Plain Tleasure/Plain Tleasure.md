Given a pcap file

Talks about stolen admin creds, that we need to find.

# Solution
As it is a pcap file best bet is to open it in wireshark. Looking at all the HTTP objects under:
```
File -> export -> HTTP
```
and filtering for a form as to update the creds it would have had to of been a post request.

There is a token file. Catting out the file will show the flag.
`HTB{th3s3_4l13ns_st1ll_us3_HTTP}`
