import streamlit as st
import math

# Title of the app
st.title("Pilot Pass")

# Displaying some text
st.write("See how easy is to guess your password")

#input boxes
st.subheader("Enter Your Personal Details")
name = st.text_input("Your Name")
surname = st.text_input("Your Surname")
dob = st.date_input("Date of Birth")

#conformation button and input data conformation
if st.button("submit"):
    st.subheader("Entered Details:")
    st.write(f"**Name:** {name}")
    st.write(f"**Surname:** {surname}")
    st.write(f"**Date of Birth:** {dob}")

#thats it for now, the rest is merging of fron n back end to show results of external py code
#i think that we should show the list of guessed passwords, and make it like a psa to make stronger passwords
#still looking into how to make a seperet tab for information about system o7

