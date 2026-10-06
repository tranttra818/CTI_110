# Trong Tran
# 10/06/2026
# Determine weekly pay using if/else and streamlit for the UI
# Steps to run -> cd into where your file lives
# python -m streamlit run P3HW2_TranTrong.py
import streamlit as st

st.title("PayCheck Calculator 🤑")


# Get name
name = st.text_input("Enter employee name: ")

# Get hours worked for the week
hours = st.number_input("Enter hours worked for the week: ")

# Get base(regular) pay rate
base_pay_rate = st.number_input("Enter base pay rate: $")


# If statement that is TRUE when they work more than 40 hours
if hours > 40:
    OT_hours = hours - 40
    OT_pay = OT_hours * (base_pay_rate*1.5)
    reg_pay = base_pay_rate * 40
    gross_pay = OT_pay + reg_pay
    
if hours <= 40:
    OT_hours = 0
    OT_pay = 0
    reg_pay = base_pay_rate * hours
    gross_pay = OT_pay + reg_pay

# Display the results
st.write(f"Employee name: {name}")
st.write(f"Hours Worked: {hours}")
st.write(f"Pay Rate: ${base_pay_rate:.2f}")
st.write(f"Overtime Hours: {OT_hours}")
st.write(f"Overtime Pay: ${OT_pay:.2f}")
st.write(f"Regular Pay: ${reg_pay:.2f}")
st.write(f"Gross Pay: ${gross_pay:.2f}")