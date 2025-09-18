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
from sympy import symbols

A = int(input("Please enter the coefficient A: "))
B = int(input("Please enter the coefficient B: "))
C = int(input("Please enter the coefficient C: "))

x = symbols('x')

# Create the quadratic expression using SymPy
equation = A*x**2 + B*x + C
# Format the equation string
equation_str = str(equation).replace('**', '^').replace('*', '')

# Add space
equation_str = equation_str.replace('-x', '- x')

# Handle cases like -2x^2, -3x, etc.
import re
equation_str = re.sub(r'-(\d)', r'- \1', equation_str)

print(f"The quadratic equation is {equation_str} = 0")