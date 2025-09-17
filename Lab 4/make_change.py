# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Benjamin Nasse
# Cameron Seal
# Charles Thomas
# Nicholas
# Radwan Merhebi
# Section: 564
# Assignment: Lab 4
# Date: 9/17/2025
#
#
#

# Get inputs
paid = float(input("How much did you pay? "))
cost = float(input("How much did it cost? "))

# Calculate change
change = paid - cost
change_cents = round(change * 100)  # work in cents to avoid float issues

print(f"You received ${change:.2f} in change. That is...")

# Quarters
quarters = change_cents // 25
change_cents = change_cents % 25

# Dimes
dimes = change_cents // 10
change_cents = change_cents % 10

# Nickels
nickels = change_cents // 5
change_cents = change_cents % 5

# Pennies
pennies = change_cents

# Only print if greater than 0
if quarters > 0:
    if quarters == 1:
        print("1 quarter")
    else:
        print(f"{quarters} quarters")

if dimes > 0:
    if dimes == 1:
        print("1 dime")
    else:
        print(f"{dimes} dimes")

if nickels > 0:
    if nickels == 1:
        print("1 nickel")
    else:
        print(f"{nickels} nickels")

if pennies > 0:
    if pennies == 1:
        print("1 penny")
    else:
        print(f"{pennies} pennies")

