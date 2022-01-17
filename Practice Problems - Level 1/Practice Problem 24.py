# Problem Statement
"""
Given two positive integers. Write a python function to return the greatest common divisor of the given numbers.

Sample Input                               Expected Output

14 and 35                                        7

800 and 2800                                    400

"""

# Code:


def find_gcd(num1, num2):
    # start writing your code here
    factor_a = set()
    factor_b = set()
    for i in range(2, num1+1):
        if num1 % i == 0:
            factor_a.add(i)
        else:
            pass
    for i in range(2, num2+1):
        if num2 % i == 0:
            factor_b.add(i)
        else:
            pass

    return max(factor_a.intersection(factor_b))


num1 = 45
num2 = 9
print(find_gcd(num1, num2))


# Alternative Method:


def find_gcd(num1, num2):
    # start writing your code here
    factor_a = set([i for i in range(2, num1+1) if num1 % i == 0])
    factor_b = set([i for i in range(2, num2+1) if num2 % i == 0])
    return max(factor_a.intersection(factor_b))


num1 = 45
num2 = 9
print(find_gcd(num1, num2))
