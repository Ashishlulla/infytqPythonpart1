# Problem Statement
"""
Given a string, write a python function to return True if the strings "mat" and "jet" appear the same number of times in the given string, else return False.

Note: Perform case insensitive string comparison wherever necessary.

Sample Input                                                  Expected Output

Jet on the Mat but mat is too long                                False

mat jet Jet Mat                                                    True
"""

# Code:
def check_occurence(string):
    #start writing your code here
    jet_count = 0
    mat_count = 0
    for i in string.lower().split(" "):
        if i == "jet":
            jet_count = jet_count + 1
        elif i == 'mat':
            mat_count = mat_count + 1
        else:
           pass
    if jet_count == mat_count:
        return True
    else:
        return False

string="Jet on the Mat but mat is too long"
print(check_occurence(string))
