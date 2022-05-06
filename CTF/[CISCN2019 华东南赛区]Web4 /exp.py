import random

mac = "86:c9:db:26:7b:dd"
nmac = mac.replace(":", "")
random.seed(int(nmac, 16))
print(str(random.random() * 233))
