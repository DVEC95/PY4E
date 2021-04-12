# Exercise 1: 
#   Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None. 
#   Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

nums = [1, 2, 3, 4, 5]

def chop(t):
    t.pop(0)
    t.pop(len(t) - 1)

def middle(t):
    return t[0:len(t)]

print(chop(nums))

print(middle(nums))
