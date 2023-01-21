"""
Write a python function to calculate average of three numbers (TSRS)
"""

# defining a average function to calculate average of three numbers
# which takes 3 numbers as an arguments and returns the average
def average(num1, num2, num3):
    return (num1+num2+num3)/3    # returns the average

# taking input from the user
num1, num2, num3 = int(input("Enter three numbers : ")), int(input()), int(input())

# printing average of the three numbers
print("Average is %.2f" %(average(num1, num2, num3)))