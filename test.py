import requests

BASE = "http://127.0.0.1:5000/"

reponse = requests.post(BASE+"getFromDatabase/124/112")
print(reponse.json())
