import streamlit as st

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