# Program 8 , Program to read first n lines of file
import os

# reading the file
# List all available files
print("All files List")
dir_list = os.listdir(os.path.join('Files'))
print(dir_list)
nm_file=input("Enter the name of file to be read : ")
r_file=open(os.path.join('Files',nm_file),'r')
read_linesFile=r_file.readlines()
lines = len(read_linesFile)
print('Total Number of lines in file:', lines)
n_line=int(input("How many line you want to read: "))
chk_count=1
for i in read_linesFile:
    print(i.strip())
    if chk_count == n_line:
        break
    chk_count=chk_count+1





