"""
Write a python function to calculate sum of two numbers. (TSRS)
"""

# we can define a function in python using "def" keyword
# defining a function "sun()" which takes two parameters and returns the sum
def sum(num1, num2):
    return num1 + num2

# taking input from the user
num1, num2 = int(input("Enter two numbers :")), int(input())

# printing sum of two numbers
print("Sum is", sum(num1, num2))