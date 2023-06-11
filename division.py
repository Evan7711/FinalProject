"""
File for division function
"""

# Function that allows division
def Division():
    while True:
        try:
            base = input("What number would you like to divide from: ")
            quotient = input("What would you like to divide by: ")
            divide = int(base) / int(quotient)
            print(f"{base} divided by {quotient} equals {divide}")
            break
        except ZeroDivisionError:
            print("You can't divide by zero")
        except ValueError:
            print("Please input numbers only!")