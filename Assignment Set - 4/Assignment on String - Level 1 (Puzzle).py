# Problem Statement
"""
Write a python program to display all the common characters between two strings. Return -1 if there are no matching characters.

Note: Ignore blank spaces if there are any. Perform case sensitive string comparison wherever necessary.

Sample Input                     Expected output

"I like Python"                    lieyon
"""
# Code: 


def find_common_characters(msg1,msg2):
    #Remove pass and write your logic here
    new_string = ""
    for i in msg1:
        if i in msg2 and i != " " and i not in new_string:
            new_string = new_string + i
        else:
            pass
    if len(new_string) == 0:
        return -1
    else:
        return new_string

#Provide different values for msg1,msg2 and test your program
msg1="moto"
msg2='moto'
common_characters=find_common_characters(msg1,msg2)
print(common_characters)

 
