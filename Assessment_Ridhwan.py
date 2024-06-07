import streamlit as st

def calculate_cpf_contribution(age, salary):
    # Minimum age for CPF contribution is 16
    if age < 16:
        st.error("Minimum age for CPF contribution is 16.")
        return None, None

    # Define CPF contribution rates based on age
    if age < 55:
        employee_contribution_rate = 0.20
        employer_contribution_rate = 0.17
    elif 55 <= age < 60:
        employee_contribution_rate = 0.13
        employer_contribution_rate = 0.13
    elif 60 <= age < 65:
        employee_contribution_rate = 0.075
        employer_contribution_rate = 0.09
    else:
        employee_contribution_rate = 0.05
        employer_contribution_rate = 0.075

    # Calculate CPF contributions
    employee_contribution = salary * employee_contribution_rate
    employer_contribution = salary * employer_contribution_rate

    return employee_contribution, employer_contribution

def main():
    # Prompt user for age and salary
    age = st.number_input("Enter your age:", min_value=16, value=30)
    salary = st.number_input("Enter your monthly salary: $", min_value=0.0, value=3000.0)

    # Calculate CPF contributions
    employee_cpf, employer_cpf = calculate_cpf_contribution(age, salary)

    # Display the results if age is valid
    if employee_cpf is not None and employer_cpf is not None:
        st.write("\nCPF Contribution Calculator")
        st.write("Age:", age)
        st.write("Monthly Salary: $", salary)
        st.write("Employee CPF Contribution: $", employee_cpf)
        st.write("Employer CPF Contribution: $", employer_cpf)

if __name__ == "__main__":
    main()
