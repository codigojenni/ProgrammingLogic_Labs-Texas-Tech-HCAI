print("")
print("------------------------------------------------------")
print("Welcome to the video renter calculator! ")
print("------------------------------------------------------")

print("")

# ask for user input
new_releases = int(input("Enter the number of new releases: "))
oldies = int(input("Enter the number of oldies: "))
number_nights = int(input("Enter the number of nights you will be renting: "))

new_releases_cost = new_releases * 3.00 * number_nights
oldies_cost = oldies * 2.00 * number_nights

total_cost = new_releases_cost + oldies_cost

# final cost - end of code
print("")
print("------------------------------------------------------")
print(f"The customer's total rental cost is: ${total_cost:.2f}")
print("------------------------------------------------------")
print("")
print("------------------------------------------------------")
print("This program was completed by, Jennifer Mendoza Trejo")
print("------------------------------------------------------")
