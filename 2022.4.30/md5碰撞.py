import hashlib

for i in range(1,100000000000):
    s = hashlib.md5(str(i).encode("utf-8")).hexdigest()[0:6]
    if s == "6d0bc1":
        print(i)
        break