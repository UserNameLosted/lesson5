import requests


r = requests.get("http://sql-ex.ru/")  #get
print(r.headers)
print(r.status_code)
print(r.text)

r = requests.head("http://sql-ex.ru/")  #head
print(r.headers)
print(r.status_code)
print(r.text)

