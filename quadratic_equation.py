from math import *

def quadratic_equation_r(a, b, c):
    if (a == 0):
        print("Not quadratic equation: a = 0")
        return None, None
    D = b ** 2 - 4 * a * c
    if (D < 0):
        print("No real roots: D < 0")
        return None, None
    if (D == 0):
        return -b / (2 * a), -b / (2 * a)

    x1 = (-b + sqrt(D)) / (2 * a)
    x2 = (-b - sqrt(D)) / (2 * a)
    return x1, x2 


if __name__ == "__main__":
    print(
        "Module for solving \
quadratic equation")
