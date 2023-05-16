# Python program to find the factorial of a number provided by the user.


# user enter the number for factorial
num = int(input("Enter a number for factorial : "))

fact = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Error : factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
    str_d = "factorial of "+str(num)+"  = "
    for i in range(num ,-1,-1):
        if i > 0:
            fact = fact * i
            if i==1:
                str_d=str_d+str(i)
            else:
                str_d = str_d + str(i) + " * "
    print(str_d+" =",fact)