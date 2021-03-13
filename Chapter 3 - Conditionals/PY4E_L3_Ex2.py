# Exercise 2: 
# Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program.

hours = input("Enter Hours: ")

try:
    float(hours)
except:
    print('Error: Please enter a numeric value.')
    quit()

rate = input("Enter Rate: £ ")

try:
    float(rate)
except:
    print('Error: Please enter a numeric value.')
    quit()

total = float(hours) * float(rate)

if float(hours) >= 40:
    bonus_hours = float(hours) - 40
    bonus = (float(rate) * bonus_hours) * 0.5
    total += bonus

print('Total: £', round(total, 2))