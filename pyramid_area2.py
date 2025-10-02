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
#

# Get user input
cube_length = float(input("Enter the side length in meters: "))
layers = int(input("Enter the number of layers: "))

# The top area is simply the area of the bottom layer
top_area = layers * layers * (cube_length ** 2)

# Each side area = (1 + 2 + 3 + ... + n) × cube_length^2
# Total for one side = n(n+1)/2 × cube_length^2
# Total for all 4 sides = 4 × n(n+1)/2 × cube_length^2 = 2n(n+1) × cube_length^2
side_area = 2 * layers * (layers + 1) * (cube_length ** 2)

total_surface_area = top_area + side_area

print(f"You need {total_surface_area:.2f} m^2 of gold foil to cover the pyramid")

