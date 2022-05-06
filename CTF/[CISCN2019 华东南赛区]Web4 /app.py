import random
import re
import urllib
import uuid

from flasksession import Flask, session, request

app = Flask(__name__)
random.seed(uuid.getnode())
app.config['SECRET_KEY'] = str(random.random() * 233)
app.debug = True


@app.route('/')
def index():
    session['username'] = 'www-data'
    return 'Hello World! Read somethings'


@app.route('/read')
def read():
    try:
        url = request.args.get('url')
        m = re.findall('^file.*', url, re.IGNORECASE)
        n = re.findall('flag', url, re.IGNORECASE)
        if m or n:
            return 'No Hack'
        res = urllib.urlopen(url)
        return res.read()
    except Exception as ex:
        print
        str(ex)
    return 'no response'


@app.route('/flag')
def flag():
    if session and session['username'] == 'fuck':
        return open('/flag.txt').read()
    else:
        return 'Access denied'


if __name__ == '__main__':
    app.run(
        debug=True,
        host="0.0.0.0"
    )
# username=fuck read /flag.txt
# session