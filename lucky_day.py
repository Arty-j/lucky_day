# Lucky Day Blockchain Application
################################################################################

################################################################################
# Imports
import os
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
# from streamlit_image_select import image_select
from wallet import get_balance, generate_account
from bip44 import Wallet
from eth_account import Account
from web3 import middleware
from web3.gas_strategies.time_based import medium_gas_price_strategy
from web3 import Web3
w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))
from utils import getnums, get_price, send_transaction
from wallet import generate_account, get_balance






################################################################################
# Step 1:
# Sets up dictionaries and datasets


################################################################################
# Step 2:
# Streamlit Code


st.set_page_config(page_title="luckyday", page_icon=None, initial_sidebar_state="collapsed")

st.markdown("# Lucky Day")
st.markdown("## Blockchain Smart Contract App")
st.markdown("**Conduct your transactions via a transparent, trustworthy decentralized network**")

################################################################################
# Step 3:
# Streamlit Main Page Form for data capture

#sets up data collection form with 3 columns
st.write("")
form = st.form(key="form_settings", clear_on_submit=False)
col1, col2, col3 = form.columns([2, 2, 1])

#1st column dropdown options
contract_options=["Vehicle", "Motorcycle"]
type = col1.selectbox(
    "Contract Type",
    options=contract_options,
    key="type",
)
#2nd column dropdown options
level_options=["Smart Contract Enabled", "Simple Transaction Record"]
level = col2.radio(
    "Transaction Level",
    options=level_options,
    key="level",
)

#3rd column slider option
excitement = col3.slider(
    "Excitement Level",
    0,
    100,
    key="excitement",
)

################################################################################
# Step 3:
# Form expander for Vehicle selection options

expander = form.expander("Customize Your Transaction")
if type == "Vehicle":
    col1style, col2style, col3style = expander.columns([2, 2, 1])
    #col 1 data input -Vehicle
    veh_make = col1style.text_input(
        "Vehicle Make",
        max_chars=20,
        key="veh_make",
    )

    veh_model = col1style.text_input(
        "Vehicle Model",
        max_chars=20,
        key="veh_model",
    )

    veh_year = col1style.selectbox(
        "Vehicle Year",
        options=getnums(1980,2023,1)
    )

    veh_vin = col1style.text_input(
        "Vehicle VIN",
        max_chars=17,
        key="veh_vin",
    )
    
    veh_color_options = ["black", "white", "silver", "grey", "beige", "blue", "red", "green", "gold", "other"]
    veh_color = col1style.radio(
        "Vehicle Color",
        options=veh_color_options,
        key="veh_color",
    )


    #col 2 data input- Seller/Buyer
    seller_name = col2style.text_input(
        "Seller Name",
        max_chars=40,
        key="seller_name",
    )

    seller_address = col2style.text_input(
        "Seller Wallet Address",
        max_chars=42,
        key="seller_address",
    )
    
    col2style.markdown("---")

    buyer_name = col2style.text_input(
        "Buyer Name",
        max_chars=40,
        key="buyer_name",
    )

    buyer_address = col2style.text_input(
        "Buyer Wallet Address",
        max_chars=42,
        key="buyer_address",
    )

    col2style.markdown("---")

    pmtCOIN_options =["USD", "ETH"]
    veh_pmtCOIN = col2style.radio(
        "Sale Transaction Coin",
        options=pmtCOIN_options,
        help="This is the coin of choice for the sale transaction",
        key="veh_pmtCOIN",
    )
    
    veh_price = col2style.text_input(
        label=":red[Sale Transaction Price]",
        help="This is agreed sale price in the coin of choice listed above",
        key="veh_price",
    )

    if veh_price != '' : 
        veh_priceUSD, veh_priceETH, veh_priceWEI = get_price(w3, veh_pmtCOIN, veh_price)
    else:
        veh_priceUSD = '' 
        veh_priceETH = '' 
        veh_priceWEI = ''   
    
    


    #col 3 data input- price
    veh_title_options = ["clean/clear", "lienholder", "electronic", "salvage", "flood/water damage", "rebuilt", "parts"]
    veh_title = col3style.radio(
        "Vehicle Title",
        options=veh_title_options,
        key="veh_title",
    )

    gas = col3style.text_input(
        "Gas",
        help="Price offering for gas",
        key="gas",
    )
    
    st.markdown("---")

# Final Form submittal of data to create smart contract or simply place transaction on blockchain
form.form_submit_button(label="Review Transaction Details")


# if type == "Vehicle" and level == "Smart Contract Enabled":
#     # with st.spinner("Creating your smart contract for final review...(may take a minute)"):
#     #     ########## * here is where we need to connect the smart contract for a vehicle *#######
#     #     smart_contract = compile_veh_contract(submitted)
#     None
# else:
#     st.write("The sale transaction of this vehicle, will be:")
#     st.write(f'{buyer_name} at {buyer_address} paying')
#     st.write(f'{seller_name} at {seller_address}')
#     st.write(f'{veh_price}, in {veh_pmtCOIN} for a {veh_make}, {veh_model}')
                 
#     st.write('The blockchain sale transaction will be in wei')
#     st.write('according to your choice of sale coin and price, which means')
#     st.write(f'${veh_priceUSD} USD = {veh_priceETH} ETH = {veh_priceWEI} wei')
#     st.write('If this sale record looks correct, use button below to complete')
#     st.write('the sales transaction and record to the Blockchain')
                


################################################################################
# Step 4: Generate Account (Wallet) on Ganache with default 100ETH
# check wallet balance and write to sidebar if user has enough ether to buy the vehicle/moto.
                 
account = generate_account(w3)
                 
walletETH = get_balance(w3, account.address)
                 
if veh_priceETH != '' and veh_priceETH <= walletETH:
    new_balance = float(walletETH) - float(veh_priceETH)
    
# Write the vehicle make and model to the sidebar
    st.sidebar.write(f"If you buy this {veh_make} {veh_model} for, {veh_priceETH} ETH, your new account balance will be: {new_balance}.")
    
else:
    st.sidebar.write(f"With a balance of {walletETH} ether in your wallet, you can't buy this {veh_make} {veh_model} for, {veh_priceETH} ETH.")

################################################################################
# Step 4:
# Streamlit “Add Block” button code so that when someone clicks the
# button, the transaction is added to the blockchain.

if st.button("Complete Transaction and Add Block to Blockchain"):
    transaction_complete = send_transaction(w3, account, buyer_address, veh_priceETH)
    st.write("Your transaction on the Ganache Blockchain tester is complete!")
    st.write("Here is the hash code confirming your transaction")
    st.write(f"{transaction_complete}")
    st.write("/n")
    st.markdown("# Congratulations on selling your car!")
    st.balloons
                 
################################################################################

st.markdown("---")
st.markdown("# If you liked this app give us a :thumbs up: it keeps us creating more great tools for the future of Blockchain!")
             
st.write(
    "Share with your friends and make buying and selling your lucky day!"
)
st.markdown(
    "More infos and :star: at [github.com/arty-j/lucky_day](https://github.com/arty-j/lucky_day)"
)

# st.session_state["previous_style"] = style
################################################################################
