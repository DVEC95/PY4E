# Exercise 3: 
#   Encapsulate this code in a function named count, and generalize it 
#   so that it accepts the string and the letter as arguments.

def count(word, letter):
    x = 0
    for character in word:
        if character == letter:
            x += 1
    print(x)
