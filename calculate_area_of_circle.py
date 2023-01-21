"""
Write a python function to calculate area of a circle (TSRS)
"""

# defining a "area()" function to calculate the area of a circle
# which takes 'radius' as an argument and returns the area of the circle
def area(radius):
    return 2*3.14*radius**2    # formula - 2*PI*r*r

# taking input from the user
radius = float(input("Enter radius of the circle : "))

# printing area of a circle
print("Area of the circle is : %.2f" %(area(radius)))