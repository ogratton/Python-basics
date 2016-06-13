one = 0
two = 0
three = 0
u1 = 0
u2 = 0
u3 = 0

q = str(input("Ask question here:"))
# e.g. "How many pounds in 5 kilogrammes?"


pounds = q.__contains__('pounds')
pound = q.__contains__('pound')
lbs = q.__contains__('lbs')
lb = q.__contains__('lb')

kilo = q.__contains__('kilo')
kilos = q.__contains__('kilos')
kilogrammes = q.__contains__('kilogrammes')
kgs = q.__contains__('kgs')
kg = q.__contains__('kg')

stones = q.__contains__('stones')
stone = q.__contains__('stone')
st = q.__contains__('st')

if pounds == True:
    one = q.find('pounds')
    u1 = 'pounds'
elif pound == True:
    one = q.find('pound')
    u1 = 'pound'
elif lbs == True:
    one = q.find('lbs')
    u1 = 'lbs'
elif lb == True:
    one = q.find('lb')
    u1 = 'lb'
else:
    one = 0

    
if kilo == True:
    two = q.find('kilo')
    u2 = 'kilo'
if kilos == True:
    two = q.find('kilos')
    u2 = 'kilos'
elif kilogrammes == True:
    two = q.find('kilogrammes')
    u2 = 'kilogrammes'
elif kgs == True:
    two = q.find('kgs')
    u2 = 'kgs'
elif kg == True:
    two = q.find('kg')
    u2 = 'kg'
else:
    two = 0


if stones == True:
    three = q.find('stones')
    u3 = 'stones'
elif stone == True:
    three = q.find('stone')
    u3 = 'stone'
elif st == True:
    three = q.find('st')
    u3 = 'st'
else:
    three = 0


##do this more intelligently and get rid of w, x and z
    
if two < one:      # how many kgs in a lb
    z = 0.454
    print("There are",z,u2,"in a",u1)
elif one < two:    # how many lbs in a kg
    z = (1/0.454)
    print("There are",z,u1,"in a",u2)
elif one < three:  # how many lbs in a stone
    z = 14
    print("There are",z,u1,"in a",u3)
elif three > one:  # how many stones in a lb
    z = (1/14)
    print("There are",z,u3,"in a",u1)
else:
    0



