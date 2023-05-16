import streamlit as st
import numpy as np
import pandas as pd


def calculate(num1,num2,op):
    ans = 0
    if op == "+":
        ans = num1 + num2
    elif op == "-":
        ans = num1 - num2
    elif op == "*":
        ans = num1 * num2
    elif op=="/" and num2!=0:
        ans = num1 / num2
    else:
        ans = "Not defined"
    return ans

 
st.title("Calculator App using Streamlit")
 
# creates a horizontal line
st.write("---")

st.subheader("Please provide a csv as shown in the example below. Column names should be the same.")
df = pd.read_csv("Streamlit/data/calc_csv.csv")
df

st.subheader("Upload Csv")
csv_file = st.file_uploader("Upload Csv",
type=["csv"])

if csv_file is not None:
    data = pd.read_csv(csv_file)   
    

if st.button("Calculate result"):
    result = [calculate(df.num1.iloc[i], df.num2.iloc[i], df.op.iloc[i]) for i in range(len(df))]

    df["result"] = result
    df
