import requests 

r = requests.get("http://https//api.opensea.io/api/v1/assets?")

print(r.json())