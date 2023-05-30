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
    st.header('Target Goal')
    st.write('We wanted to show how easy and fast you can build web-applications in Python only using the streamlit package. The result can be seen under 🧮:orange[Calculator] in the sidebar.')
    st.write("If you're interested how our code works you should click on 👨‍💻:orange[Code].")
    
# ---- Credits ----
with st.container():
    st.write('---')
    
    st.header('Contributers')
    #col1,col2,col3,col4 = st.columns(4)
    col1,col2 = st.columns(2)
    col3,col4 = st.columns(2)
    
    with col1:
        st.image('assets/img/GP_GitHub.jpg',use_column_width=True, caption='German Paul')
    with col2:
        st.image('assets/img/MG_GitHub.jpg',use_column_width=True, caption='Michael Greif')
    # with col3:
    #   st.image('assets/img/F_GitHub.jpg',use_column_width=True, caption='Finn')
    # with col4:
    #   st.image('assets/img/DS_GitHub.jpg',use_column_width=True, caption='David Siregar')
