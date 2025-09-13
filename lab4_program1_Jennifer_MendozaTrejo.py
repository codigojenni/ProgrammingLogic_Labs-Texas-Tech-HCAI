print("")
print("------------------------------------------------------")
print("Welcome to the video renter calculator! ")
print("------------------------------------------------------")

print("")

# ask for user input
new_releases = int(input("Enter the number of new releases: "))
oldies = int(input("Enter the number of oldies: "))
number_nights = int(input("Enter the number of nights you will be renting: "))

total_movies = new_releases + oldies

new_releases_price = 3.00
oldie_price = 2.00

new_releases_cost = new_releases * new_releases_price * number_nights
oldies_cost = oldies * oldie_price * number_nights
total_cost = new_releases_cost + oldies_cost

#labor day promotion
discount_applied = False
if total_movies >= 10 or total_cost >= 50:
      discount = total_cost * 0.20
      total_cost -= discount
      discount_applied = True


# final cost - end of code
print("")
print("------------------------------------------------------")
if discount_applied:
      print("Labor Day Special applied! You received a 20% discount.")
print(f"The customer's total rental cost is: ${total_cost:.2f}")
print("------------------------------------------------------")
print("")
print("------------------------------------------------------")
print("This program was completed by, Jennifer Mendoza Trejo")
print("------------------------------------------------------")