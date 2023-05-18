# Function using the reverse and compare method
def isPalindrome1(string):
    print("Checking with reverse and comparision")
    if (string == string[::-1]):
        return "The input string is a palindrome."
    else:
        return "The input string is not a palindrome"

# Function using the loop method
def isPalindrome2(string):
    print("Checking with loop method")
    for i in range(0, int(len(string) / 2)):
        if string[i] != string[len(string) - i - 1]:
            return "The input string is not a palindrome"
    return "The input string is  a palindrome"


# Enter input string
string=input("Enter string which needs to check for palindrome: ")

print(isPalindrome1(string))
print("================================================")
print(isPalindrome2(string))