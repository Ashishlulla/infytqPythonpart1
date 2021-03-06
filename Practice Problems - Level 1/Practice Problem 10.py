# Problem Statement
"""
Write a Python function which accepts a string and returns a string made of the first 2 and the last 2 characters of the given string.

If the string length is less than 2, return -1.

Note: If the string length is equal to 2, consider the 2 characters to be the first as well as the last two characters.

Sample Input                           Expected Output

w3resource                                  w3ce

w3                                          w3w3

A                                             -1

"""
# Code

def string_both_ends(input_string):
    # start writing your code here
    if len(input_string) > 2:
        return input_string[:2] + input_string[-2:]
    elif len(input_string) == 2:
        return input_string * 2
    else:
        return -1


input_string = "w3w"
print(string_both_ends(input_string))
