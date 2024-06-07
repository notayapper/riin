import streamlit as st

def grocery(order):
    discount = 25 if order > 200 else 0
    disc_amt = discount * order / 100
    tax = 0.07 * (order - disc_amt)
    return disc_amt, tax

st.title("Ridhwan Grocery Calculator")

order = st.number_input("Enter the amount of your order:", min_value=0.0, format="%.2f")

if st.button("Calculate"):
    discount, tax = grocery(order)
    st.write(f"The discount is ${discount:.2f}")
    st.write(f"The tax is ${tax:.2f}")
