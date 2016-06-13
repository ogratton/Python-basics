import os
import shutil


all_notes = []
notes = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
f = 0
i = 3 # cos our lowest not is D#2
o = 2


for filename in os.listdir("."):
    if filename.endswith(".py"):
        pass
    else:
        all_notes.append(filename)

for file in all_notes:
    os.rename(file, str(f)+" "+notes[i]+str(o)+".mp3")
    f += 1
    i += 1
    if i == 12:
        i = 0
        o += 1



print("done")
