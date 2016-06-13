def main():
        print (letter)


score = float(input('What mark did you get?'))
if score >= 90:
        letter = 'A*'
        main()
        print("Very good")
elif score >= 80:
        letter = 'A'
        main()
        print("Well done")
elif score >= 70:
        letter = 'B'
        main()
        print("Not bad")
elif score >= 60:
        letter = 'C'
        main()
        print("Could do better")
else:
        letter = 'D'
        main()
        print("Jesus Christ, what happened?")


