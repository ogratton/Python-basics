word = "robot"

while 1:
    line = input("Line: ")

    if word in line.lower():            # if the string "robot" is in there at all
        pos = line.lower().index(word)  # get its position (starts from 0)

    if pos == 0:                                                            # if word is at start of line
        left = True                                                         # - allow
    elif line[pos -1] in [" ", ",", ".", "?", ":", "'", '"']:               # if word not at start but character before isn't a letter
        left = True                                                         # - allow
    else:
        left = False                                                        # don't allow
    if len(line) == pos + len(word):                                        # if word is at end of line
        right = True                                                        # - allow
    elif line[pos + len(word)] in [" ", ",", ".", "?", ":", "'", '"']:      # if word not at end but character after isn't a letter
        right = True                                                        # - allow
    else:
        right = False                                                       # don't allow

    if left and right:                                                      # both sides clear
        both = True                                                         # jolly good
    else:
        both = False                                                        # don't bother

    if both:                                # if word satisfies conditions above
        if word.lower() in line:
            print(">> small",word)          # lower case
        elif word.upper() in line:
            print(">> large",word)          # upper case
        elif word.lower() in line.lower(): 
            print(">> medium",word)         # neither fully upper nor lower case
    else:
        print(">> no",word)                 # not in there at all
