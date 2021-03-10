# Exercise 1: 
#   Write a while loop that starts at the last character in the string 
#   and works its way backwards to the first character in the string, 
#   printing each letter on a separate line, except backwards.

def reversal(text):
    length = len(text)
    while 0 < length:
        letter = text[length - 1]
        print(letter)
        length -= 1