#!/usr/bin/python3.2
# -*-coding:Utf-8 -*

#Vocabulary/translation quiz

import os
import random

keep_adding=input("Would you like to add a new word ? If yes, press \"7\" : ")
with open("data.txt","a") as f:
    while keep_adding=="7":
        word=input("Enter a word : ")
        translation=input("And its translation : ") 
        f.write("{0},{1},\n".format(word,translation))
        keep_adding=input("To continue, press \"7\" : ")


#in case the file doesn't exist, we create one :
with open("data.txt","a") as f:
    pass

os.system('clear')
print("* * * QUIZ STARTS ! * * *")

with open("data.txt","r") as f:
    question = [line.split(",") for line in f]
    i = 0
    score = 0
    while i<len(question):
        num = random.randint(0,len(question)-1)
        print("\nQuestion number ",i+1,": \nWhat is the translation for ", question[num][0], "?")
        answer = input("Answer : ")
        if (answer == str(question[num][1])):
            print("Congratulations ! That's the good answer !")
            score += 1
        else:
            print("Wrong. The correct answer was : ",question[num][1])
        i += 1

if len(question)==0:
    print("\nThe file is empty. Please add new words to start the quiz !\n")
else:   
    if i>1:
        qu_pl = "questions"
    else:
        qu_pl = "question"
    if score>1:
        sc_pl = "answers"
    else:
        sc_pl = "answer"
    print("\n RESULTS :\n ",i, qu_pl,", ",score,"correct ",sc_pl," \n"\
    ," --> Your score is : ",score*100/i,"% !\n")