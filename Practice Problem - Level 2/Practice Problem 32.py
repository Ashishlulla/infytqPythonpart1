# Problem Statement
"""
Given an integer n, write a python function to return true, if it is possible to represent it as a sum of the squares of two different integers, else return false.
"""
# code

def check_squares(number):
    #start writing your code here
    square = []
    for i in range(len(square)):
        for j in range(i+1, len(square)):
            if square[i] + square[j] == number:
                return True
            else:
                pass
    return False


number=68
print(check_squares(number))
