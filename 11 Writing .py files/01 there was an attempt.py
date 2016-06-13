import os
import sys
import subprocess

setupFileName = "omg2.py"

def Write():
    output = open(setupFileName, "w")
    w = lambda s: output.write(s + "\n")

    w("#import summat")
    w("")
    w("# I've just made a py file")
    w("# How d'ya like that")
    w("inp = input('Do summat')")


def main():
    Write()
    print("")
    print("Setup script written to %s; run it as:" % setupFileName)
    print("    python %s build" % setupFileName)
    subprocess.call(["python", setupFileName, "build"]) # run it too

main()
