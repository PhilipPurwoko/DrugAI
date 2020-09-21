import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'age':1, 'sex':1, 'bp':0, 'chol':0, 'natok':12})

print(r.json())
