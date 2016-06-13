r = 0
while r<1:
    try: input = raw_input
    except NameError: pass
    print("Hi " + input("Say something: "))
