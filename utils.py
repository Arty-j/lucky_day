import streamlit as st
from web3 import Web3 as w3



@st.experimental_memo(show_spinner=False)
def getnums(s,e,i):
    """function to get list of numbers from 1980-2023 for selectbox veh_year"""
    return list(range(s,e,i))

# def getvalue(COIN,price):
#     """function to calculate price of vehicle sale in ethereum"""
# ######use api to get current rate of eth to usd, convert usd sale price to wei###
#     conversion_rate = 
#     if COIN == 'USD':
#         USD = price
#         eth = COIN * conversion_rate
#         wei = w3.toWei(eth, "ether")
#     return USD, eth, wei

# def compile_contract(data):
#     return smart_contract

