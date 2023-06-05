import streamlit as st

st.title("Our Calculator Code 💻")
st.subheader("If you like to see the whole code then feel free to checkout our Github")
st.code('''
        import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px


st.set_page_config('Calculator',page_icon='🧮')
state = st.session_state



def main():
    if 'calc_list' not in st.session_state:
        st.session_state.calc_list = []
    # Sidebar
    with st.sidebar:
        st.title("Sections")
        st.markdown("[Start](#calculator-app-using-streamlit)", 
            unsafe_allow_html=True)
        st.markdown("[Simple Calculator](#simple-calculator)", 
            unsafe_allow_html=True)
        st.markdown("[CSV Calculator](#csv-calculator)", 
            unsafe_allow_html=True)
    
    # Calculator
    with st.container():
        st.title("Calculator App using Streamlit")
        st.write("---")  # creates a horizontal line
        st.header("Simple Calculator",)
        st.write("---")  # creates a horizontal line
        
        st.write("Operation")
        op = st.radio(
            "Select an operation to perform:",
            ("Add ( + )", "Subtract ( - )", "Multiply ( * )", "Divide ( / )"),
            key="operationCalc"
        )
        
        num1 = st.number_input(label="Enter first number",
            value=0,key="number1")
        num2 = st.number_input(label="Enter second number",
            value=0,key="number2")
        calculate(num1, num2, op)
        
        with st.expander("History List of the last 10 calculations"):
            if len(st.session_state.calc_list) > 1:
                for i in st.session_state.calc_list:
                    st.write(i)
            elif len(st.session_state.calc_list) == 1:
                st.write(st.session_state.calc_list[0])
            else:
                st.write("No previous calculations")            
        st.write("---")  # creates a horizontal line

    # CSV - Calculator
    with st.container():
        st.header("CSV Calculator")
        st.write("---")
        st.subheader(
            "Please provide a csv as shown in the example below. Column names should be the same.")
        
        df = pd.read_csv("Streamlit/data/calc_csv.csv")
        df

        st.subheader("Upload Csv")
        
        csv_file = st.file_uploader("Upload your csv file to calculate results for whole dataset",
                                    type=["csv"])
        if csv_file:
            data = pd.read_csv(csv_file)

        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                calc_result = st.button("Calculate result ad create insights", 
                    key='csv')
            with col2:
                save_file = st.button("Download Csv")
        
        if calc_result:
            if csv_file:
                with st.expander("Exapnd to see results"):
                    
                    results = [calculate(data.num1.iloc[i], data.num2.iloc[i],
                                        data.op.iloc[i], return_message=False) for i in range(len(data))]

                    data["result"] = results
                    data       
                    op_count = data.op.value_counts()
                    bar = px.bar(op_count, 
                        title="How many operations are there in the dataset for each operator")
                    pie = px.pie(op_count, 
                        values="op", names=op_count.index, 
                        title="Distribution of operators in the dataset")
                    st.plotly_chart(bar)
                    st.plotly_chart(pie)
            else:
                st.warning("Please upload a csv file")    
            
        
        if save_file:
            if csv_file is not None:
                # To See details
                csv_details = {"file_name":csv_file.name,
                "file_type":csv_file.type,
                                "file_size":csv_file.size}
                st.write(csv_details)
                # To save uploaded Csv
                results = [calculate(data.num1.iloc[i], data.num2.iloc[i],
                                    data.op.iloc[i], 
                                    return_message=False) for i in range(len(data))]

                data["result"] = results     
                data.to_csv("downloaded_streamlit_csv.csv", index=False)       
                    
                st.success("Csv Saved Successfully")
                
            else:
                st.warning("No Csv File is Uploaded")     
    

   
# ---- METHODES ----
def add_calculation_to_history(calculation):
    """
    Adds given calculation to the history
    @param calculation: The calculation to add to history
    """
    st.session_state.calc_list.append(calculation) 

@st.cache_data
def calculate(num1:(int|float), num2:(int|float), op:(str), return_message:(bool)=True):
    """
    Calculate any numbers with basic operators
    @param num1: Set to any numeric
    @param num2: Set to any numeric
    @param op: Choose your operator of choice
    @param return_message: Let's you choose between displaying only a return message of your calculation or returning the result default: True
    @return: Returns your mathematic result
    """
    ans = 0
    match op:
        case "+" | "Add ( + )":
            operator = "+"
            ans = num1 + num2
        case "-" | "Subtract ( - )":
            operator = "-"
            ans = num1 - num2
        case "*" | "Multiply ( * )":
            operator = "*"
            ans = num1 * num2
        case "/" | "Divide ( / )":
            operator = "/"
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
        add_calculation_to_history(f"{state['number1']} {operator} {state['number2']} = {round(ans,6)}")
        st.success(f"{state['number1']} {operator} {state['number2']} = {round(ans,6)}")
        return ans
    else:
        return ans

if __name__ == '__main__':
    main()
''')