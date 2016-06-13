import os

for filename in os.listdir("."):
    if filename.startswith("DSC") or filename.startswith("MAH"):
        os.rename(filename, filename[3:])
