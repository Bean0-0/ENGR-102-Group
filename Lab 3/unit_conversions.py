# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Benjamin Nasse 
# Cameron Seal
# Charles Thomas
# Nicholas Strickler
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
print (f"{quantity:.2f} meters is equivalent to {feet:.2f} feet")

#atmospheres --> kilopascals
atmospheres_to_kilopascals_converter = 101.33
kilopascals = quantity * atmospheres_to_kilopascals_converter
print (f"{quantity:.2f} atmospheres is equivalent to {kilopascals:.2f} kilopascals")

#watts to BTU
watts_to_BTU_converter=3.41
BTU=quantity*watts_to_BTU_converter
print(f"{quantity:.2f} watts is equivalent to {BTU:.2f} BTU per hour")

#liters per second to gallons
lps_to_gpm_converter=15.8503
GPM=quantity*lps_to_gpm_converter
print(f"{quantity:.2f} liters per second is equivalent to {GPM:.2f} US gallons per minute")

#celsius to farenheit
faren=(9/5)*quantity+32
print(f"{quantity:.2f} degrees celsius is is equivalent to {faren:.2f} degrees fahrenheit")



