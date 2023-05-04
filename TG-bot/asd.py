import requests

token = 'http://127.0.0.1:8000/ipadipad'

users = requests.get(token).status_code

print(users)