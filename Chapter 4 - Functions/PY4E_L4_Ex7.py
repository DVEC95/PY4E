# Exercise 7: 
# Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string.

def computegrade(score):
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

user_score = input("Please enter your score. \n")

try:
    float(user_score)
except:
    print("Score not recognised.")
    quit()

try:
    if float(user_score) <= 1.0 and float(user_score) >= 0.0:
        user_score = float(user_score)
except:
    print("Score not recognised.")
    quit()

try:
    computegrade(user_score)
except:
    print("Score not recognised.")