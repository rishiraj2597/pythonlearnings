from datetime import datetime,date

# https://docs.python.org/3/library/datetime.html
dt_dob=input('Enter your date of birth in DD-MM-YYYY format:')
d1_dob=datetime.strptime(dt_dob, '%d-%m-%Y')
today = date.today()
age = today.year - d1_dob.year - ((today.month, today.day) < (d1_dob.month, d1_dob.day))

print("Based on your date of birth ")
print("The Day you were born was :"+d1_dob.strftime("%A"))
print("The Day number of the year was  :"+d1_dob.strftime("%j"))
print("The Week number of the year was  :"+d1_dob.strftime("%U"))
print("The Weekday number of the week was  :"+d1_dob.strftime("%u"))
print("Your Age as of Today is "+str(age)+" years")

