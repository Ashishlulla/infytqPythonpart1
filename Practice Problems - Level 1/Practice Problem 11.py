# Problem Statement
"""
Write a python function which accepts a sentence and returns a list in which first value is the count of upper case letters 
and second value is the count of lower case letters in the sentence. Ignore spaces, numbers and other special characters if any.

Sample Input                                            Expected Output

Hello world!                                               [1,9]

Welcome to Mysore                                          [2,13]
"""

# Code

def find_upper_and_lower(sentence):
    #start writing your code here
    upper_count = 0
    lower_count = 0
    for i in sentence:
        if i.isalpha():
            if i.isupper():
                upper_count = upper_count + 1
            else:
                lower_count = lower_count + 1
        else:
            pass
       
    return [upper_count, lower_count]

sentence="Come Here"
print(find_upper_and_lower(sentence))
