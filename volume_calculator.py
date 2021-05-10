import fractions
import sys

def cylinder(x, y):
    return 3.14 * x ** 2 * y

def cone(x, y, z):
    z = fractions.Fraction(numerator=1, denominator=3)
    return z * 3.14 * x ** 2 * y

def sphere(x, y):
    y = fractions.Fraction(numerator=4, denominator=3)
    return y * 3.14 * x ** 3

def print_titles():

    print("""
    ~~~~~~~~~~~~~~~~~~~~~
    1. Cylinder
    2. Cone
    3. Sphere
    ~~~~~~~~~~~~~~~~~~~~~
    π = 3.14
    ~~~~~~~~~~~~~~~~~~~~~

        """)
    print("""The Else statement is broken for the cone.
    So you will have two 'turns' or infinite turns if you keep choosing cone.
    Just ignore the 'Invalid Input' message. -Crue
        """)
print_titles()

while True:
    choice = input("Enter choice(1/2/3/4) 4 = End Program: ")

    if choice in ('1'):
        num1 = float(input("Enter your radius: "))
        num2 = float(input("Enter your height: "))
        print(cylinder(num1, num2))
    if choice in ('2'):
        num1 = float(input("Enter your radius: "))
        num2 = float(input("Enter your height: "))
        z = fractions.Fraction(numerator=1, denominator=3)
        num3 = float(z)
        print(cone(num1, num2, num3))
    if choice in ('3'):
        num1 = float(input("Enter your radius: "))
        y = fractions.Fraction(numerator=4, denominator=3)
        num2 = float(y)
        print(sphere(num1, num2))
    if choice in ('4'):
        sys.exit('Program Stopped!')

        break
    else:
        print("Invalid Input")