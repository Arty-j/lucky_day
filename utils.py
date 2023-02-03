import streamlit as st
from bip44 import Wallet
from eth_account import Account
from web3 import middleware
from web3.gas_strategies.time_based import medium_gas_price_strategy
from web3 import Web3
w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))


@st.experimental_memo(show_spinner=False)
def getnums(s,e,i):
    """function to get list of numbers from 1980-2023 for selectbox veh_year"""
    return list(range(s,e,i))


################################################################################

def get_price(w3,veh_pmtCOIN, veh_price):
    """function to calculate price of vehicle sale in USD, ethereum & wei"""
######use api to get current rate of 1usd to eth, set = to conversion_rate ** currently using static rate for code testing#######

    #conversion rate is $1USD to ETH
    conversion_rate = 0.0006030253783230467

    if veh_pmtCOIN == 'USD':
        veh_priceUSD = veh_price
        
        #change veh_priceUSD to a float to multipy times a float(conversion_rate)
        veh_priceETH_float = float(veh_priceUSD) * float(conversion_rate)
        
        #calculation result veh_priceETH_float, changed back to a string to use in w3
        veh_priceETH = str(veh_priceETH_float)
        
        veh_priceWEI = w3.toWei(veh_priceETH, "ether")
        
    elif veh_pmtCOIN =='ETH':
        veh_priceETH = veh_price
        veh_priceWEI = w3.toWei(veh_priceETH, "ether")
        
        #change veh_priceETH to a float to be divided by the float(conversion_rate)
        veh_priceUSDfloat = float(veh_priceETH) / float(conversion_rate)
        
        #calculation result veh_priceUSDfloat, changed back to a string for type coninuity
        veh_priceUSD = str(veh_priceUSDfloat)
    
    return veh_priceUSD, veh_priceETH, veh_priceWEI

################################################################################

def send_transaction(w3, account, buyer_address, veh_priceETH):
    """Send an authorized transaction to the Ganache blockchain."""
    # Set gas price strategy
    w3.eth.setGasPriceStrategy(medium_gas_price_strategy)

    # Convert eth amount to Wei
    value = w3.toWei(veh_priceETH, "ether")

    # Calculate gas estimate
    gasEstimate = w3.eth.estimateGas({"to": buyer_address, "from": account.address, "value": value})

    # Construct a raw transaction
    raw_tx = {
        "to": buyer_address,
        "from": account.address,
        "value": value,
        "gas": gasEstimate,
        "gasPrice": 0,
        "nonce": w3.eth.getTransactionCount(account.address)
    }

    # Sign the raw transaction with ethereum account
    signed_tx = account.signTransaction(raw_tx)

    # Send the signed transactions
    return w3.eth.sendRawTransaction(signed_tx.rawTransaction)

################################################################################
    