# Quadratic Solver
# -b/(2*a) - sqrt(b*b-4*a*c)/(2*a)

from math import sqrt

while 1:
    a = float(input('Enter "a" (the quadratic coefficient)'))
    b = float(input('Enter "b" (the linear coefficient)'))
    c = float(input('Enter "c" (the constant/free term)'))
    q_pos = -b/(2*a) + sqrt(b*b-4*a*c)/(2*a)
    q_neg = -b/(2*a) - sqrt(b*b-4*a*c)/(2*a)
    print("x = ", str(q_pos), "or", str(q_neg))

