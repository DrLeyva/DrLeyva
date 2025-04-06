import streamlit as st
from SendEmail import SendEmail

st.header("Contact Me")

with st.form(key ="email_forms"):
    user_email = st.text_input("Your Email address")
    raw_message = st.text_area("Your Message")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    print(button)
    if button:
        SendEmail(message)
        st.info("Your email was sent Successfully")
        #message = message + user_email
        print("Button was pressed")


        #print(button) will show boolean True!