# Exercise 2: Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the average.

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

print('Highest number entered:', max(numbers))
print('Lowest number entered:', min(numbers))