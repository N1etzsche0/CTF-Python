import os
import config
from flask import Flask, request, session, render_template, url_for,redirect,make_response
import pickle
import io
import sys
import base64


app = Flask(__name__)


class RestrictedUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        if module in ['config'] and "__" not in name:
            return getattr(sys.modules[module], name)
        raise pickle.UnpicklingError("global '%s.%s' is forbidden" % (module, name))


def restricted_loads(s):
    return RestrictedUnpickler(io.BytesIO(s)).load()

@app.route('/')
def show():
    base_dir = os.path.dirname(__file__)
    resp = make_response(open(os.path.join(base_dir, __file__)).read()+open(os.path.join(base_dir, "config/__init__.py")).read())
    resp.headers["Content-type"] = "text/plain;charset=UTF-8"
    return resp

@app.route('/home', methods=['POST', 'GET'])
def home():
    data=request.form['data']
    User = restricted_loads(base64.b64decode(data))
    return str(User)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
import os
def backdoor(cmd):
    # 这里我也改了一下
    if isinstance(cmd,list) :
        s=''.join(cmd)
        print("!!!!!!!!!!")
        s=eval(s)
        return s
    else:
        print("??????")

