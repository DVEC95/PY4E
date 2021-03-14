# Exercise 1: 
# Write a program which repeatedly reads numbers until the user enters “done”. 
# Once “done” is entered, print out the total, count, and average of the numbers. 
# If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.

numbers = []

while True:
    user_input = input('Enter a number: \n')
    try:
        if user_input != 'done':
            numbers.append(int(user_input))
    except:
        print('Please enter a numeric value or type "done" to exit.')
    if user_input == 'done':
        break

print('Numbers entered:', len(numbers))
print('Sum of numbers:', sum(numbers))

if len(numbers) > 0:
    print('Average:', sum(numbers) / len(numbers))
else:
    print('Average not available.')