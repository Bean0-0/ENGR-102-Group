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
number = float(1)

pounds_in_newtons = (number * 4.45)
meters_in_feet = (number * 3.28)
Atmospheres_to_kilopascals = (number * 101.33)
watts_to_btu_per_hour = (number *  3.41)
liters_to_gallons= ((number * 60) * 0.264 + .01)
dc_to_df = ((number * (9.000/5.000) + 32))
formatted = format (dc_to_df , ".2f")
form = format (liters_to_gallons, ".2f")
print ("please enter the quantity to be converted:", number )
print (number, "pound force is equivilaent to ",pounds_in_newtons, "newtons") 
print (number, "meters is equivilaent to ", meters_in_feet, "feet")
print (number, "atmospheres is equivalent to", Atmospheres_to_kilopascals, "kilopascals")
print (number, "watts is equivalent to", watts_to_btu_per_hour, "BTU per hour")
print (number, "liters per second is equivalent to", form , "gallons per minute")
print (number, "degrees Celsius is equivalent to", formatted,  "degrees Fahrenheit")