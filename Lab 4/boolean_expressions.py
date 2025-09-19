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

############ Part A ############
#inputs for boolean expressions
def b_bool(user_input):
    return user_input.strip().upper() in ["T", "TRUE"]

a = b_bool(input("Enter True or False for a: ").strip().upper())
b = b_bool(input("Enter True or False for b: ").strip().upper())
c = b_bool(input("Enter True or False for c: ").strip().upper())


############ Part B ############
# odd number of trues?

print("a and b and c:", a and b and c)
print("a or b or c:", a or b or c)
XOR = (a and not b) or (not a and b)
print ("XOR:", XOR)
############ Part C ############
Odd= ((a and not b and not c) or
    (not a and b and not c) or
    (not a and not b and c) or
    (a and b and c))
print("Odd number:", Odd)
############ Part D ############

c1=(not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b)
c2= (not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (not a or(a and b and c) or (a and ((b and not c) or (not b))))
s1= (not b) or (not a and b and not c)
s2=(not b and c) or a
print("Complex 1:",c1)
print("Complex 2:",c2)
print("Simple 1:",s1)
print("Simple 2:",s2)
