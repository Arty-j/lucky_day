# Lucky Day Blockchain Application
################################################################################

################################################################################
# Imports
import os
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
# from streamlit_image_select import image_select
from utils import getnums, get_price, send_transaction
from wallet import generate_account, get_balance
from bip44 import Wallet
from eth_account import Account
from web3 import middleware
from web3.gas_strategies.time_based import medium_gas_price_strategy
from web3 import Web3

w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))


################################################################################
# Step 1:
# Streamlit Code for Header


st.set_page_config(page_title="luckyday", page_icon=None)

st.markdown("# Lucky Day")
st.markdown("## Blockchain Smart Contract App")
st.markdown("**Conduct your transactions via a transparent, trustworthy decentralized network**")

################################################################################
# Step 2:
# Get Buyer Wallet data and balance for sidebar

account = generate_account()
walletETH = get_balance(w3, account.address)
buyer_address = account.address

st.sidebar.markdown("**It's Your Lucky Day to Buy**")
st.sidebar.write("Your (buyer) Account")
st.sidebar.write(f"Account Address : {buyer_address}")
st.sidebar.write(f"Balance: {walletETH}")


################################################################################
# Step 3:
# Streamlit Main Page  - Form for data capture to set up additional form expanders

#sets up data collection form with 3 columns
st.write("")
form = st.form(key="form_settings", clear_on_submit=False)
col1, col2, col3 = form.columns([2, 2, 1])

