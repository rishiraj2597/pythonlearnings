

divisble_number=int(input("Enter the number by which divisble needs to be done between 1 to 100: "))
list_display=[]
for i in range(1,101):
    if i % divisble_number == 0:
        list_display.append(i)

print("List of Numbers which are divisble by "+str(divisble_number))
print(list_display)
