# Problem Statement
"""
Tom is working in a shop where he labels items. Each item is labelled with a number between num1 and num2(both inclusive). Since Tom is also a natural mathematician, he likes to observe patterns in numbers. Tom could observe that some of these label numbers are divisible by other label numbers.

Write a Python function to find out those label numbers that are divisible by another label number and display how many such label numbers are there totally.

Note:- Consider only the distinct label numbers. The list of those label numbers should be considered as a set.
"""
# Code:
def check_numbers(num1,num2):
    #start writing your code here
    l = [i for i in range(num1, num2+1)]
    num_list = []
    for i in l :
        for j in l[::-1]:
            if j > i  and j % i ==0 :
                num_list.append(j)
            else:
                pass
    
    return [set(num_list),len(set(num_list))]

num1=2
num2=20
print(check_numbers(num1, num2))



# Alernative Mathod

def check_numbers(num1,num2):
    #start writing your code here
    l = [i for i in range(num1, num2+1)]
    num_list = [j for i in l for j in l[::-1] if j > i and j % i == 0]
    return [set(num_list),len(set(num_list))]

num1=2
num2=20
print(check_numbers(num1, num2))
