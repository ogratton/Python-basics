import random

a = 0
b = 0

diff = int(input("Choose the difficulty:\n For Easy (1-9x tables), type 1\n For Normal (2-15x tables), type 2\n For Hard (3-19x tables), type 3:"))
if diff == 1:
    a = 1
    b = 9
    print("You have selected Easy Mode, you lightweight!")
elif diff == 2:
    a = 2
    b = 15
    print("You have gone for Normal Mode. Good on yer, son!")
elif diff == 3:
    a = 3
    b = 19
    print("You've only gone an' chosen Hard Mode! Cor!")

r = 0
while r<1:
    score = 0
    num1 = random.randint(a,b)
    num2 = random.randint(a,b)
    print(num1,"x",num2," = ?")
    answer = int(input())
    if answer ==int(num1*num2):
        print("yay")
        score += 1
    elif answer ==0:
        print("Okey-Dokey")
        print("Stopping programme...")
        print("...")
        r = 1
    else:
        print("nay, 'twas",num1*num2)
