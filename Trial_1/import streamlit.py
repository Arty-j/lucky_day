import streamlit
import requests 
import web3
import json
import pandas


params = {
    'collection': 'the-wanders',
    'limit': 1
}

r = requests.get("https://api.opensea.io/api/v1/assets", params = params)

print(json.dumps(r.json()))