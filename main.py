import streamlit as st
import logging
from datetime import datetime
from utils.coin_flip import get_heads_or_tails
from utils.roll_dice import roll_dice
from utils.random_str import get_random_string_of_length_6


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

move_ahead = False

st.title("It's saturday !!")
user_name = st.text_input("Enter your name")

if user_name: 
    move_ahead = not move_ahead
    logger.info(f"User entered name: {user_name}")
    st.write(f"Hi {user_name}")
else:
    logger.warning("No name entered by the user.")

if move_ahead:
    st.write(datetime.now())

    heads_or_tails = get_heads_or_tails()

    st.write(f"Result of coin flip: {heads_or_tails}")

    dice_roll = roll_dice()

    st.write(f"Result of dice roll: {dice_roll}")

    random_string_of_length_6 = get_random_string_of_length_6()

    st.write(f"Random string of length 6: {random_string_of_length_6}")