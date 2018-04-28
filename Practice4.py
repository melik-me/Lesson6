# Запрограммировать запросы к web-серверу (как клиент).

# import http.client
#
# conn = http.client.HTTPSConnection("bash.im")
# conn.request("GET", "/")
# r1 = conn.getresponse()
#
# print(r1.read())

import requests

r = requests.get("https://raw.githubusercontent.com/melik-me/HomeWork5/master/Task1.py")


#print(r.text)
print(r.url)