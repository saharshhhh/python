import streamlit as st
st.title("Gross Salary Calculator")
basicSal=st.number_input("Enter the basic Salary", min_value=0, step=1)
if st.button("Calculate Gross Salary"):
    hra=0
    da=0
    if basicSal<10000:
        hra= basicSal* 0.67
        da= basicSal*0.73
    elif basicSal>=10000 and basicSal<20000:
        hra= basicSal * 0.69
        da= basicSal * 0.76
    else:
        hra= basicSal* 0.73
        da= basicSal*0.89
    Gross= basicSal+hra+da
    st.success(Gross)


