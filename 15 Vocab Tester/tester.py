from easygui import *
import random

def wordreview():
    fulllist = []
    with open("data.txt","r") as f:
        global question
        question = [line.split("/") for line in f] # 'question' is the entire line split by every /
        for item in question:
            item.pop()
        num = 0
        while num < (len(question)-1):
            que = str(question[num][0])
            ans = str(question[num][1])
            correction = que + " = " + ans + "\n"
            fulllist.append(correction)
            num += 1
        textbox("Review the "+str((len(fulllist)-1))+" words before starting the test:","Latin Vocab Test",fulllist,0)
        global first
        first = 0
        global last
        last = len(question)-1
    f.close()

def test():
    global redoline
    redoline = []
    global wrongs
    wrongs = []

    with open("data.txt","r") as f:
        global i
        i = 0
        global score
        score = 0
        
        while i<int(im):									
            num = random.randint(first,last)
            q1 = 'Question '+str(i+1)+' of '+str(im)
            answer = enterbox(question[num][0],q1,"")
            que = str(question[num][0])                                               
            ans = str(question[num][1])
            correction = que + " = " + ans + "\n"

            if len(answer) == 0: 
                msgbox("You didn't even try! Minus 1 point!\nThe correct answer is:\n\n"+ans,"Shame on you!","BOOO!")                 
                score += -1             
                wrongs.append(correction)
                redoline.append(num)
            elif str(answer) in question[num]:
                msgbox("CORRECTAMUNDO!", "Well Done!")
                score += 1 
            else:
                msgbox('Wrong!\nThe correct answer is: \n'+ans,"Pull yer socks up, laddy!")	        
                wrongs.append(correction)
                redoline.append(num)
                
            i += 1 #Next question
    f.close()

def redo():
    i2 = 0
    while i2 < len(redoline):
        q1 = 'Redoing '+str(len(redoline))+' Question(s)...'
        for item in redoline:
            answer = enterbox(question[item][0],q1,"")

            if len(answer) == 0:
                ans = str(question[item][1])
                skip1 = "That's not the attitude!\nTry at least!\nThe correct answer is:\n\n"+ans
                msgbox(skip1,"Shame on you!","BOOO!")
            elif str(answer) in question[item]:
                msgbox("You got there in the end...", "Well done, I guess")
                redoline.remove(item)
                i2 += 1            
            else:
                ans = str(question[item][1])
                proper = 'Wrong!\nThe correct answer is: \n'+ans
                msgbox(proper,"Pull yer socks up, laddy!")

def scoring():
    if i>1:
        qu_pl = "questions"
    else:
        qu_pl = "question"
    if score == 1:
        sc_pl = "point"
    else:
        sc_pl = "points"
    if i == 1:
        was_pl = "was"
    else:
        was_pl = "were"

    ar1 = "There "+was_pl+" "+str(i)+" "+qu_pl+", you got "
    ar2 = str(score)+" "+str(sc_pl)+".\n"
    ar3 = "That makes your score "+str(score*100/i)+"%"
    ar4 = str(ar1)+str(ar2)+str(ar3)
    msgbox(ar4, "RESULTS")
    
r = 0
while r<1:
    wordreview()
    im = integerbox("How many questions do you want?","OCR A2 Level Vocab Test","",1,300)
    test()
    scoring()

    if len(redoline) > 0:
        textbox("You got the following wrong:","The ones that got away",wrongs,0)
        while len(redoline) > 0:
            redo()
    else:
        msgbox("You'll go far, boy!", "100%! WOO!")
        
    if ccbox("Go again?"):
        pass
    else:
        exit()
                


