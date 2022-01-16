# Problem Statement
"""
Write a python function which accepts a list of numbers and returns true if the list contains a 2 next to a 2. Otherwise it should return false.

Sample Input                                           Expected Output

[ 1,2,1,2,3,4,5,2,2]                                       True

[3,2,5,1,2,1,2]                                           False
"""
# Code
def check_22(num_list):
    #start writing your code here
    string = ""
    for i in num_list:
        string = string + str(i)
    if '22' in string:
        return True
    else:
        return False
        
print(check_22([3,2,5,1,2,1,2,2]))
