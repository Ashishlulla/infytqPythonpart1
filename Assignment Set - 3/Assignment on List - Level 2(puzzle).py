Problem Statement
"""
Write a python function, create_largest_number(), which accepts a list of numbers and returns the largest number possible by concatenating the list of numbers. 
Note: Assume that all the numbers are two digit numbers.

Sample Input       Expected Output

23,34,55               553423
"""

# Code
def create_largest_number(number_list):
    a = sorted(number_list, reverse= True)
    string = ""
    for i in a:
        string = string+str(i)
    
    return int(string)
        

number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)
