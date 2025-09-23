# What is Plagiarism?

# Plagiarism is when someone uses someone else's work,ideas or creation without giving proper credit and present it as their own.

# Plagiarism detection using Python Program

import difflib # used for comparing sequences especially strings. Helps find diff btw files or text snippets and can generate diff,similarities,even close matches

with open ("C:/Users/Shuvam Saha/Desktop/Python codes/shuvam/demo1.txt") as f1 , open("C:/Users/Shuvam Saha/Desktop/Python codes/shuvam/demo2.txt") as f2:

    data_f1 = f1.read()

    data_f2 = f2.read()

matches = difflib.SequenceMatcher(None,data_f1,data_f2).ratio() #SequenceMatcher is a class that helps you compare two sequences(like strings,list etc.).
                                                                #The first parameter is a function that tells which elements to ignore,if you dont want to ignore anything ,you pass none.
                                                                #ratio() func in SequenceMatcher calculates the similarity btw two sequences(like strings or lists).

print(f"The plagiarized content is : {matches}%")



