num = int(input("Enter a number:"))

for i in range(1,num):
    if i*i == num:
        print(str(num) + " is " + str(i) + " squared")
        break

else:
    print("Not a square")
