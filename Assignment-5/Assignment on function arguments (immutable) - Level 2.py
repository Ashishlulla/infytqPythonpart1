# Problem Statement
"""
Write a python function, check_double(number) which accepts a whole number and returns True if it satisfies the given conditions.

The number and its double should have exactly the same number of digits.

Both the numbers should have the same digits ,but in different order.

Otherwise it should return False.

Example: If the number is 125874 and its double, 251748, contain exactly the same digits, but in a different order.
"""

# Code

def check_double(number):
    #Remove pass and write your logic here
    b = number * 2
    a_sort = sorted(str(number))
    b_sort = sorted(str(b))
    if a_sort == b_sort:
        return True
    else:
        return False

#Provide different values for number and test your program
print(check_double(125874))
