'''Conversion of strings to int before addition'''

xString = input("Enter a number: ")                          # xString is the input
x = int(xString)                                             # x = the INTEGER equal to xString

yString = input("Enter a second number: ")                   # yString is the input
y = int(yString)                                             # y = the INTEGER equal to yString

print('The sum of ', x, ' and ', y, ' is ', x+y, '.', sep='')# Prin the sum of the integers
