import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("The Best Company")
content = """
   Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam luctus sollicitudin nunc non facilisis. 
   Sed venenatis quis nisl eget tempus. Pellentesque et mi dignissim, tincidunt diam posuere, pharetra lectus. 
   Phasellus interdum risus ipsum, hendrerit luctus orci facilisis vel. Nam risus metus, mollis ut mattis porttitor,
    vulputate vel neque. Morbi venenatis non magna sed feugiat. Aenean non eros et ex dictum pulvinar eget ut quam. 
    Proin ut odio nibh.
   """
st.write(content)
st.header("Our Team")

col1, col2, col3 = st.columns(3)

df = pd.read_csv("data.csv")

with col1:
    for index, row in df[:4].iterrows():
        st.header(f"{row['first name']} {row['last name']}".title())
        st.write(row["role"])
        st.image(f"images/{row['image']}")


with col2:
    for index, row in df[4:8].iterrows():
        st.header(f"{row['first name']} {row['last name']}".title())
        st.write(row["role"])
        st.image(f"images/{row['image']}")


with col3:
    for index, row in df[8:].iterrows():
        st.header(f"{row['first name']} {row['last name']}".title())
        st.write(row["role"])
        st.image(f"images/{row['image']}")