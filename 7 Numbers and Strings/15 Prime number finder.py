stack = []

lb = int(input("Enter the lower bound:"))
ub = int(input("Enter the upper bound:"))

for n in range(lb, ub): 
        for x in range(2, n):  # Keep this as 2 no matter what
            if n % x == 0:
                #print(n, 'equals', x, '*', int(n/x))
                break
        else:
            # loop fell through without finding a factor
            print(n, 'is a prime number')
            stack.append(n)

print('Type "main()" for a list of primes between ',lb,' and ',ub)

def main():
    for item in stack:
        print(item)
