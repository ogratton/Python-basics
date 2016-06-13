totalnum = []

while 1:
    last = str(input("Enter the last letter of a word:"))

    ## read the dictionary
    def main():
        with open("Dictionary2.txt","r") as f:
            words = f.read().splitlines()
            for word in words:                          # separate the words
                length = len(word)                      # get length of words
                end = word[length-1]                    # get last letter
                penult = word[length-2]                 # get penultimate letter
                if end == last:
                    if penult != 's':                   # if it doesn't end in ss
                        print(word)
                        totalnum.append(word)
    
    main()

    print(len(totalnum))


## this is a horrendous failure as most dictionaries give plurals
