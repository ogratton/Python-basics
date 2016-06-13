score = float(input('What mark did you get?'))
if score >= 90:
        letter = 'A*'
else:
    if score >= 80:
            letter = 'A'
    else:
        if score >= 70:
                letter = 'B'
        else:
            if score >= 60:
                    letter = 'C'
            else:
                    letter = 'D'

print (letter)
print ('Not bad')

import os
os.system("pause")
