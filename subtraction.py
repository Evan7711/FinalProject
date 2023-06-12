"""
File for subtraction function
"""

# Function that allows subtraction
def Subtraction():
    while True:
        try:
            base = input("What number would you like to subtract from: ")
            minus = input("How much would you like to subtract from it: ")
            difference = int(base) - int(minus)
            print(f"The difference between {base} and {minus} is {difference}")
            break
        except ValueError:
            print("Please input numbers only!")
    