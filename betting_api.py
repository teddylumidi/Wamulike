import json
import requests

with open('betting_data.json', 'r') as f:
    data = json.load(f)

url = 'http://localhost:8080/wins'
response = requests.post(url, json=data)

if response.ok:
    print('Data added successfully!')
else:
    print('Failed to add data.')
