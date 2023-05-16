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