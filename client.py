import requests
import json

headers = {"content-length": "18", "content-type": "application/json"}

name = "prasun"
jso = {"title": name, "Name": "Ratan"}
print(jso["title"])

r = requests.post('http://localhost:8000/dbreq', params={'tablename': "Table1"}, headers=headers, json=jso)
data = json.loads(r.text)  # It will convert json format to python dictionary
data1 = json.dumps(r.text)  # it converts (json or dictionary) to string.
print(data1)  # it's a string
print(data["id"])  # It's a dictionary

t = requests.get('http://localhost:8000/table1', params={'ids': data["id"]})
print(t.text)
