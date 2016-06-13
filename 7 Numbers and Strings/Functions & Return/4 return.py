'''Display a sum problems with a function returning a string,
not printing directly.
'''

def sumProblemString(x, y):
    sum = x + y
    return 'The sum of {} and {} is {}.'.format(x, y, sum)

def main():
    print(sumProblemString(2, 3))
    a = int(input("Enter an integer: "))
    b = int(input("Enter another integer: "))
    print(sumProblemString(a, b))

main() 
