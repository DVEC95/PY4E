# Exercise 2: 
#   Write a program to prompt for a file name, and then read through the file and look for lines of the form:
#   X-DSPAM-Confidence: 0.8475
#   When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart the line to extract the floating-point number on the line. 
#   Count these lines and then compute the total of the spam confidence values from these lines. 
#   When you reach the end of the file, print out the average spam confidence.

file_name = input('Please enter a file name: \n')

try:
    txt_file = open(file_name, 'r')

except:
    if file_name == 'na na boo boo':
        print('Grow up.')
    print('Please enter a valid file name.')
    exit()

num_array = []

for line in txt_file:
    if line.startswith('X-DSPAM-Confidence:'):
        num = line[line.find(':') + 2:line.find('\n')]
        num_array.append(float(num))

print('Average spam confidence:', sum(num_array) / len(num_array))