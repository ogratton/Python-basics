r = 1

while r == 1:

    first = str(input("Enter your name:"))
    firstlwr = first.lower()
    length = len(firstlwr)
    stack = []


## defines the dictionary
    numlet = dict()

    numlet[' '] = 0
    numlet['-'] = 0
    numlet['a'] = 1
    numlet['b'] = 2
    numlet['c'] = 3
    numlet['d'] = 4
    numlet['e'] = 5
    numlet['f'] = 6
    numlet['g'] = 7
    numlet['h'] = 8
    numlet['i'] = 9
    numlet['j'] = 10
    numlet['k'] = 11
    numlet['l'] = 12
    numlet['m'] = 13
    numlet['n'] = 14
    numlet['o'] = 15
    numlet['p'] = 16
    numlet['q'] = 17
    numlet['r'] = 18
    numlet['s'] = 19
    numlet['t'] = 20
    numlet['u'] = 21
    numlet['v'] = 22
    numlet['w'] = 23
    numlet['x'] = 24
    numlet['y'] = 25
    numlet['z'] = 26


## this produces the numbers 0->(length) and adds them to a stack in the dictionary form: "numlet[first[n]]"
    for n in range(0,length):
        um = numlet[firstlwr[n]]
        stack.append(um)

## adds up all the numbers in the stack and prints it
    sumling = (sum(stack))
    print("When each letter in your name is assigned a number from 1-26, your name adds up to",sumling)


## checks whether the total is a prime number or not
    for n in range(sumling,sumling+1):
                for x in range(2,n):
                        if n % x == 0:
                                print(sumling,"is not a prime number. It is",x,"*",int(n/x))
                                break
                else:
                        print("Your name adds up to a prime number.")


