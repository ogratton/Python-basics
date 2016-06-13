def main():

    while 1:
        
        reply = input("Enter an integer: ")
        if reply == None: return None           # Not sure why necessary

        try:
            reply = int(reply)
        except:
            print("That's not an integer")
            continue

        return reply

main()
