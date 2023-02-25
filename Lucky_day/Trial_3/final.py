# Imports
import os
import json
import requests
from eth_account import account
from eth_typing import abi
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
## Configure streamlit page
st.set_page_config(
    page_title="Lucky Day's Auction House",
    page_icon="💸",
)
##from crypto_wallet import generate_account, get_balance, send_transaction

load_dotenv()

# Define and connect a new Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

################################################################################
# Contract Helper functions:
# 1. Loads the contract once using cache
# 2. Connects to the contract using the contract address and ABI
################################################################################


@st.cache(allow_output_mutation=True)
def load_contract():

    # Load the contract ABI
    with open(Path('./contracts/compiled/auction.json')) as f:
        auction_abi = json.load(f)

    # Set the contract address (this is the address of the deployed contract)
    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    # Get the contract
    contract = w3.eth.contract(
        address=contract_address,
        abi=auction_abi
    )

    return contract


# Load the contract
contract = load_contract()

################################################################################
# View the NFT (Hardpasted)
################################################################################
art_database = {
    "Image1": ["Image1", "0xc259A1dc029dfdC30977E8878270ddF5d82a89FF", "Firas", 2, "https://gateway.pinata.cloud/ipfs/QmaLAE6cUptyBq7xEgQMViWuFtS685nk1yW7ph8eWEHttW?_gl=1*qzrcxs*_ga*MTM2ODU1OTg5NC4xNjc2OTI4MjI1*_ga_5RMPXG14TE*MTY3NzI4NjU4NC44LjEuMTY3NzI4OTk5OS41OC4wLjA."],
    "Image2": ["Image2", "0x77ac9dDaD5e2D4E1Cd47E493f65FCdCc48917DCF", "Marissa", 2, "https://gateway.pinata.cloud/ipfs/Qmbk7zeUBQRHABiTUjv1Cn6QFcXv7EhQn97KEDwRDNNP2s?_gl=1*bbtxm8*_ga*MTM2ODU1OTg5NC4xNjc2OTI4MjI1*_ga_5RMPXG14TE*MTY3NzI4NjU4NC44LjEuMTY3NzI4ODE2OC42MC4wLjA."],
    "Image3": ["Image3", "0x0de909742De737fA48ad38b2146625434B6a6f35", "Jodi", 2, "https://gateway.pinata.cloud/ipfs/Qmd1JZTwCXgdkrBPrTaG237AxJpaRZhE4t2NZoV8nxPpjj?_gl=1*1bi9crx*_ga*MTM2ODU1OTg5NC4xNjc2OTI4MjI1*_ga_5RMPXG14TE*MTY3NzI4NjU4NC44LjEuMTY3NzI4ODE2OC42MC4wLjA."],
    "Image4": ["Image4", "0x502f7Ea88b7DFa9572138E062B4e7628A350e2E8", "Kausar", 2, "https://gateway.pinata.cloud/ipfs/Qmbb4co5T1yyJTtDazbp5fqwtiuKA1XQSsTD5W1y6PjSRq?_gl=1*1iufsc*_ga*MTM2ODU1OTg5NC4xNjc2OTI4MjI1*_ga_5RMPXG14TE*MTY3NzI4NjU4NC44LjEuMTY3NzI5MDEyMC41Ny4wLjA."],
    "Image5": ["Image5", "0x77084f1971306E919Bb0ba86B3235920eEF82293", "Edith", 2, "https://gateway.pinata.cloud/ipfs/QmdfSyexGGTzJ3cG9mFA98JSNtTvqgWNFzRnzS3L4CUNZm?_gl=1*1kw202g*_ga*MTM2ODU1OTg5NC4xNjc2OTI4MjI1*_ga_5RMPXG14TE*MTY3NzI4NjU4NC44LjEuMTY3NzI5MDEyMC41Ny4wLjA."],
    "Image6": ["Image6", "0xc259A1dc029dfdC30977E8878270ddF5d82a89FF", "Firas", 4, "https://gateway.pinata.cloud/ipfs/QmTtodGSvmEweAB5UV6kqK8BDiokgDwDtaU8b2tq2oxGb2?_gl=1*1gp63m5*_ga*MTM2ODU1OTg5NC4xNjc2OTI4MjI1*_ga_5RMPXG14TE*MTY3NzI4NjU4NC44LjEuMTY3NzI5MDEyMC41Ny4wLjA."],
    "Image7": ["Image7", "0x502f7Ea88b7DFa9572138E062B4e7628A350e2E8", "Kausar", 4, "https://gateway.pinata.cloud/ipfs/QmezL9E2W9ikfWQewWYHgFXAxZoh24x8PTcwsRWqL8K79S?_gl=1*pnl9mi*_ga*MTM2ODU1OTg5NC4xNjc2OTI4MjI1*_ga_5RMPXG14TE*MTY3NzI4NjU4NC44LjEuMTY3NzI5MDg1OC42MC4wLjA."],
    "Image8": ["Image8", "0x77084f1971306E919Bb0ba86B3235920eEF82293", "Edith", 4, "https://gateway.pinata.cloud/ipfs/QmWGarVaDHYzQhVETvW2nq4bKvQPb1TXtiomYNJY4WBzKR?_gl=1*fmddls*_ga*MTM2ODU1OTg5NC4xNjc2OTI4MjI1*_ga_5RMPXG14TE*MTY3NzI4NjU4NC44LjEuMTY3NzI5MDg1OC42MC4wLjA."],
    "Image9": ["Image9", "0x77ac9dDaD5e2D4E1Cd47E493f65FCdCc48917DCF", "Jodi", 4, "https://gateway.pinata.cloud/ipfs/QmQYK7TRnaBEQZje9UMd7zpnpbBeuxooRg7Zp1w4ayP871?_gl=1*1xciftp*_ga*MTM2ODU1OTg5NC4xNjc2OTI4MjI1*_ga_5RMPXG14TE*MTY3NzI4NjU4NC44LjEuMTY3NzI5MTM4OS42MC4wLjA."],
    "Image10": ["Image10", "0x0de909742De737fA48ad38b2146625434B6a6f35", "Marissa", 4, "https://gateway.pinata.cloud/ipfs/QmVhWWTjD7hXNgfTimYfCpY6xeLEv1trEXVghPdY9boJax?_gl=1*1oftpnb*_ga*MTM2ODU1OTg5NC4xNjc2OTI4MjI1*_ga_5RMPXG14TE*MTY3NzI4NjU4NC44LjEuMTY3NzI5MDEyMC41Ny4wLjA."],
}

