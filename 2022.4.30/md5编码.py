import hashlib

s1 = (hashlib.md5("/fllllllllllllag".encode()).hexdigest())
print(hashlib.md5(("a2416a13-961b-4958-aa09-e442e81a82b6"+s1).encode()).hexdigest())
