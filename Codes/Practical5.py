"""
5. Write a function that finds the sum of the n terms of the following series. Import the factorial function created in question 4.
    Series : 1-x2/2!+x4/4!-x6/6!+…xn/n!

"""
from Practical3 import factorial


def sum_series(x, n):
    sum = 0
    for i in range(1, n+1):
        term = ((-1)**(i+1))*(x**(2*i-2)/factorial(2*i-2))
        sum += term
    return sum


if __name__ == "__main__":
    n = int(input("Enter n: "))
    x = int(input("Enter x: "))
    sum = sum_series(x, n)
    print(f'Sum of {n} terms of series for x={x} is {sum}')
