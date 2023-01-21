"""
Write a python fucntion to calculate compound interest (TSRS)
"""

# defining a function "compound_interest()" which takes 
# principle amount, rate of interest and time as an arguments
# and returns the compound interest
def compound_interest(principle_amt, roi, time):
    return principle_amt * ((1+roi/100)**time) - principle_amt # returning compound interest

# taking input from the user
principle_amt, roi, time = float(input("Enter principle amount, rate of interest and time : ")), float(input()), int(input())

# printing compound interest
print("Compound Interest %.2f" %(compound_interest(principle_amt, roi, time)))