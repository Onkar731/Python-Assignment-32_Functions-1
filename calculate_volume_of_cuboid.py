"""
Write a python function to calculate volume of a cuboid (TSRS)
"""

# defining a function to calculate volume of a cuboid "cuboid_volume()"
# which takes length, width and height of the cuboid and returns voiume
def cuboid_volume(length, width, height):
    return length*width*height    # formula of cuboid volume - base*height

# taking input from the user
length, width, height = float(input("Enter lenght, width and height of the cuboid : ")), float(input()), float(input())

# printing volume of the cuboid
print("Volume of the cuboid is %.2f cubic cm" %(cuboid_volume(length, width, height)))