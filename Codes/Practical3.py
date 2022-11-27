"""
3. Write a Python function to find the nth term of Fibonacci sequence and its factorial.Return the result as a list.
"""


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


def fibonnaci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonnaci(n-1) + fibonnaci(n-2)


if __name__ == '__main__':
    num = int(input("Enter a number: "))
    print(f"{num} term of fibonacci series : ", fibonnaci(num))
    print(f"Factorial of {num} : ", factorial(num))
