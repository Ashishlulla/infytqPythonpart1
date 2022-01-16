# Problem Statement
"""
Write a python function to generate and return the list of all possible sentences created from the given lists of Subject, Verb and Object.
Note: The sentence should contain only one subject, verb and object each.

Sample Input                                           Expected Output

subjects=["I", "You"]                                    I Play Hockey
verbs=["Play", "Love"]                                   I Play Football           
objects=["Hockey","Football"]                            I Love Hockey
                                                         I Love Football
                                                         You Play Hockey
                                                         You Play Football
                                                         You Love Hockey
                                                         You Love Football        
  """
#  Code: 

def generate_sentences(subjects, verbs, objects):
    # start writing your code here
    string = ""
    sentence_list = []
    for i in range(len(subjects)):
        for j in range(len(verbs)):
            for k in range(len(objects)):
                string = subjects[i] + " " + verbs[j] + " " + objects[k]
                sentence_list.append(string)

    return sentence_list

subjects = ["I", "You"]
verbs = ["love", "play"]
objects = ["Hockey", "Football"]
print(generate_sentences(subjects, verbs, objects))

