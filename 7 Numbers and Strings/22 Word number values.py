totalnum = []

while 1:
    target = int(input("Enter an integer:"))

    ## defines the dictionary
    numlet = dict()

    numlet[' '] = 0
    numlet["'"] = 0
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

    ## read the dictionary
    def main():
        with open("Dictionary.txt","r") as f:
            words = f.read().splitlines()
            for word in words:                          # separate the words
                length = len(word)                      # get length of words
                stack = []
                for letnum in range(0,length):
                    stack.append(numlet[word[letnum]])
                wordval = sum(stack)
                if wordval == target:                   # change operation for ranges
                    print(word," = ",str(wordval))
                    totalnum.append(word)
    
    main()

    print(len(totalnum))


