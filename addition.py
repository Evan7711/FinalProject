"""
This file contains the function for addition
"""


# Function for adding any number of inputs
def Addition():
    while True:
        try:
            x = list(map(int, input("Enter all the values you'd like to add: ").split()))
            total = sum(x)
            print(f"The sum is {total}")
            break
        except ValueError:
            print("Please input numbers only!")