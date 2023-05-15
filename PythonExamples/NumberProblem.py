import math
import sys


def add(var1,var2):
    return var1 + var2

def sub(var1,var2):
    return var1 - var2

def multiply(var1,var2):
    return var1 * var2

def division(var1,var2):
    return var1 / var2

def log10(var):
    return math.log10(var)


def mathActions():
    
    var1=int(sys.argv[1])
    var2=int(sys.argv[2])

    # Converting return types to string for display
    print("Addition of Two numbers is "+ str(add(var1,var2)))
    print("Difference of Two numbers is " + str(sub(var1,var2)))
    print("Multiplication of Two numbers is " + str(multiply(var1,var2)))
    print("Division of Two numbers is " + str(division(var1,var2)))
    print("Log of first  number "+str(var1)+" is " + str(log10(var1)))
    print("Log of second  number "+str(var2)+" is " + str(log10(var2)))

mathActions()




