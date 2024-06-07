import streamlit as st

def main():
    st.title("Perfectly Odd Calculator")
    st.write("Enter a number below and click on the button to calculate its square.")

    # Input field for the user to enter a number
    number = st.number_input("Enter a number", value=0.0)

    # Button to calculate square
    if st.button("Calculate Square"):
        square = number * number
        st.write(f"The square of {number} is: {square}")

if __name__ == "__main__":
    main()
