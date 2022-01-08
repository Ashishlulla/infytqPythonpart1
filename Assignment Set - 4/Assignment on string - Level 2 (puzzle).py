# Problem Statement
"""
Write a python function, encrypt_sentence() which accepts a message and encrypts it based on rules given below and returns the encrypted message.
Words at odd position -> Reverse It
Words at even position -> Rearrange the characters so that all consonants appear before the vowels and their order should not change

Note: 

Assume that the sentence would begin with a word and there will be only a single space between the words.

Perform case sensitive string operations wherever necessary.

Sample Input                      Expected Output

the sun rises in the east      eht snu sesir ni eht stea
"""

# Code

def encrypt_sentence(sentence):
    #start writing your code here
    c = ""
    lista = list(sentence.split(" "))
    new_list = []
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for i in range(len(lista)):
        if (i+1) % 2 == 0:
            for j in lista[i]:
                if j in vowels:
                    lista[i]= lista[i].replace(j, "")
                    c = c + j
            d = lista[i]+c
            new_list.append(d)
            c = ""
        else:
            d = lista[i][::-1]
            new_list.append(d)
    a = " ".join(new_list)
    return a
  

sentence="The sun rises in the east"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)
