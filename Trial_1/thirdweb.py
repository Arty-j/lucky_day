import streamlit as st
import pandas as pd
import json
import requests
from io import StringIO
from thirdweb import ThirdwebSDK
from eth_account import Account
from dotenv import load_dotenv
from web3 import Web3
import os


st.set_page_config(
    page_title="Lucky_Day",
    page_icon="☘️",
)
st.write("# Create your own NFT Here!")

### CREATE/ UPLOAD NFT IMAGE
if st.button('Select Image'):
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # To read file as bytes:
        bytes_data = uploaded_file.getvalue()
        st.write(bytes_data)

        # To convert to a string based IO:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        st.write(stringio)

        # To read file as string:
        string_data = stringio.read()
        st.write(string_data)

        # Can be used wherever a "file-like" object is accepted:
        dataframe = pd.read_csv(uploaded_file)
        st.write(dataframe)


# MULTIPLE FRAMES

#uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
#for uploaded_file in uploaded_files:
    #bytes_data = uploaded_file.read()
    #st.write("filename:", uploaded_file.name)
    #st.write(bytes_data)

    ### IF VIDEO FILE
# video_file = open('myvideo.mp4', 'rb')
#video_bytes = video_file.read()
#st.video(video_bytes)

    ### CREATING WALLET
# Load environment variables into this file
load_dotenv()

# This PRIVATE KEY is coming from your environment variables. Make sure to never put it in a tracked file or share it with anyone.
PRIVATE_KEY = os.environ.get("PRIVATE_KEY")

# Add your own RPC URL here or use a public one
RPC_URL = "HTTP://127.0.0.1:7545"

# Instantiate a new provider to pass into the SDK
provider = Web3(Web3.HTTPProvider(RPC_URL))

# Optionally, instantiate a new signer to pass into the SDK
signer = Account.from_key(PRIVATE_KEY)

# Finally, you can create a new instance of the SDK to use
sdk = ThirdwebSDK(provider, signer)

nft_collection = sdk.get_nft_collection("0x214997754cd8c83bD65f78f86a33AA27a19B59F8")

    ###OWNER & RECIPIENT ADRESSESS
col1, col2,col3, col4 = st.columns(4)

with col1:
    st.radio(
        "Which Car is Going to Make Your Lucky Day? 👉",
        key="Car",
        options=["SUV", "Hatchback","Crossover","Convertible","Sedan","Sports Car","Coupe","Minivan", "Pick-Up Truck","Motorcycle,"],
    )

    st.text_input(
        "The Owner's Current Wallet Address",
        key="adress",
        text_input = st.text_input()
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        placeholder=st.session_state.placeholder,
        )
    if st.text_input:
        st.write("You entered: ", text_input)
    

with col2:
    text_input = st.text_input(
        "Please Enter the Recipents Address 👇",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        placeholder=st.session_state.placeholder,
    )

    if text_input:
        st.write("You entered: ", text_input)




    ###SYMBOL/ SIGNATURE
with col3:
    text_input = st.text_input(
        "Symbol",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        placeholder=st.session_state.placeholder,
    )

    if text_input:
        st.write("You entered: ", text_input)
with col3:
    text_input = st.text_input(
        "Description",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        placeholder=st.session_state.placeholder,
    )

    if text_input:
        st.write("You entered: ", text_input)


### MINTING
#// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@thirdweb-dev/contracts/base/ERC721Base.sol";
import "@thirdweb-dev/contracts/extension/Permissions.sol";

contract MyNFT is ERC721Base, Permissions {
    bytes32 private constant MINTER_ROLE = keccak256("MINTER_ROLE");

    constructor(
        string memory _name,
        string memory _symbol,
        address _royaltyRecipient,
        uint128 _royaltyBps
    ) ERC721Base(_name, _symbol, _royaltyRecipient, _royaltyBps) {}

    #/**
    # *  `_canMint` is a function available in `ERC721Base`.
    #*
    # *  It is called every time a wallet tries to mint NFTs on this
    # *  contract, and lets you define the condition in which an
    # *  attempt to mint NFTs should be permitted, or rejected.
    # *
    # *  By default, `ERC721Base` only lets the contract's owner mint
    # *  NFTs. Here, we override that functionality.
    # *
    # *  We use the `Permissions` extension to specify that anyone holding
    # *  "MINTER_ROLE" should be able to mint NFTs.
    # */
    #function _canMint() internal view override returns (bool) {
    #    return hasRole(MINTER_ROLE, msg.sender);
    #}
#}