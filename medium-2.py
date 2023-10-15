import math

radius = input("Enter the radius of the circle: ")

try:
    radius = float(radius)
except ValueError:
    print("Please enter a valid value.")
    exit()

if radius < 0:
    print("The radius must be a non-negative number.")
    exit()

print(f"The radius is: {math.pi * radius**2}")