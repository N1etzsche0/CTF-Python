import requests

for x in range(1,200):
    url = "http://191d0848-358b-485e-8eb0-2796e24dfd3d.node4.buuoj.cn:81/shop?page={}".format(x)
    r = requests.get(url)
    if "lv6.png" in r.text:
        print(x)
        print(r.text)
