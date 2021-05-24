"""
In mathematical term, the secquence FN of Fibonacci numbers is defined by the recurrence relation

Fn = Fn-1 + Fn-2
with seed Value

F0 = 0 and F1 =1
"""


# Function for nth Fibonacci number


def Fibonacci(n):
    """this function calculate fibonacci number of n"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


def make_Fibonacci_list(n):
    """This function make a list of all Fibonacci numbers"""
    # Remove negative and string characters
    number = int(n)

    # list of Fibonacci numbers
    Fibonacci_list = []

    # loop on all number between Zero to selected number and add it to our list
    for n in range(0, number):
        Fibonacci_list.append((n, Fibonacci(n)))

    return Fibonacci_list


# Flag for continue process, Zero = stop
permission = 1
while (permission != 0):

    # select method of process
    choose = input("\t1 - Calculate just Fibonacci number;"
                   "\n\t2 - Calculate a list of Fibonacci numbers;"
                   "\n\t3 - Exit;"
                   "\nPlease enter one option (just enter option number): ")
    print("You select Option:", choose)
    # Here we convert choose to number(integer)
    choose = int(choose)

    if choose == 1:

        # Get the selected number
        number = input("Enter a positive and grater than 2, number: ")
        print("You enter :", number)
        # Here we convert number to number(integer)
        number = int(number)
        print("Your number is: ", number)
        print("Its Fibonacci number is: ", Fibonacci(number))
        print("=======================================================")

    elif choose == 2:

        # Get the selected number
        number = input("Enter a positive and grater than 2, number: ")
        print("You enter :", number)
        # Here we convert number to number(integer)
        number = int(number)
        print("Your number is: ", number)
        print("Its Fibonacci number is: ", Fibonacci(number))
        print("The Fibonacci list of numbers before it are: ", make_Fibonacci_list(number))
        print("=======================================================")

    elif choose == 3:
        print("Your welcome.")
        print("=======================================================")
        permission = 0
