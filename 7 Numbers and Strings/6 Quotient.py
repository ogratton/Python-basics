'''Quotient (Says the division and then the remainder'''

x = int(input("Enter the main number: "))
y = int(input("Enter the number to divide the previous by: "))
div = x//y
rem = x%y
print('The quotient of ',x, ' and ', y, ' is ', div, ' with a remainder of ', rem, '.', sep='')
