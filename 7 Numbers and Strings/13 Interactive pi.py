radius = int(input("Enter the radius of a circle in cm:"))

pi = 3.14159265358979                     # global constant

def circleArea(radius):
    return pi*radius*radius               # using the constant

def circleCirc(radius):
    return 2*pi*radius                    # using the constant again

def main():
    print("circle area with radius 5:", circleArea(radius))
    print("cirumference of same circle:", circleCirc(radius))

main()
