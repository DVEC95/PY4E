# Exercise 6: 
# Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).

def computepay(h, r):   
    total = float(h) * float(r)

    if float(h) >= 40:
        bonus_hours = float(h) - 40
        bonus = (float(r) * bonus_hours) * 0.5
        total += bonus

    return round(total, 2)


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

print('Total: £', str(computepay(hours, rate)))