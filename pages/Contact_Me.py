import streamlit as st
import send_email as se

st.header("Contact Me")

with st.form(key="email_form", clear_on_submit=True):
    user_email = st.text_input("Enter Your Email")
    user_message = st.text_area("Enter your message")
    button = st.form_submit_button("Submit")

if button:
    se.sendmail(user_email_local = user_email, message_local = user_message)