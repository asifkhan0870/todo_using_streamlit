import streamlit as st
import numpy as np
import sympy as sp

if "history" not in st.session_state:

    st.session_state.history=[]


st.title("Sc. Calculator using streamlit")    

st.sidebar.title("History")

for i ,h in enumerate (reversed(st.session_state.history[-10:])):

      st.sidebar.text(f"{len(st.session_state.history)-i}: {h}")


if st.sidebar.button("Clear History"):

    st.session_state.history=[]
    st.sidebar.success("History Cleared")    


st.sidebar.markdown("---")
st.sidebar.markdown("Supports: + , − , ×  ,÷ , ^ , % , mod , √  ,log , sin/cos/tan")      


col1, col2 = st.columns(2)

with col1:
    a = st.text_input("Enter First Number / Expression", "")

with col2:
    b = st.text_input("Enter Second Number (if needed)", "")

operation = st.selectbox("Select Operation", [
    "Add ➕", "Subtract ➖", "Multiply ✖", "Divide ➗",
    "Power ^", "Mod %", "Percentage", "Square Root √",
    "Log (base 10)", "Sin", "Cos", "Tan"
])


result = None

if st.button("Compute"):


    try: 

        expr_a = sp.sympify(a)
        num_a = float(expr_a.evalf())

        num_b = float(sp.sympify(b).evalf()) if b else None

        if operation == "Add ➕":
            result = expr_a + num_b

        elif operation == "Subtract ➖":
            result = expr_a - num_b

        elif operation == "Multiply ✖":
            result = expr_a * num_b

        elif operation == "Divide ➗":
            if num_b == 0:
                st.error("❌ Cannot divide by zero!")
            else:
                result = expr_a / num_b

        elif operation == "Power ^":
            result = expr_a ** num_b

        elif operation == "Mod %":
            result = num_a % num_b

        elif operation == "Percentage":
            result = (num_a * num_b) / 100

        elif operation == "Square Root √":
            if num_a < 0:
                st.error("❌ Cannot find square root of negative number!")
            else:
                result = sp.sqrt(expr_a)

        elif operation == "Log (base 10)":
            if num_a <= 0:
                st.error("❌ Log is only defined for positive numbers!")
            else:
                result = sp.log(expr_a, 10)

        elif operation == "Sin":
            result = sp.sin(np.radians(num_a))
            # result = float(num_a * 180 / np.pi)
            # result=sp.sin(result)

        elif operation == "Cos":
            result = sp.cos(np.radians(num_a))

        elif operation == "Tan":
            result = sp.tan(np.radians(num_a))

        if result is not None:
            st.session_state.history.append(f"{a} {operation} {b if num_b is not None else ''} = {result}")
            # st.code(str(result))
            st.success(f"✅ Result: {result}")    

    except Exception as e:

        st.error(f"Error in calculation {e}")    

if result is not None:
    st.code(str(result))
    st.button("📋 Copy Result", on_click=lambda: st.toast("Copied! (select & Ctrl/Cmd+C)", icon="✅"))

