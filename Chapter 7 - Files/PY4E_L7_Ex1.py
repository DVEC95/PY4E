# Exercise 1: 
#   Write a program to read through a file and print the contents of the file (line by line) all in upper case.

file_name = input('Please enter a file name: \n')

try:
    txt_file = open(file_name, 'r')

except:
    print('Please enter a valid file name.')
    exit()

for line in txt_file:
    print(line.rstrip().upper())

txt_file.close()