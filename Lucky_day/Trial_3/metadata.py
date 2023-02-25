import os
import json
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

file_headers = {
    "pinata_api_key": os.getenv("PINATA_API_KEY"),
    "pinata_secret_api_key": os.getenv("PINATA_SECRET_API_KEY"),
}

r = requests.post(
        "https://api.pinata.cloud/pinning/pinFileToIPFS",
        files={'file': data},
        headers=file_headers
    )
print(r.json())

def pin_file_to_ipfs(data):
    r = requests.post(
        "https://api.pinata.cloud/pinning/pinFileToIPFS",
        files={'file': data},
        headers=file_headers
    )
    print(r.json())
    ipfs_hash = r.json()["IpfsHash"]
    return ipfs_hash
file = st.file_uploader("Upload Artwork", type=["jpg", "jpeg", "png"])
file_ipfs_hash = pin_file_to_ipfs(file.getvalue())
print(f"The IPFS file hash is {file_ipfs_hash}")
print(f"The IPFS file URI is ipfs://{file_ipfs_hash}")

headers = {
    "Content-Type": "application/json",
    "pinata_api_key": os.getenv("PINATA_API_KEY"),
    "pinata_secret_api_key": os.getenv("PINATA_SECRET_API_KEY"),
}

def pin_json_to_ipfs(json):
    r = requests.post(
        "https://api.pinata.cloud/pinning/pinJSONToIPFS",
        data=json,
        headers=headers
    )
    print(r.json())
    ipfs_hash = r.json()["IpfsHash"]
    return ipfs_hash

data = {"pinataOptions": {"cidVersion": 1}, "pinataContent": content}

def convert_data_to_json(content):
    data = {"pinataOptions": {"cidVersion": 1}, "pinataContent": content}
    return json.dumps(data)
def pin_artwork(artwork_name, artwork_file):
    # Pin the file to IPFS with Pinata
    ipfs_file_hash = pin_file_to_ipfs(artwork_file.getvalue())

    # Build a metadata file for the artwork
    token_json = {
        "name": artwork_name,
        "image": ipfs_file_hash
    }

    # Convert the metadata to the JSON data string that Pinata requires
    json_data = convert_data_to_json(token_json)

    # Pin the json to IPFS with Pinata
    json_ipfs_hash = pin_json_to_ipfs(json_data)

    return json_ipfs_hash

def pin_appraisal_report(report_content):
    json_report = convert_data_to_json(report_content)
    report_ipfs_hash = pin_json_to_ipfs(json_report)
    return report_ipfs_hash