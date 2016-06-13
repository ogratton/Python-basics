rep = 1
while rep == 1:
    num = int(input("Enter a number you think is a prime:"))

    for n in range(num,num+1):
            for x in range(2,n):
                    if n % x == 0:
                            print("no,",n, 'equals', x, '*', int(n/x))
                            break
            else:
                    print(n, "is a prime number. Well done.")

