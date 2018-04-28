import requests

r = requests.get("http://pulse-rest-testing.herokuapp.com/books/")

books = r.json()

for b in books:
    print(b["title"])

name = {"title" : "Playboy", "author" : "Hugh Hefner"}
p = requests.post("http://pulse-rest-testing.herokuapp.com/books/", data=name)
print(p.status_code)
print(p.json())