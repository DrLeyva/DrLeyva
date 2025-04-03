import streamlit as st  # st is the module
from pathlib import Path
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns([1, 2])  # columns is the method  & col1 and col2 are the instances or objects

with col1:
    image_path = r"C:\Users\aaron\OneDrive\Desktop\resume\GitHub\PytonMegaCourse\app2-portfolio\images\photo2.png"
    st.image(image_path, width=400)
with col2:
    st.title("Aaron Leyva")
    content = """
   My name is Aaron Leyva. I am python programmer looking to advance in the world of software development and machine learning engineering. 

    """
    # You can use st.markdown for custom styling
    # st.markdown(f"<div style='font-size: 18px; line-height: 1.4;'>{content}</div>", unsafe_allow_html=True)

    st.info(content)

    content2 = """
    Below you can find apps I have built on python.
        """
    st.write(content2)
    
    col3, col4 = st.columns(2)

    df = pandas.read_csv("data.csv", sep=";")
    
    with col3:
        for index, row in df[:10].iterrows():
            st.header(row["title"])

    with col4:
        for index, row in df[10:].iterrows():
            st.header(row["title"])
