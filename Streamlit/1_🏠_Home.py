import streamlit as st
import numpy as np
import pandas as pd

# PageConfig
st.set_page_config(page_title='Homepage',page_icon='🏠')
st.sidebar.success('Select a page above ⬆')

# ---- HEADER SECTION ----
with st.container():
    st.title('Fortgeschrittene Programmierung - Webapplikation')
    st.write('You want to see our code? ➡ Check out our [Github Repository](https://github.com/GermanPaul12/Streamlit-and-Voila-Website-Fortgeschrittene-Programmierung) 💡')

# ---- MAIN SECTION ----
with st.container():
    st.write('---')
    
    st.header('Contributers')
    col1,col2,col3,col4 = st.columns(4)
    
    col1 = st.image('assets/img/GP_GitHub.jpg',use_column_width=True)
    col2 = st.image('assets/img/MG_GitHub.png',use_column_width=True)
    col3 = st.image('assets/img/F_GitHub.png',use_column_width=True)
    col4 = st.image('assets/img/DS_GitHub.png',use_column_width=True)
    st.header('Target Goal')
    st.write()