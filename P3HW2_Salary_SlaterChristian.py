#CTI-110
#P3HW2 - Salary
#Christian Slater
#10/23/2023


#Ask the user to enter employee name
name = input("Enter Employee's Name: ")
#Ask user to enter number of hours employee worked
hours = float (input("Enter Number of Hours Worked: "))
#Ask user to enter employee's rate of pay
rate = float (input("Enter Employee's Pay Rate: "))
#Calculate if user worked overtime (over 40 hours)

if hours >40 :

    overtime = hours - 40

    over_pay = rate * 1.5 * overtime

    gross_pay = rate * 40 + over_pay

else:

    gross_pay - hours * rate

print("-----------------------------")
print("Employee name:    ", name)


print("Hours Worked  Pay Rate  Overtime  Overtime Pay  RegHour Pay  Gross Pay")
print("-------------------------------------------------------------------------")
print(f'{hours}          {rate}        {overtime}         {over_pay}      {rate}        {gross_pay}')
      
