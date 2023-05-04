import requests
token = 'http://127.0.0.1:8000/ipadipad/'

users = requests.get(token).json()

print(users[2]['ID'])