import requests

token = 'http://127.0.0.1:8000/ipadipad'



users = requests.get(token).json()

for i in users:
    print(i['title'])