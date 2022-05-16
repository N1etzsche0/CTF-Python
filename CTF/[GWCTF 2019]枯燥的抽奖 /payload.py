str1 = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
str2 = 'KE2YS7F3eN'
str3 = str1[::-1]
length = len(str2)
res = ''
for i in range(len(str2)):
    for j in range(len(str1)):
        if str2[i] == str1[j]:
            res += str(j) + ' ' + str(j) + ' ' + '0' + ' ' + str(len(str1) - 1) + ' '
            break

print(res)