art = ["Image1", "Image2", "Image3", "Image4", "Image5", "Image6", "Image7", "Image8", "Image9", "Image10"]

def get_art():
    """Display the database of art information."""
    db_list = list(art_database.values())

    for number in range(len(art)):
        st.image(db_list[number][4], width=200)
        st.write("Name: ", db_list[number][0])
        st.write("Ethereum Account Address: ", db_list[number][1])
        st.write("Artist: ", db_list[number][2])
        st.write("Minimum Bid: ", db_list[number][3], "ETH")
        st.text(" \n")


################################################################################
# Streamlit code
################################################################################

# Streamlit application headings
st.markdown("# Lucky Day NFT Auction House!")
st.markdown("## Bid For Your Favourite NFT!")
st.text(" \n")

# Streamlit Sidebar Code - Start
get_art()

st.sidebar.markdown("## Client Account Address and Ethernet Balance in Ether")

accounts = w3.eth.accounts
address = st.sidebar.selectbox("Select Account", options=accounts)

# Write the client's Ethereum account address to the sidebar
st.sidebar.write()

# Create a select box to chose a car to bid on
art = st.sidebar.selectbox('Select NFT', art)

# Create a input field to record the initial bid
starting_bid = st.sidebar.number_input("Bid")

# Identify the Art for auction
art = art_database[art][0]

# Write the art's name to the sidebar
st.sidebar.markdown("## NFT Name")
st.sidebar.write(art)

# Identify the the starting bid for the art being auctioned
st.sidebar.markdown("## Minimum Bid")
starting_bid = art_database[art][3]

# Write the arts starting bid
st.sidebar.write(starting_bid)

# Identify the auction owner's Ethereum Address
st.sidebar.markdown("## Account Address")
art_address = art_database[art][1]

# Write the auction owner's Ethereum Address to the sidebar
st.sidebar.write(art_address)

if st.sidebar.button("Place Bid"):
    tx_hash = contract.functions.bid().transact({'from': account, 'gas': 3000000})
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write("Transaction receipt mined:")
    st.write(dict(receipt))
 
if st.sidebar.button("Withdraw"):
    tx_hash = contract.functions.withdraw()
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write("Transaction receipt mined:")
    st.write(dict(receipt))

if st.sidebar.button("End Auction"):
    tx_hash = contract.functions.auctionend()
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write("Transaction receipt mined:")
    st.write(dict(receipt))

st.sidebar.markdown("## Highest Bid in Ether")

## Additional code apart from BID, to showcase proof of transaction
purchase_price = starting_bid

# Write the `total purchase` calculation to the Streamlit sidebar
st.sidebar.write(purchase_price)


if st.sidebar.button("Send Transaction"):

    # Call the `send_transaction` function and pass it 3 parameters:
    # Your `account`, the `art_address`, and the `purchase_price` as parameters
    # Save the returned transaction hash as a variable named `transaction_hash`
    transaction_hash = send_transaction(w3, accounts, art_address, purchase_price)

    # Markdown for the transaction hash
    st.sidebar.markdown("#### Validated Transaction Hash")

    # Write the returned transaction hash to the screen
    st.sidebar.write(transaction_hash)

    # Celebrate your successful payment
    st.balloons()