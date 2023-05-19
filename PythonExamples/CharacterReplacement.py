

# Enter input string
a_string=input("Enter string for character removal: ")
n_remove=int(input("Enter number of characters to remove , integer values only : "))
reduced_string = a_string[n_remove:]

print("Reduced  String is : "+ reduced_string)

b_string=input("Enter string for character replacement: ")
n_replace=int(input("Enter number of characters to replace from first position , integer values only : "))
c_char=input("Enter character which should be placed in the position: ")

strValue = c_char*n_replace + b_string[n_replace:]

print("New String is : "+ strValue)

