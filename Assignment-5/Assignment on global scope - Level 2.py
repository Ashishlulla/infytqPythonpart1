# Problem Statement

"""
A teacher is in the process of generating few reports based on the marks scored by the students of her class in a project based assessment.
Assume that the marks of her 10 students are available in a tuple. The marks are out of 25.

Write a python program to implement the following functions:

1. find_more_than_average(): Find and return the percentage of students who have scored more than the average mark of the class.

2. generate_frequency(): Find how many students have scored the same marks. For example, how many have scored 0, how many have scored 1, how many have scored 3….how many have scored 25. The result should be populated in a list and returned.

3. sort_marks(): Sort the marks in the increasing order from 0 to 25. The sorted values should be populated in a list and returned.


Sample Input                                                          Expected Output

list_of_marks = (12,18,25,24,2,5,18,20,20,21)                              70.0  
                                                           [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2,
                                                                     0, 2, 1, 0, 0, 1, 1]
                                                                [2, 5, 12, 18, 18, 20, 20, 21, 24, 25]
"""
# Code

#Global variable
list_of_marks=(12,18,25,24,2,5,18,20,20,21)

def find_more_than_average():
    #Remove pass and write your logic here
    avg = sum(list_of_marks)/len(list_of_marks)
    count = 0
    for i in list_of_marks:
        if i > avg:
            count +=1
        else:
            pass
    return (count*100)/len(list_of_marks)

def sort_marks():
    #Remove pass and write your logic here
    return sorted(list_of_marks)

def generate_frequency():
    #Remove pass and write your logic here
    count = [0] * (max(list_of_marks)+1)
    for i in list_of_marks:
        count[i] += 1
    return count
print(find_more_than_average())
# print(generate_frequency())
print(sort_marks())
