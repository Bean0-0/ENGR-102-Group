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

import math

x = float(input("Enter a value for x: "))
while x <= 0 or x > 2:
    x = float(input("Out of range! Try again: "))

tolerance = float(input("Enter the tolerance: "))

taylor_series = 0
n = 1
term = (x - 1)  # First term: (x-1)^1 / 1
while abs(term) >= tolerance:
    taylor_series += term
    n += 1
    term = ((-1) ** (n - 1)) * ((x - 1) ** n) / n  # Calculate the next term
    


print(f"ln({x}) is approximately {float(taylor_series)}")
print(f"ln({x}) is exactly {math.log(x)}")
print(f"The difference is {abs(taylor_series - math.log(x))}")