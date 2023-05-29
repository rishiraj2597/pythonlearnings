# Program to check file
import os

# create file
nm_file=input("Enter the name of file to be created: ")

#Below code will create an empty file in the "Files" folder
create_file=open(os.path.join('Files',nm_file),'x')

# Add content to file
content_file=input("Enter the contents needs to be written:")
create_file.write(content_file)

# Closing the file after write
create_file.close()

# reading the file
# Again we have to open the file first for reading

print("Reading content of  file")
create_file=open(os.path.join('Files',nm_file),'r')
print(create_file.read())
