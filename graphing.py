"""
This is my file for graphing
"""

#importing libraries
import matplotlib.pyplot as plt
import numpy as np

# Sets numpy to 3 significant figures
np.set_printoptions(precision=3)
# This is my graphing function
def Graphing():
    print("""
    IMPORTANT:
      Type quit at any point to exit graphing mode
      In order to use powers you must put two **
      If using Trig function please input np. in front
      Use lowercase only for variables
      When multiplying you must use * symbol, ex:) 3*x
      When done with graph hit X in top right corner to close
    """)
    # sets basic values for variables
    eq1, eq2, r1, r2 = "", "", 0, 0
    # creates loop for graphing
    while eq1 != "quit":
        try:
            print("Enter first equation: ")
            eq1 = input()
            if eq1 == "quit":
                print("Exiting graphing mode")
                break
            print("Enter second equation: ")
            eq2 = input()
            if eq2 == "quit":
                print("Exiting graphing mode")
                break
            print("Enter the minimum of your range:")
            r1 = input()
            if r1 == "quit":
                print("Exiting graphing mode")
                break
            else:
                r1 = int(r1)
            print("Enter the maximum of your range:")
            r2 = input()
            if r2 == "quit":
                print("Exiting graphing mode")
                break
            else:
                r2 = int(r2)
            x = np.array(range(int(r1), int(r2)))
            y1 = eval(bytes([ord(p) for p in eq1]))
            y2 = eval(bytes([ord(p) for p in eq2]))
            y3 = np.where(y1 == 0)
            Xintercept = x[y3]
            print(f"Graph 1 has x intercepts at x = {Xintercept}")
            y4 = np.where(y2 == 0)
            Xintercept2 = x[y4]
            print(f"Graph 2 has x intercepts at x = {Xintercept2}")
            plt.plot(x, y1)
            plt.plot(x, y2)
            plt.show()
            break
        except:
            print("Invalid input")