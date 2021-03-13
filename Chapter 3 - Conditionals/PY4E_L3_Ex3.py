# Exercise 3: 
# Write a program to prompt for a score between 0.0 and 1.0. 
# If the score is out of range, print an error message. 
# If the score is between 0.0 and 1.0, print a grade using the following table:

#   Score   Grade
# >= 0.9     A
# >= 0.8     B
# >= 0.7     C
# >= 0.6     D
#  < 0.6     F

score = input("Please enter your score. \n")

try:
    float(score)
except:
    print("Bad score.")
    quit()

try:
    if float(score) <= 1.0 and float(score) >= 0.0:
        score = float(score)
except:
    print("Bad score.")
    quit()

try:
    if score >= 0.9:
        grade = "A"
    elif score >= 0.8:
        grade = "B"
    elif score >= 0.7:
        grade = "C"
    elif score >= 0.6:
        grade = "D"
    else:
        grade = "F"

    print(grade)
except:
    print("Bad score.")