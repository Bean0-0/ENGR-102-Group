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
# Assignment: Lab 3
# Date: 9/9/2025
#
#
#
from math import*


quantity = float(input("Please enter the quantity to be converted: "))

#pounds --> newtons
pounds_to_newtons_converter = 4.45
newtons = quantity * pounds_to_newtons_converter
print (f"{quantity:.2f} pounds force is equivalent to {newtons:.2f} newtons")

#meters --> feet
meters_to_feet_converter = 3.28
feet = quantity * meters_to_feet_converter
print (f"{quantity:.2f} meters is equivalent to {feet} feet")

#atmospheres --> kilopascals
atmospheres_to_kilopascals_converter = 101.33
kilopascals = quantity * atmospheres_to_kilopascals_converter
print (f"{quantity:.2f} atmospheres is equivalent to {kilopascals} kilopascals")


