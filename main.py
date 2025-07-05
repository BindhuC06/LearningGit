import streamlit as st
import logging

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
    pass
