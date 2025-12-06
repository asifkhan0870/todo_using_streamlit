import streamlit as st

st.title("Calci by streamlit  ")

n1=st.number_input("Enter the first number: ",value=0.0)
n2=st.number_input("Enter the second number: ",value=0.0)

operand=st.selectbox("Choose the operation: ", ["Add", "Substract", "Multiplication", "Division"])

if st.button("compute"):

    if(operand=="Add"):

        res=n1+n2

    elif (operand=="Substract"):

        res=n1-n2

    elif(operand=="Multiplication"):

        res=n1*n2

    else :
        if n2==0:
            res="Infinity"
        else:
            res=n1/n2

    st.success(f"Result {res}")            