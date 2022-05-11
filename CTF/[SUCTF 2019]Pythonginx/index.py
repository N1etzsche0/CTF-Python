import urllib
from urllib import parse
from urllib.parse import urlsplit, urlunsplit

from flask import request


@app.route('/getUrl', methods=['GET', 'POST'])
def getUrl():
    url = 
    host = parse.urlparse(url).hostname
    if host == 'suctf.cc': return "我扌 your problem? 111"
    parts = list(urlsplit(url))
    host = parts[1]
    if host == 'suctf.cc': return "我扌 your problem? 222 " + host
    newhost = []
    for h in host.split('.'): newhost.append(h.encode('idna').decode('utf-8'))
    parts[1] = '.'.join(newhost)  # 去掉 url 中的空格
    finalUrl = urlunsplit(parts).split(' ')[0]
    host = parse.urlparse(finalUrl).hostname
    if host == 'suctf.cc':
        return urllib.request.urlopen(finalUrl).read()
    else:
        return "我扌 your problem? 333"
