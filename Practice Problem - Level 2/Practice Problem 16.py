# Problem Statement
"""
Write a Python function to rotate the list of elements by N positions. The function should return the rotated list.

Sample Input                                            Expected Output

Input list: [1, 2, 3, 4, 5, 6]
Number of positions to be rotated = 2                [5, 6, 1, 2, 3, 4]

Input list: [1, 2, 3, 4, 5, 6]
Number of positions to be rotated = 4                 [3,4,5, 6, 1, 2]

Note : Assume that number of positions to be rotated is always a value >= 0 and <= length of the input list. 
"""
# Code:
def rotate_list(input_list,n):
    #start writing your code here
     return input_list[-(n):] + input_list[:-(n)]


input_list= [1,2,3,4,5,6]
output_list=rotate_list(input_list,4)
print(output_list)
