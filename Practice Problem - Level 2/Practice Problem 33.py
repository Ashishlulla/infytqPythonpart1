# Problem Statement
"""
Write a python function to identify and return the number name of a given number. The number should be in the range 1 to 1000. If the number is invalid, return -1.

Example:

Sample input                                           Expected output

1                                                           one

15                                                         fifteen

45                                                        forty five

125                                               one hundred and twenty five

999                                                nine hundred and ninety nine

1000                                                       one thousand

1211                                                            -1

"""
# Code

num1_19 = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 
            18: 'Eighteen', 19: 'Nineteen'}
            
num20_90= {0:"", 2:'Twenty', 3:'Thirty', 4:'Forty', 5:'Fifty', 6:'Sixty', 7:'Seventy', 8:'Eighty', 9:'Ninety'}

num100_900 = {1:"One Hundred", 2:"Two Hundred", 3:"Three Hundred", 4:"Four Hundred", 5:"Five Hundred",6: "Six Hundred",
             7:"Seven Hundred", 8:"Eight Hundred",9:"Nine Hundred"}
             
def integer_to_english(number):
    #start writing your code here
    string =""
    if number in range(0, 19):
        return num1_19[number]
    elif number in range(20, 100):
        if number % 10 == 0:
            return num20_90[int(str(number)[0])]
        else:
            return num20_90[int(str(number)[0])] +" "+num20_90[int(str(number)[1])]
    elif number in range(100, 1000):
        if number % 100 == 0:
            return num100_900[int(str(number)[0])]
        else:
            if number % 100 in range(1,20):
                return num100_900[int(str(number)[0])]+" and "+num1_19[number % 100]
            else:
                return num100_900[int(str(number)[0])]+" and "+num20_90[int(str(number)[1])] +" "+num1_19[int(str(number)[2])]
    elif number == 1000:
        return "One Thousand"
    else:
        return -1



number=789
print(integer_to_english(number))
