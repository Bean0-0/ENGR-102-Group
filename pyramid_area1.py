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
# Date: 9/30/2025
#

cube_length = float(input("Enter the side length in meters: "))
layers = int(input("Enter the number of layers: "))

top_area = 0
for i in range(layers, 0, -1):  # from bottom layer to top layer
    layer_cubes = i * i  # total cubes in this layer (i × i)
    if i > 1:
        covered_cubes = (i - 1) * (i - 1)  # cubes covered by layer above
    else:
        covered_cubes = 0  # top layer has nothing covering it
    exposed_cubes = layer_cubes - covered_cubes
    top_area += exposed_cubes * (cube_length ** 2)

side_area = 0
for i in range(1, layers + 1): # from top layer to bottom layer
    cubes_per_side_per_layer = i
    side_area += 4 * cubes_per_side_per_layer * (cube_length ** 2)

total_surface_area = top_area + side_area

print(f"You need {total_surface_area:.2f} m^2 of gold foil to cover the pyramid")