#1st column dropdown options
contract_options=["Vehicle", "Motorcycle"]
type = col1.selectbox(
    "Purchase Type",
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

submit = form.form_submit_button(label="Transaction Type")

################################################################################
# Step 4:
# Sets up data customization Form 2, with expander for Vehicle or Motorcycle selection options


    
# Sets up form 2
if submit == True and type == "Vehicle":
    form2 = st.form(key="form2_settings", clear_on_submit=False)
    
    # Expander opens and collapses the form with 3 columns
    expander = form2.expander("Customize Your Transaction")
    col1style, col2style, col3style = expander.columns([2, 2, 1])
        
# ---------
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
    
    col1style.markdown("---")
    
    seller_name = col1style.text_input(
        "Seller Name",
        max_chars=40,
        key="seller_name",
    )

    seller_address = col1style.text_input(
        "Seller Wallet Address",
        max_chars=42,
        key="seller_address",
    )
    

# ---------
#col 2 data input- Vehicle
    veh_color_options = ["black", "white", "silver", "grey", "beige", "blue", "red", "green", "gold", "other"]
    veh_color = col2style.radio(
        "Vehicle Color",
        options=veh_color_options,
        key="veh_color",
    )
    
    col2style.write(" ")
    
    col2style.write(" ")
    
    col2style.markdown("---")

    buyer_name = col2style.text_input(
        "Buyer Name",
        max_chars=40,
        key="buyer_name",
    )

    # col2style.write(buyer_address)
    
    # buyer_address = col2style.text_input(
    #     "Buyer Wallet Address",
    #     max_chars=42,
    #     key="buyer_address",
    # )
    
    
# ---------    
#col 3 data input- Vehicle
    veh_title_options = ["clean/clear", "lienholder", "electronic", "salvage", "flood/water damage", "rebuilt", "parts"]
    veh_title = col3style.radio(
        "Vehicle Title",
        options=veh_title_options,
        key="veh_title",
    )
    
    col3style.write(" ")
    col3style.write(" ")
    col3style.write(" ") 
    col3style.write(" ") 
    col3style.write(" ")  
    col3style.markdown("---")
    
    pmtCOIN_options =["USD", "ETH"]
    pmtCOIN = col2style.radio(
        "Sale Transaction Coin",
        options=pmtCOIN_options,
        help="This is the coin of choice for the sale transaction",
        key="veh_pmtCOIN",
    )
    
    price = col2style.text_input(
        label="Sale Transaction Price",
        help="This is agreed sale price in the coin of choice listed above",
        key="veh_price",
    )

    if price != '' : 
        priceUSD, priceETH, priceWEI = price(w3, pmtCOIN, price)
    else:
        priceUSD = '' 
        priceETH = '' 
        priceWEI = ''   
    
     
    gas = col3style.text_input(
        "Gas",
        help="Price offering for gas",
        key="veh_gas",
    )
    
# Final Form2 submittal of data to of Transaction Details
    submit2 = form2.form_submit_button(label="Review Transaction Details")

# ----------------------------
# ----------------------------

if submit == True and type == "Motorcycle":
    
    # Sets up form 3
    form3 = st.form(key="form3_settings", clear_on_submit=False)

    # Expander opens and collapses the form with 3 columns
    expander = form3.expander("Customize Your Transaction")
    col1style, col2style, col3style = expander.columns([2, 2, 1])

# ---------
    #col 1 data input -Motorcycle
    moto_make = col1style.text_input(
        "Motorcycle Make",
        max_chars=20,
        key="moto_make",
    )

    moto_model = col1style.text_input(
        "Motorcycle Model",
        max_chars=20,
        key="moto_model",
    )

    moto_year = col1style.selectbox(
        "Motorcycle Year",
        options=getnums(1980,2023,1)
    )

    moto_vin = col1style.text_input(
        "Motorcycle VIN",
        max_chars=17,
        key="moto_vin",
    )
    
    col1style.write(" ") 
    
    col1style.markdown("---")
    
    seller_name = col1style.text_input(
        "Seller Name",
        max_chars=40,
        key="moto_seller_name",
    )

    seller_address = col1style.text_input(
        "Seller Wallet Address",
        max_chars=42,
        key="moto_seller_address",
    )
    
    
# ---------
    #col 2 data input- Motorcycle
    motor_size = col2style.text_input(
        "Engine Size",
        max_chars=40,
        key="motor_size",
    )
    
 
    moto_color_options = ["black", "white", "silver", "yellow", "orange", "blue", "red", "green", "gold", "other"]
    moto_color = col2style.radio(
        "Motorcycle Color",
        options=moto_color_options,
        key="moto_color",
    )
    
    col2style.markdown("---")

    buyer_name = col2style.text_input(
        "Buyer Name",
        max_chars=40,
        key="moto_buyer_name",
    )

    # col2style.write(buyer_address)
    # buyer_address = col2style.text_input(
    #     "Buyer Wallet Address",
    #     max_chars=42,
    #     key="buyer_address",
    # )

    pmtCOIN_options =["USD", "ETH"]
    pmtCOIN = col2style.radio(
        "Sale Transaction Coin",
        options=pmtCOIN_options,
        help="This is the coin of choice for the sale transaction",
        key="moto_pmtCOIN",
    )
    
    price = col2style.text_input(
        label="Sale Transaction Price",
        help="This is agreed sale price in the coin of choice listed above",
        key="moto_price",
    )

    if price != '' : 
        priceUSD, priceETH, priceWEI = get_price(w3, pmtCOIN, price)
    else:
        priceUSD = '' 
        priceETH = '' 
        priceWEI = ''   
    
    
# --------- 
    #col 3 data input- Motorcycle
    moto_title_options = ["clean/clear", "lienholder", "electronic", "salvage", "flood/water damage", "rebuilt", "parts"]
    moto_title = col3style.radio(
        "Motorcycle Title",
        options=moto_title_options,
        key="moto_title",
    )
    
    col3style.write(" ") 
    col3style.write(" ") 
    col3style.write(" ")
    col3style.write(" ")
    col3style.write(" ") 
    col3style.write(" ") 
    col3style.write(" ")  
    col3style.markdown("---")
    
    gas = col3style.text_input(
        "Gas price in wei",
        help="Price offering for gas in wei",
        key="moto_gas",
    )
    

    # Final Form3 submittal of data to of Transaction Details
    submit3 = form3.form_submit_button(label="Review Transaction Details")

################################################################################
# Step 4: Connect Smart Contract or Record simple transaction to Ganache Blockchain
             
# if (submit2 or submit3) == True and level == "Smart Contract Enabled":
#     with st.spinner("Creating your smart contract for final review...(may take a minute)"):
        
#         smart_contract = compile_veh_contract(submit2, buyer_address)


                 

# Remove the if statement and replace with "else" once smart contract connected               
# else:                
if submit2 or submit3 == True:             
    if priceETH != '' and float(priceETH) <= float(walletETH):
        new_balance = float(walletETH) - float(priceETH)
        st.write("**The blockchain sale transaction will be in wei**")
        st.write("current market price of Ethereum")
        st.write(f"${priceUSD} USD = {priceETH} ETH = {priceWEI} wei")
        
        st.sidebar.write(" ")
        st.sidebar.write(" ")
        if type == "Vehicle":
            st.sidebar.write(f":blue[If you buy this {veh_make} {veh_model} for, {priceETH} ETH]")
            st.sidebar.write(f":blue[your new balance: {new_balance}]")
        else:
            st.sidebar.write(f":blue[If you buy this {moto_make} {moto_model} for, {priceETH} ETH]")
            st.sidebar.write(f":blue[your new balance: {new_balance}]")
        
        st.write(" ")
        st.markdown("### If this sale record looks correct, press the button below")
        st.markdown("### to complete the transaction and record it to the Blockchain")    
        st.write(" ")
        st.markdown(f":red[*{buyer_name} @ {buyer_address}*]")
        st.markdown(f":red[*paying {price}{pmtCOIN}*]")
        st.markdown(f":red[*to*]")
        st.markdown(f":red[*{seller_name} @ {seller_address}*]")
        if type =="Vehicle":
            st.write(f":red[*for the {veh_year} {veh_make}, {veh_model}*]")
        else:
            st.write(f":red[*for the {moto_year}, {moto_make}, {moto_model}*]")
        
                       
    else:
        if type == "Vehicle":
            st.write(f"With a balance of {walletETH} ether in your wallet, you can't afford this {veh_make} {veh_model} for, {priceETH} ETH.")
        else:
            st.write(f"With a balance of {walletETH} ether in your wallet, you can't afford this {moto_make} {make_model} for, {priceETH} ETH.")
            


###############################################################################
# Step 5:
# Streamlit “Complete Transaction” button code so that when someone clicks the
# button, the transaction is added to the blockchain.

if st.button("Complete Transaction"):
    transaction_complete = send_transaction(w3, account, seller_address, priceETH)
    st.write("Your transaction on the Ganache Blockchain tester is complete!")
    st.write("Here is the hash code confirming your transaction")
    st.write(f"{transaction_complete}")
    st.write("/n")
    if type == "Vehicle":
        st.markdown("## Congratulations on buying your vehicle!")
        st.balloons()
    else:
        st.markdown("## Congratulations on buying your motorcycle!")
        st.balloons()
                 
################################################################################
# Step 4:
# Streamlit “Add Block” button code so that when someone clicks the
# button, the transaction is added to the blockchain.
st.markdown("---")

st.write(
    " "
)

st.markdown("### *:red[Share with your friends and make buying and selling your lucky day!]*")

st.write(
    " "
)
st.markdown("If you liked this app give us a :thumbsup: it keeps us creating more great tools for the future of Blockchain!")

st.write("More infos and :star: at [github.com/arty-j/lucky_day](https://github.com/arty-j/lucky_day)")

# st.session_state["previous_style"] = style
################################################################################
