import pandas as pd
import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Abdulrasheed Shittu")
    content = """ Hi, I’m Abdulrasheed, a passionate Software Developer with a B.Eng in Electrical and Computer
    Engineering. I specialize in backend development using Python and Django, and I’ve successfully led and
     contributed to impactful projects across e-libraries, VAT audit systems, AI agents, and eCommerce platforms.
    With hands-on experience in cloud platforms, APIs, data pipelines, and full-stack development, I bring 
    a blend of technical expertise and problem-solving skills. My work emphasizes performance, security, 
    and real-world usability—whether it's building AI-powered platforms or creating scalable systems for organizations    
    """
    st.info(content)

content2 = """Below you will find some of the apps i have built. Feel free to contact me!
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv("datax.csv", sep=",", encoding="windows-1252")
df.columns = df.columns.str.strip()

with col3:
    for index, row in df[:6].iterrows():
        st.header(row["Title"])
        st.write(row["Description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code or Weblink]({row['URL']})")

with col4:
    for index, row in df[6:].iterrows():
        st.header(row["Title"])
        st.write(row["Description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code or Weblink]({row['URL']})")












