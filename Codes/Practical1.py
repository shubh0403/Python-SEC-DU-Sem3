"""
1. Write a function that takes the lengths of three sides : side1,side2 and side3 of the triangle as the input from the user using input function and return the area and perimeter of the triangle as a tuple. Also, assert that sum of the length of any two sides is greater than the third side.

"""

import math


def calculate(side1, side2, side3):
    perimeter = 0
    area = 0
    # Checking condition : Sum of the length of any two sides is greater than the third side
    if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
        print("Given sides form a triangle.")
        perimeter = side1 + side2 + side3
        s = perimeter/2
        area = math.sqrt(s*(s-side1)*(s-side2)*(s-side3))
    else:
        print("Given sides do not form a triangle. The sum of two sides of a triangle should be greater than the third side")
        quit()

    return perimeter, area


if __name__ == "__main__":

    side1 = float(input("Enter the length of side 1: "))
    side2 = float(input("Enter the length of side 2: "))
    side3 = float(input("Enter the length of side 3: "))

    perimeter, area = calculate(side1, side2, side3)
    print(f'Perimeter : {perimeter} units')
    print(f"Area: {area:.3f} sq. units")
