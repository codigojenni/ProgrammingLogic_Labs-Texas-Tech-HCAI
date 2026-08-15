# lab3_program2_Jennifer_MendozaTrejo.py

# importing function from module
from mymodule_Jennifer_MendozaTrejo import pay_calculator

print("")
print("-----------------------------------------------------")
print("Welcome to the Employee Weekly Pay Calculator!")

# user input

hourly_wage = float(input("Enter hourly wage:"))
regular_hours = float(input("Enter total regular hours:"))
overtime_hours = float(input("Enter total overtime hours: "))

# calculating pay using function we imported from module 

total_pay = pay_calculator(hourly_wage, regular_hours, overtime_hours)

#printing results
print("")
print("-----------------------------------------------------")
print(f"Total weekly pay: ${total_pay:.2f}")
print("")
print("-----------------------------------------------------")
print("Completed by, Jennifer Mendoza Trejo")

