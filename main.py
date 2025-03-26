import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)
with col1:
    st.image("images/photo.png")
with col2:
    st.title("Neeraj Shimpi")
    content = '''
    Hi, I'm Neeraj Shimpi, a first-year Computer Engineering student passionate about automation, software development, and problem-solving. I enjoy working on Python projects, exploring new technologies, and optimizing systems for efficiency. With a strong foundation in programming and a keen interest in finance, investing, and professional growth, I'm continuously learning and building solutions that make an impact. My goal is to secure a high-paying tech role while gaining hands-on experience through internships and projects.
    '''
    st.info(content)