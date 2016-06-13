word = str(input("Enter a word: "))

for l in range(0,len(word)):
    First = word[0]
    pos = 0
    for let in range(0, len(word)):
        if word[let] < First:
            First = word[let]
            pos = let
    word = word[:pos] + word[(pos+1):]
    print(First)



















































        
