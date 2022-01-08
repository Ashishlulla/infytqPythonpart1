# Problem Statement
"""
Write a python program that accepts a text and displays a string which contains the word with the largest frequency in the text and the frequency itself separated by a space.

Rules:

The word should have the largest frequency.

In case multiple words have the same frequency, then choose the word that has the maximum length.

Assumptions:

The text has no special characters other than space.

The text would begin with a word and there will be only a single space between the words.

Perform case insensitive string comparisons wherever necessary.

Sample Input                                                                                                                  Expected Output

"Work like you do not need money love like you have never been hurt and dance like no one is watching"                            like 3

"Courage is not the absence of fear but rather the judgement that something else is more important than fear"                     fear 2

"""

# Code:
def max_frequency_word_counter(data):
    word=""
    frequency=0


    b_set = set()
    dict1 = {}
    for i in data.split():
        count = data.count(i)
        dict1[i] = count

    b = max(set(dict1.values()))

    for i in dict1.keys():
        if dict1[i] == b:
            b_set.add(i)

    print(max(b_set, key=len), dict1[max(b_set,)])


#Provide different values for data and test your program.
data= "Work like you do not need money, love like you have never been hurt, and dance like no one is watching"
max_frequency_word_counter(data)
