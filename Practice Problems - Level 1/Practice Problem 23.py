# Problem Statement
"""
Write a python function to find out whether a number is divisible by the sum of its digits. If so return True,else return False.

Sample Input                       Expected Output

42                                    True

66                                   False
"""
#Code:

def divisible_by_sum(number):
    #start writing your code here
    add = 0
    for i in str(number):
        add = add + int(i)
    if number % add == 0:
        return True
    else:
        return False

    
number=42
print(divisible_by_sum(number))
