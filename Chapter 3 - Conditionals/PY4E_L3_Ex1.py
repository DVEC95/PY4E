# Exercise 1: 
#   Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

hours = input("Enter Hours: ")

rate = input("Enter Rate: £ ")

total = float(hours) * float(rate)

if float(hours) >= 40:
    bonus_hours = float(hours) - 40
    bonus = (float(rate) * bonus_hours) * 0.5
    total += bonus

print('Total: £', round(total, 2))