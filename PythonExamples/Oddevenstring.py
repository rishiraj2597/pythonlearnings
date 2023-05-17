input_string=input("Enter a string: ")
even_chars_str = {}
odd_chars_str = {}

for i in range(len(input_string)):
    if i % 2 == 0:
        even_chars_str.update({i:input_string[i]})
    else:
        odd_chars_str.update({i:input_string[i]})

print(f'Odd characters in input string with index position: {odd_chars_str}')
print(f'Even characters in input string with index position : {even_chars_str}')