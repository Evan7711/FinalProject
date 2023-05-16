number = input("What function would you like to use: ").lower()

if number == "addition":
    x = input("What's the first number you'd like to add: ")
    y = input("What's the second number you'd like to add: ")
    additional = input("Would you like to add more numbers: ").lower()
    if additional == "no":
        add = int(x) + int(y)
        print(f"The sum of {x}, and {y} is {add}")
    elif additional == "yes":
        