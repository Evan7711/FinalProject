"""
file for my multiplication function
"""

# Function to allow multiplication
def Multiply():
    while True:
        try:  
            x = list(map(int, input("Enter all your values: ").split()))
            product = 1
            for value in x:
                product *= value
                print(f"The product is {product}")
            break
        except ValueError:
            print("Please input numbers only!")