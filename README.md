# lucky_day
Blockchain Buy/Sell App

This project utilizes Streamlit to prototype a deployable app using blockchain payments for purchases of cars and motorcycles.
The python code in this project leverages the program Ganache to create a user's/(buyer's) crypto wallet with public and private keys. The buy/sell transaction is identified as a vehicle or motorcycle and the option to include a more complex smart contract, or simply handle the payment transaction on the Ganache testing Blockchain. 

---

# Technologies
python 3.8

Web3 5.17

mnemonic 0.20

bip44 0.1.3

os-sys 2.1.4

python-dotenv 0.21.1

ethereum 2.3.2

https://trufflesuite.com/ganache/

---

# Required Libraries
import os

from dotenv import load_dotenv

import streamlit as st

from bip44 import Wallet

from eth_account import Account

from web3 import middleware

from web3.gas_strategies.time_based import medium_gas_price_strategy

from web3 import Web3

w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))

---

# Install Fintech Finder
1. Open your terminal and start a new dev env

`conda create -n dev python=3.8 anaconda`
    
2. Activate your dev envnironment

`conda activate dev`
    
3. Install required Technologies in development environment
```
pip install web3
pip install mnemonic
pip install bip44
pip install os-sys
pip install python-dotenv
pip install ethereum
```

4. In the directory of your choice, clone this repository

`git clone https://github.com/Arty-j/lucky_day.git`

5. Download Ganache to local system
    www.https://trufflesuite.com/ganache/
    
    - click on download to your local system
    
    - open Ganache using a Quick Start button
    
6. At top of the dasboard under the "Accounts" Tab, will be a mnemonic string

<img  src="./Images/mnemonic_ex.png"  width="600" />

    - copy the string to your clipboard
    
7. Create a new .env file in your lucky_day cloned directory 

    - open the IDE of your choice and create a new text file
    
    - type `MNEMONIC = "paste your mnemonic string saved on your clipboard from ganache here"`
    
    - save the text file as '.env' file
    
<img  src="./Images/directory.png"  width="200" />
    
    - **this mnemonic will be used in the `lucky_day.py` code to create a wallet with public and private key for you use on the local Ganache testing Blockchain**
    
8. Navigate to your Ganache Dashboard once again
    
    - your wallet and public address will be listed as the first address on the Ganache dashboard
    - you can choose another address in the list to be your "Seller_Address" 
        -- as described below in step 5.
    
<img  src="./Images/address.png"  width="600" />  
    

---

## Run lucky_day

1. Navigate to your terminal, then to the directory where you cloned the lucky_day repository

    - run `streamlit run lucky_day.py`
    
2. Navigate to streamlit page running locally in browser window

3. Enter they type of transaction you would like to conduct "Vehicle" or "Motorcycle", and whether or not you would like to have it "Smart Contract Enabled" or "Simple Transaction Record".

4. Hit the "Transaction Type" button, to register your preferences.

<img  src="./Images/main_page.png"  width="600" /> 

5. Open the "Customize your Transaction" expander and enter the specific information about the vehicle or motorcycle you are buying. 
    - you can go to your Ganache Dashboard and copy one of the addresses listed, (as mentioned above)
    - paste that address in the "Seller's Address" area of the app
    - this way you can test the app and see the transaction on your Ganache Dashboard
    
<img  src="./Images/data_form_top.png"  width="600" /> 
<img  src="./Images/data_form_bottom.png"  width="600" /> 
  
6. Hit the "Review Transaction Details" button on the bottom of the expander
    - the current USD to ETH to wei equivalents are listed
    - the details you entered about the transaction are listed as a transaction record for final review
    
<img  src="./Images/transaction_review.png"  width="600" /> 
    
7. Hit the "Complete Transaction" button on the bottom of the expander
    -see the transactions hash code printed below the button verifying the hash code added to the block as the transaction was processed
<img  src="./Images/complete_st_hash.png"  width="600" />  

5. You can verify this transaction by navigating to your Ganache dashboard and clicking on the "Transactions" tab

<!-- <img  src="./Images/transaction.png"  width="600" /> -->

6. The amount paid will also be subtracted from your wallet balance, listed next to your wallet address on the "Accounts" page
    - you can also see the transaction price added to the seller's Address that you listed in the app

<!-- <img  src="./Images/my_gan_acct.png"  width="600" />
 -->


---

# Contributors

Jodi Artman.  *github.com/Arty-j*

Kausar Hina.  *github.com/KausarHina*

Marissa Gonzalas.  *github.com/Marissagonzales468*

Edith Chou.   *github.com/wf880180*

---

# License

licensed in accordance with UC Berkeley policy