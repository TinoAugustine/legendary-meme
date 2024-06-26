import streamlit as st
import pandas

st.set_page_config(layout="wide")
st.header("The Best Company")
content = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint 
occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""

st.info(content)

st.subheader("Our Team")

col1, col2, col3 = st.columns(3)

# Make a dataframe with the company members

df = pandas.read_csv("data.csv", sep=",")

with col1:
    # Iterate over only the first four rows
    for index, row in df[:4].iterrows():
        # Add member's first and last names
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.subheader(row["role"])
        # Add member's photo
        st.image("images/"+row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.subheader(row["role"])
        st.image("images/"+row["image"])

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.subheader(row["role"])
        st.image("images/" + row["image"])
