# CTI-110
# P4HW2 - Salary Calculator
# Christian Slater
# 11/15/2023


# This program calculates the pay for employees based on their pay rate and hours worked.

# Initialize variables to keep track of totals
overtime_total = 0
regular_pay_total = 0
gross_pay_total = 0
num_employees = 0

# Start a loop to continuously ask for employee information
while True:
    # Ask the user for the employee's name
    employee_name = input("Enter employee name (or 'Done' to terminate program): ")

    # Check if the user wants to terminate the program
    if employee_name.lower() == "done":
        break

    # Ask for pay rate and hours worked
    pay_rate = float(input("Enter pay rate: "))
    hours_worked = float(input("Enter hours worked: "))

    # Calculate regular pay and overtime pay
    if hours_worked > 40:
        regular_pay = 40 * pay_rate
        overtime_pay = (hours_worked - 40) * (1.5 * pay_rate)
    else:
        regular_pay = hours_worked * pay_rate
        overtime_pay = 0

    # Calculate gross pay and update totals
    gross_pay = regular_pay + overtime_pay
    overtime_total += overtime_pay
    regular_pay_total += regular_pay
    gross_pay_total += gross_pay
    num_employees += 1

# Display the results
print("\nOvertime total:", overtime_total)
print("Regular pay total:", regular_pay_total)
print("Gross pay total:", gross_pay_total)
print("Number of employees entered:", num_employees)
