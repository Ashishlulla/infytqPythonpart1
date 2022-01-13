# Problem Statement
"""
Write a python function which accepts a sentence and finds the number of letters and digits in the sentence.

It should return a list in which the first value should be letter count and second value should be digit count. Ignore the spaces or any other special character in the sentence.

Sample Input                     Expected Output

Infosys 123                         [7,3]

ABCEFG                              [6,0]
"""

# Code
def count_digits_letters(sentence):
    #start writing your code here
    char_count = 0
    digit_count = 0
    for i in sentence:
        if i.isalpha() and i != " ":
            char_count = char_count + 1
        elif i.isdigit() and i != " ":
            digit_count = digit_count + 1
        else:
            pass

    
    return [char_count, digit_count]

sentence="Infosys Mysore 570027"
print(count_digits_letters(sentence))
