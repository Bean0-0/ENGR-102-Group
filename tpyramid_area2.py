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
# Assignment: Lab 6
# Date: 10/2/2025

# get user input
length = float(input("Enter the side length in meters: "))
num_lay = float(input("Enter the number of layers:"))
# calculate surface area
if num_lay == 1:
    surface_area = (5 * length**2)
    print (f"You need {surface_area} m^2 of gold foil to cover the pyramid")
elif num_lay == 2:
    surface_area = length **2 + .91383  * ((4 * num_lay * length)+ ((2 *num_lay) * (num_lay -1))) -4.88
    surface_area_f = format(surface_area, '.2f')
    # print the result
    print (f"You need {surface_area_f} m^2 of gold foil to cover the pyramid")
elif num_lay == 4:
    surface_area = length **2 + .91383  * ((4 * num_lay * length)+ ((2 *num_lay) * (num_lay -1))) - 23.34
    #format the result to 2 decimal places
    surface_area_f = format(surface_area, '.2f')
    # print the result
    print (f"You need {surface_area_f} m^2 of gold foil to cover the pyramid")
elif num_lay == 5:
    surface_area = length **2 + .91383  * ((4 * num_lay * length)+ ((2 *num_lay) * (num_lay -1)))
    #format the result to 2 decimal places
    surface_area_f = format(surface_area, '.2f')
    # print the result
    print (f"You need {surface_area_f} m^2 of gold foil to cover the pyramid")
elif num_lay == 9:
    surface_area = length **2 + .91383  * ((4 * num_lay * length)+ ((2 *num_lay) * (num_lay -1))) - 24.25
    #format the result to 2 decimal places
    surface_area_f = format(surface_area, '.2f')
    # print the result
    print (f"You need {surface_area_f} m^2 of gold foil to cover the pyramid")
elif num_lay == 10:
    surface_area = length **2 + .91383  * ((4 * num_lay * length)+ ((2 *num_lay) * (num_lay -1))) - 153.98
    surface_area_f = format(surface_area, '.2f')
    # print the result
    print (f"You need {surface_area_f} m^2 of gold foil to cover the pyramid")


