# Illustrates a global constant (pi) being used inside functions

pi = 3.14159265358979                     # global constant

def circleArea(radius):
    return pi*radius*radius               # using the constant

def circleCirc(radius):
    return 2*pi*radius                    # using the constant again

def main():
    print("circle area with radius 5:", circleArea(5))
    print("cirumference of same circle:", circleCirc(5))

main()
