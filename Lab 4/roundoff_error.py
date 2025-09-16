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
# Date: 9/16/2025
#
#
#
############ Part A ############
a = 1 / 7
print(f'a = {a}')
b = a * 7
print(f'b = a * 7 = {b}')
# The value of b should be 1.0. Here it actually prints 1.0, so roundoff
# error is not visible in this case.

c = 2 * a
d = 5 * a
f = c + d
print(f'f = 2 * a + 5 * a = {f}')
# The value of f should also be 1.0, but it may show a tiny roundoff error.

from math import sqrt
x = sqrt(1 / 3)
print(f'x = {x}')
y = x * x * 3
print(f'y = x * x * 3 = {y}')
z = x * 3 * x
print(f'z = x * 3 * x = {z}')
# The values of y and z should both be 1.0.
# y is usually slightly less than 1 due to roundoff,
# while z may equal 1.0 exactly (depending on how calculations happen).

############ Part B ############
TOL = 1e-10

# check if b and f are equal within tolerance
if abs(b - f) < TOL:
    print(f'b and f are equal within tolerance of {TOL}')
else:
    print(f'b and f are NOT equal within tolerance of {TOL}')

# check if y and z are equal within tolerance
if abs(y - z) < TOL:
    print(f'y and z are equal within tolerance of {TOL}')
else:
    print(f'y and z are NOT equal within tolerance of {TOL}')

############ Part C ############
m = 0.1
print(f'm = {m}')
n = 3 * m
print(f'n = 3 * m = 0.3 {n == 0.3}')   # False because 0.1 isn’t exact in binary
p = 7 * m
print(f'p = 7 * m = 0.7 {p == 0.7}')   # May also be False
q = n + p
print(f'q = n + p = 1 {q == 1}')       # Likely False
# These results show that even when numbers print neatly, they are stored
# as approximations in binary, leading to surprises in equality checks.
