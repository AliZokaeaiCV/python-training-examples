# Pyhton program to find the maximum of two numbers

def maximum(a, b):
    a = float(a)
    b = float(b)
    print("You Enter two numbers {0} and {1}." .format(a,b))
    if a >= b:
        print("Maximum number is fist number:{0}".format(a))
    else:
        print("Maximum number is second number:{0}".format(b))


# Driver code

a = input("Please import first number: ")
b = input("Please import second number: ")

maximum(a, b)
