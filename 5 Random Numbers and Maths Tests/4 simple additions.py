import random

a = 0
b = 0

diff = int(input("Choose the difficulty:\n For Easy (one-two digits), type 1\n For Normal (two-four digits), type 2\n For Hard (three-six digits), type 3:"))
if diff == 1:
    a = 1
    b = 99
    print("You have selected Easy Mode, you lightweight!")
elif diff == 2:
    a = 10
    b = 9999
    print("You have gone for Normal Mode. Good on yer, son!")
elif diff == 3:
    a = 100
    b = 999999
    print("You've only gone an' chosen Hard Mode! Cor!")

r = 0
while r<1:
    
    score = 0
    num1 = random.randint(a,b)
    num2 = random.randint(a,b)
    
    print(num1,"+",num2," = ?")
    answer = int(input())
    
    if answer ==int(num1+num2):
        print("yay")
        score += 1
    elif answer ==0:
        print("Okey-Dokey")
        print("Stopping programme...")
        print("...")
        r = 1 
    else:
        print("nay, 'twas",num1+num2)
