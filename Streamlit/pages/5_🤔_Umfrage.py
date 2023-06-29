import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Umfrage Ergebnisse")

df = pd.read_csv("UmfrageDaten.csv")
chart, ax = plt.subplots()
ax.bar(x=df.columns, height=df.iloc[0])
ax.set_yticks([i for i in range(31)])
"Chart der Ergebnisse", chart


st.video("https://www.youtube.com/watch?v=IxAKFlpdcfc")