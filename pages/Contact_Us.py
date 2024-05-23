import streamlit as st
import send_email
import pandas

st.header("Contact Us")

df = pandas.read_csv("topics.csv", sep=",")

with (st.form(key="Contact_Form")):
    email = st.text_input("Enter Your Email")
    option = st.selectbox(
        'Select Topic',
        df["topic"])
    raw_message = st.text_area("Enter Your Message")
    message = f"""\
Subject: New Website Enquiry + {email}

From: {email}
Topic {option}
{raw_message}
"""
    button = st.form_submit_button("Send Email")
    if button:
        send_email.send_email(message)
        st.info("Your Email was sent Successfully!")
