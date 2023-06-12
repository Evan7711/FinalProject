#------------------------------------------------------------------------------
# Title: Graphing Calculator
# Assignment: Final Project
# Date: 16/05/23
# Student: Evan Smart
# Version: 1.0
#------------------------------------------------------------------------------
"""
This is the main code for the use of the different calculator functions
"""

# Importing external files for each operation
import addition
import multiplication
import subtraction
import division
import graphing

# prints a message stating what kind of functions the calculator has
print(""" This graphing calculator can run addition, subtraction, multiplication, division, and graphing!
The calculator does not compute decimals, so please stick to whole numbers.
""")

# main code for when user chooses a function
while True:
    operation = input("What function would you like to use: ").lower()
    if operation == "addition":
        print("""
        To use addition:
        Enter the numbers you'd like to add with a space between each
        """)
        addition.Addition()
    elif operation == "multiplication":
        print("""
        To use multiplication:
        Enter the numbers you'd like to multiply with a space between each
        """)
        multiplication.Multiply()
    elif operation == "subtraction":
        subtraction.Subtraction()
    elif operation == "division":
        division.Division()
    elif operation == "graphing":
        graphing.Graphing()
    elif operation == "quit":
        print("Closing calculator")
        break
    else:
        print(f"Invalid Option: {operation}")
