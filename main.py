from colorama import Fore, init
import fractions
import sys

def cube(x):
    return x**3

def rec_prism(x, y, z):
    return x * y * z

def cylinder(x, y):
    return 3.14 * x ** 2 * y

def cone(x, y, z):
    z = fractions.Fraction(numerator=1, denominator=3)
    return z * 3.14 * x ** 2 * y

def sphere(x, y):
    y = fractions.Fraction(numerator=4, denominator=3)
    return y * 3.14 * x ** 3

def tri_pyramid(x, y):
    f = fractions.Fraction(numerator=1, denominator=3)
    return f * x * y

def tri_prism(x, y):
    return x * y

def sqr_pyramid(x, y):
    return x**2 * y / 3

def print_titles():

    print(f"""
 {Fore.BLUE}~~~~~~~~~~~~~~~~~~~~~
 {Fore.CYAN}1. Cube
 {Fore.CYAN}2. Rectangular Prism
 {Fore.CYAN}3. Cylinder
 {Fore.CYAN}4. Cone
 {Fore.CYAN}5. Sphere
 {Fore.CYAN}6. Triangular Pyramid
 {Fore.CYAN}7. Triangular Prism
 {Fore.CYAN}8. Square Pyramid
 {Fore.CYAN}9. Exit
 {Fore.BLUE}~~~~~~~~~~~~~~~~~~~~~
 {Fore.CYAN}π = 3.14
 {Fore.BLUE}~~~~~~~~~~~~~~~~~~~~~

        """)
init()
print_titles()

while True:
    choice = input("Enter choice(1/2/3/4/5/6/7/8/9): ")

    if choice in ('1'):
        num1 = float(input("Enter side value: "))
        print(cube(num1))

    if choice in ('2'):
        num1 = float(input("Enter length: "))
        num2 = float(input("Enter width: "))
        num3 = float(input("Enter length: "))
        print(rec_prism(num1, num2, num3))

    if choice in ('3'):
        num1 = float(input("Enter your radius: "))
        num2 = float(input("Enter your height: "))
        print(cylinder(num1, num2))

    if choice in ('4'):
        num1 = float(input("Enter your radius: "))
        num2 = float(input("Enter your height: "))
        z = fractions.Fraction(numerator=1, denominator=3)
        num3 = float(z)
        print(cone(num1, num2, num3))

    if choice in ('5'):
        num1 = float(input("Enter your radius: "))
        y = fractions.Fraction(numerator=4, denominator=3)
        num2 = float(y)
        print(sphere(num1, num2))

    if choice in ('6'):
        num1 = float(input("Enter base area: "))
        num2 = float(input("Enter height: "))
        print(tri_pyramid(num1, num2))

    if choice in ('7'):
        num1 = float(input("Enter base area: "))
        num2 = float(input("Enter height: "))
        print(tri_prism(num1, num2))

    if choice in ('8'):
        num1 = float(input("Enter base edge: "))
        num2 = float(input("Enter height: "))
        print(sqr_pyramid(num1, num2))

    if choice in ('9'):
        sys.exit('Program Stopped!')

        break
