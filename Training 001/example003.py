# Python 3 program to find factorial of given number

def factorial(n):
    # single line to find factorial
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)


num = float(input("Please import a number for calculate its factorial: "))
print("Your number was", num, "and its factorial is", factorial(num))


# Python 3 program fo find factorial of given number

def factorial2(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while (n > 1):
            fact *= n
            n -= 1
        return fact


number = int(input("Please import a number to calculate its factorial: "))

print("Your number is ", number, "and its factorial is ", factorial2(number))

# Python 3 program to find factorial of given number
import math


def factorial3(n):
    return (math.factorial(n))


number1 = int(input("Please import a number to calculate its factorial: "))

print("Your number is ", number1, "and its factorial is ", factorial3(number1))
