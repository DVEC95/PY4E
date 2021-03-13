# Exercise 3: 
#   Write a program to prompt the user for hours and rate per hour to compute gross pay.

h = input('Enter Hours: ')
r = input('Enter Rate: £ ')

print('Pay: £', round(float(h) * float(r), 2))