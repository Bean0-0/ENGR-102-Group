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
# YOUR CODE HERE
#

t0 = float(input("Enter time 1: "))

x0 = float(input("Enter the x position of the object at time 1: "))
y0 = float(input("Enter the y position of the object at time 1: "))
z0 = float(input("Enter the z position of the object at time 1: "))


t1 = float(input("Enter time 2: "))

x1 = float(input("Enter the x position of the object at time 2: "))
y1 = float(input("Enter the y position of the object at time 2: "))
z1 = float(input("Enter the z position of the object at time 2: "))

def posStr(t, point_num):
    '''
    #At time 12 seconds, observed position was (8, 6, 7) meters
    #At time 85 seconds, observed position was (-5, 30, 9) meters
    x0, y0, z0 = 8.0, 6.0, 7.0
     
    x1, y1, z1 = -5.0, 30.0, 9.0
    '''
    
    #p(t) = p0 + (p1-p0) * (t-t0)/dt
    dt = t1 - t0
    
    x = x0 + (x1 - x0) / dt * (t - t0)
    y = y0 + (y1 - y0) / dt * (t - t0) 
    z = z0 + (z1 - z0) / dt * (t - t0)

    m = f"At time {t:.2f} seconds the object is at  ({x:.3f}, {y:.3f}, {z:.3f})"

    return m



# Display the results from interpolating at 5 points, evenly spaced from the beginning time to the ending time, inclusive.
# Interpolate, starting at time 30 seconds and ending at time 60 seconds, printing the result each time. The line of dashes will separate each computation.

for i in range(5):
    t = t0 + i * (t1 - t0) / 4 # initial +4
    print(posStr(t, i + 1))