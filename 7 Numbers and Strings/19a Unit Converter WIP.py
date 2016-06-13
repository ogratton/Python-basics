#!python3

m2f = 3.2808399
f2m = 0.3048

r = 1
while r == 1:
    x = input("Type 'm' to convert metres to feet, and type 'f' to convert feet to metres: ")
    if x == 'm':
        n = int(input("How many metres?  "))
        feet = n*m2f
        print(n,"metres is",feet,"feet")
        r = 0
    elif x == 'f':
        n = int(input("How mant feet?  "))
        metres = n*f2m
        print(metres)
        r = 0
    else:
        r = 1




