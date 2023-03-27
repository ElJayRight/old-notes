import requests

r = requests.get("http://openwebanalytics.vessel.htb/index.php")
print(r.text)