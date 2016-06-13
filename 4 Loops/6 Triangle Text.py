def ask():

    while 1:
        
        reply = input("Enter an integer between 2 and 10: ")

        try:
            reply = int(reply)
        except:
            print("That's not an integer")
            continue
        if reply < 2:
            print("That's smaller than 2")
            continue
        if reply > 10:
            print("That's bigger than 10")
            continue
        

        stack = []              # count up (simple)
        
        for i in range(reply+1):
            stack.append(i)

        for num in stack:
            print('#' * num)

        print("\n")

        stack = []              # count down (more complicated)
        n = 0
        
        while (reply-n) > 0:
            stack.append(reply-n)
            n += 1

        for num in stack:
            print('#' * num)

ask()
