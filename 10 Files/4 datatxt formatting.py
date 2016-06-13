inFile = open('toomanycommas.txt', 'r')
contents = inFile.read()

outFile = open('fewercommas.txt', 'r')


contents = "blah, blah, , "
double = contents.strip(", , ")
triple = contents.strip(", , , ")

print(double)

