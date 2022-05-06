import requests

host = "http://470a0b56-2410-4f5c-b4ac-87d23644662b.node4.buuoj.cn:81/"
while True:
    r = requests.get(host + "evi1?name=vnctf2022")
    r.encoding = "utf-8"
    if r.text.find("The Key is") != -1:
        print(r.text)
