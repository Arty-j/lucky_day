# Lucky Day Blockchain Application
################################################################################

################################################################################
# Imports
import streamlit as st
# from streamlit_image_select import image_select
from wallet import get_balance, generate_account

import datetime as datetime
from dataclasses import dataclass
from typing import Any, List
import pandas as pd
import datetime as datetime
import hashlib
from utils import getnums
#from utils import getvalue
from web3 import Web3 as w3





################################################################################
# Step 1:
# Creates the Block and PyChain data classes

@dataclass
class Block:
    data: Any
    buyer: int
    seller: int
    value: int
    gas: int
    prev_hash: str = "0"
    timestamp: str = datetime.datetime.utcnow().strftime("%H:%M:%S")

    def hash_block(self):
        sha = hashlib.sha256()

        data = str(self.data).encode()
        sha.update(data)

        buyer = str(self.buyer).encode()
        sha.update(buyer)

        seller = str(self.seller).encode()
        sha.update(seller)

        value = str(self.value).encode()
        sha.update(value)

        timestamp = str(self.timestamp).encode()
        sha.update(timestamp)

        prev_hash = str(self.prev_hash).encode()
        sha.update(prev_hash)

        return sha.hexdigest()


# Create the data class PyChain
@dataclass
class PyChain:
    chain: List[Block]

    def add_block(self, block):
        self.chain += [block]


################################################################################
# Step 2:
# Streamlit Code
# Adds the cache decorator for Streamlit, Initializes the Blockchain
@st.cache(allow_output_mutation=True)
# st.set_page_config(page_title="luckyday", page_icon=None)

st.markdown("# Lucky Day")
st.markdown("## Blockchain Smart Contract App")
st.markdown("**Conduct your transactions via a transparent, trustworthy decentralized network**")

################################################################################
# Step 3:
# Streamlit Main Page Form for data capture

#sets up the form with 3 columns
st.write("")
form = st.form(key="form_settings")
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
style = col3.slider(
    "Excitement Level",
    0,
    100,
    key="excitement",
)

#Form expander for selection options
expander = form.expander("Customize Your Transaction")
if type == "Vehicle":
    #run a function in different py file? to gather form details?
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
        max_chars=20,
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
        max_chars=40,
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
        max_chars=40,
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
        "Sale Transaction Price",
        help="This is agreed sale price in the coin of choice listed above",
        key="veh_price",
    )
    # USD, eth, wei = getvalue(veh_pmtCOIN,veh_price)
    # st.write(f"Sale transaction price will be ${USD}USD or {eth}, transacted on the Ethereum network as {wei}wei")


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
    
    # Final Form submittal of data to create smart contract or simply place transaction on blockchain
    st.markdown("---")
form.form_submit_button(label="##Review")
    # if submitted:
    #         st.write(f'The sale transaction of this vehicle, will be {buyer_name} at {buyer_address} paying {seller_name} at {seller_address} {veh_price}, in {veh_pmtCOIN}')
            # if level == "Smart Contract Enabled":
            #     with st.spinner("Creating your smart contract for final review...(may take a minute)"):
            #     smart_contract = compile_contract(submitted)
            #     print(smart_contract)
            # else:
            #     input_data = [veh_make, veh_model, veh_color, veh_vin, veh_title, veh_pmtCOIN, veh_price]
input_data = [veh_make, veh_model, veh_color, veh_vin, veh_title, veh_pmtCOIN, veh_price, gas]
wei = w3.toWei(veh_price, "ether")
st.write(f"The sale transaction of this vehicle, will be: {buyer_name} at {buyer_address} paying {seller_name} at {seller_address}, {veh_price} {veh_pmtCOIN}, for the {veh_make} {veh_model}")
# if style == 100:
#     st.balloons

################################################################################


################################################################################
# Step 4:
# Modify the Streamlit “Add Block” button code so that when someone clicks the
# button, the code adds a new block to the blockchain.

if st.button("Complete Transaction and Add Block to Blockchain"):
    # Select the previous block in the chain
    prev_block = pychain.chain[-1]
    # Hash the previous block in the chain
    prev_block_hash = prev_block.hash_block()
    # Create a new block in the chain
    new_block = Block(data=input_data, buyer=buyer_address, seller=seller_address, value=wei, gas=gas, prev_hash=prev_block_hash)
    # Add the new block to the chain
    pychain.add_block(new_block)


# Create a Pandas DataFrame to display the `PyChain` ledger
pychain_df = pd.DataFrame(pychain.chain)

# Use the Streamlit `write` function to display the `PyChain` DataFrame
st.write(pychain_df)

################################################################################

st.markdown("---")
st.write(
    "Share with your friends and make buying and selling your lucky day!"
)
st.markdown(
    "More infos and :star: at [github.com/arty-j/lucky_day](https://github.com/arty-j/lucky_day)"
)

# st.session_state["previous_style"] = style
################################################################################
