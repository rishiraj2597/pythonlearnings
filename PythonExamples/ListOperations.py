
List1 =[1,2,3,4,5]
List2=[51,52,53,54,55]

print("original List1 is :",List1)
print("original List2 is :",List2)

# Output
# original List1 is : [1, 2, 3, 4, 5]
# original List2 is : [51, 52, 53, 54, 55]

#  append() method

List1.append(6)
List1.append(7)
List1.append(8)

print("List1 after append is :",List1)

# Output
# List1 after append is : [1, 2, 3, 4, 5, 6, 7, 8]

# extend() , use to add more than 1 element at one go
List1.extend([9,10,11,12])

print("List1 after extend is :",List1)

# Output
# List1 after extend is : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# insert() method ,
## It insert a given element at the desired poistion , it only add one element at a time

List1.insert(5,13)  # Insert number 13 at index position 5 i.e. after 5 elements in list

print("List1 after insert is :",List1)

# Output
# List1 after insert is : [1, 2, 3, 4, 5, 13, 6, 7, 8, 9, 10, 11, 12]

# remove() method, removes an element from the list.
List1.remove(13)
print("List1 after remove is :",List1)

# Output
# List1 after remove is : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# pop() , remove an element from any position in the list.
List1.pop()  # removes last element of the list
print("List1 after pop is :",List1)

# Output
# List1 after pop is : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


List1.pop(3)  # removes element from the list at 4 th position
print("List1 after pop with index position 3 is :",List1)

# Output
# List1 after pop with index position 3 is : [1, 2, 3, 5, 6, 7, 8, 9, 10, 11]


# slice is used to print a section of the list.
# It is denoted by List[index_start_position : index_end_position ]
# The slice operation returns a specific range of elements. It does not modify the original list.

print(List1[:5]) # prints element of list till index position 5
# Output
# [1, 2, 3, 5, 6]

print(List1[5:8]) # prints element of list from  index position 5 to 7
# Output
# [7, 8, 9]

print(List1[6:3]) # prints nothing , as start position of index (6)  is greater than end position (3)
# Output
# [] // empty list

# reverse()
print(List1[::-1])  # does not modify the original list
# Output
# [11, 10, 9, 8, 7, 6, 5, 3, 2, 1]

List1.reverse()     # modifies the original list
print(List1)
# Output
# [11, 10, 9, 8, 7, 6, 5, 3, 2, 1]

# len() : Gives the the length of list i.e. total number of elements in list
print(len(List1))

# Output
# 10

# min and max
# min : gives the minimum value in list
# max : gives the maximum value in list

print(min(List1))
# Output
# 1

print(max(List1))
# Output
# 10

# count
# count the number of given element in list
print(List1.count(3))  # count occurence of 3 in list
# Output
# 1

# concat ; It add two lists , denoted by '+'
print(List1 + List2) # add two lists

# Output
# [11, 10, 9, 8, 7, 6, 5, 3, 2, 1, 51, 52, 53, 54, 55]


# multiply
print(List1 * 3) # repeat the elements in list by the time , here 3 is defined

# Output
# [11, 10, 9, 8, 7, 6, 5, 3, 2, 1, 11, 10, 9, 8, 7, 6, 5, 3, 2, 1, 11, 10, 9, 8, 7, 6, 5, 3, 2, 1]


# index
print(List1.index(3))            # print  position of element passed in the  list
# Output : 7 , as we have reversed the list above using "reverse" function , which has modified oriinal list

# print(List1.index(6, 0, 2))     # searches from 0th to 2nd position ,
# Above gives error as "ValueError: 6 is not in list" , as 6 number is not between 0 to 2nd position


# sort
List1.sort() # sort the list in ascending order
print(List1)
# Output
# [1, 2, 3, 5, 6, 7, 8, 9, 10, 11]


# clear
List1.clear()  # clears the list or make list empty
print(List1)

# Output
# [] // empty list

# copy
List3=List2.copy()  # copy elements of List2 in List3
print("List3",List3)

# Output
# List3 [51, 52, 53, 54, 55]

List3.append(56) # Add "56" to List 3
print("List3",List3)

# Output
# List3 [51, 52, 53, 54, 55, 56]

# Print element of List
for l in List3:  # Using for loop to iterate over each element of List3
    print(l)     # Print item of the list as iteration goes

# Output
# 51
# 52
# 53
# 54
# 55
# 56

