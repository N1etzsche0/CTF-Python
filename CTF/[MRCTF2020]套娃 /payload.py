import base64

list1 = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)] + [str(i) for i in range(0, 9)]


def payload():
    flag = ''
    for _ in range(0, 30):
        for x in list1:
            flag += x
            re = ''
            for i in range(len(flag)):
                re += chr(ord(flag[i]) + i * 2)
                if re == "flag.php":
                    print(base64.b64encode(re))


if __name__ == '__main__':
    payload()
