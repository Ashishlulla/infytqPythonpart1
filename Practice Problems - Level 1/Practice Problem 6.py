# Problem Statment
"""
Write a python function which accepts a list of numbers and returns true, if 1, 2, 3 appears in sequence in the list.

Otherwise, it should return false.

Sample Input                         Expected Output

[1, 1, 2, 3, 1]                         True

[1, 1, 2, 4, 3]                         False

"""
# Code

def list123(nums):
    #start writing your code here
    string = ""
    for i in nums:
        string = string + str(i)
    if '123' in string:
        return True
    else:
        return False

    

nums=[1,2,3,4,5]
print(list123(nums))
