import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config('Calculator',page_icon='🧮')
state = st.session_state

def main():

    # Calculator
    with st.container():
        st.title("Calculator App using Streamlit",)
        st.write("---")  # creates a horizontal line
        
        st.write("Operation")
        op = st.radio(
            "Select an operation to perform:",
            ("Add ( + )", "Subtract ( - )", "Multiply ( * )", "Divide ( / )"),
            key='operationCalc'
        )
        
        num1 = st.number_input(label="Enter first number",value=0,key='number1')
        num2 = st.number_input(label="Enter second number",value=0,key='number2')
        calculate(num1, num2, op)
        
        st.write("---")  # creates a horizontal line

    # CSV - Calculator
    with st.container():
        st.title("Calculator App using Streamlit")
        st.write("---")
        st.subheader(
            "Please provide a csv as shown in the example below. Column names should be the same.")
        
        df = pd.read_csv("Streamlit/data/calc_csv.csv")
        df

        st.subheader("Upload Csv")
        csv_file = st.file_uploader("Upload Csv",
                                    type=["csv"])

        if csv_file:
            data = pd.read_csv(csv_file)

        if st.button("Calculate result", key='csv'):
            result = [calculate(df.num1.iloc[i], df.num2.iloc[i],
                                df.op.iloc[i], return_message=False) for i in range(len(df))]

            df["result"] = result
            df        
            
# ---- METHODES ----

@st.cache_data
def calculate(num1:(int|float), num2:(int|float), op:(str), return_message:(bool)=True):
    '''
    Calculate any numbers with basic operators
    @param num1: Set to any numeric
    @param num2: Set to any numeric
    @param op: Choose your operator of choice
    @param return_message: Let's you choose between displaying only a return message of your calculation or returning the result default: True
    @return: Returns your mathematic result
    '''
    ans = 0
    match op:
        case '+' | 'Add ( + )':
            operator = '+'
            ans = num1 + num2
        case "-" | 'Subtract ( - )':
            operator = '-'
            ans = num1 - num2
        case "*" | 'Multiply ( * )':
            operator = '*'
            ans = num1 * num2
        case "/" | 'Divide ( / )':
            operator = '/'
            if num2 != 0:
                ans = num1 / num2
            else:
                st.error(":color[:red[ERROR:]] Division by 0. Please enter a non-zero number.")
                ans = np.NaN
                st.error(f"{state['number1']} {operator} :red[{state['number2']}] = {ans}")
                return ans
        case other:
            st.error('This should not happen! Please report to the authorities')
    if return_message:
        st.success(f"{state['number1']} {operator} {state['number2']} = {round(ans,6)}")
        return ans
    else:
        return ans

if __name__ == '__main__':
    main()
