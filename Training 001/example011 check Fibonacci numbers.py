"""
>> CHECK IS A NUMBER FIBONACCI

Here we select a number and programme check is it a fibonacci number or not.

There we use of these formula

(5*n^2+4) or (5n^2 -4)

"""
# python program to check if x is a perfect square
import math


# A utility function that returns true if x is perfect square

def is_perfect_square(x):
    """this function calculates a perfect number. perfect number is a (int(n))^2;
     Here n is a integer number without any decimal part"""
    s = int(math.sqrt(x))
    return s * s == x


# Returns true if n is a Fibonacci Number, else false
def is_fibonacci(n):
    """this function check a perfect number is a Fibonacci number or not.
    It return True or False"""
    # n is Fibonacci if one of 5*n*n + 4 or 5*n*n - 4 or both
    # is a perfect square
    return is_perfect_square(5 * n * n + 4) or (is_perfect_square(5 * n * n - 4))


# A utility function  to test above functions
def range_fibonacci(first_number=0, second_number=0):
    """This function made a list of fibonacci numbers and return a list."""
    # this list store all Fibonacci numbers in a range.
    list_of_fibonacci_numbers = []
    # If second Number equal by zero mean user doesn't enter any number or wrong number.
    if second_number == 0:
        return False
    else:
        for i in range(first_number, second_number):
            if is_fibonacci(i):
                list_of_fibonacci_numbers.append(i)
    # If Our list have any member this part return a code else return false.
    if len(list_of_fibonacci_numbers) > 0:
        return list_of_fibonacci_numbers
    else:
        return False


# Flag for continue process, Zero = stop
permission = 1
while permission != 0:
    # This loop take numbers and options of user.
    # select method of process
    choose = input("\t1 - Check only one number;"
                   "\n\t2 - Check a interval of one to a favorite number (0, number);"
                   "\n\t3 - Check a interval between to favorite number;"
                   "\n\t4 - Exit;"
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
        if is_fibonacci(number):
            print(number, " is a Fibonacci number.")
        else:
            print(number, " isn't a Fibonacci Number")

        print("=======================================================")

    elif choose == 2:

        # Get the favorite number
        number = abs(int(input("Enter a positive and grater than 2, number: ")))
        print("You enter :", number)
        print("Now We calculate interval (0, ", number, ")")
        if range_fibonacci(0, number):
            print("We find ", len(range_fibonacci(0, number)), "number(s), there is your list:",
                  range_fibonacci(0, number))
        else:
            print("In this interval is not any Fibonacci number.")

        print("=======================================================")
    elif choose == 3:

        # Get the favorite numbers
        number_first = abs(int(input("Enter a first positive and grater than 2, number: ")))
        number_second = abs(int(input("Enter a second positive and grater than 2, number: ")))

        # check two number is not equal, if they were equal request another number for calculation
        while number_second == number_first:
            print("your first and second numbers is equal please and other number\n(Your first number is:",
                  number_first, ")")
            number_second = abs(int(input(">>Enter a second positive and grater than 2, number: ")))
        # check arrangement of numbers
        # if first number is small then second, their places will changed.
        if number_second < number_first:
            number_first, number_second = number_second, number_first

        print("You enter two number (", number_first, ",", number_second, ")")
        print("Now We calculate interval (", number_first, ",", number_second, ")")
        if range_fibonacci(number_first, number_second):
            print("We find ", len(range_fibonacci(number_first, number_second)), "number(s), there is your list:",
                  range_fibonacci(number_first, number_second))
        else:
            print("In this interval is not any Fibonacci number.")

        print("=======================================================")

    elif choose == 4:
        print("Your welcome.")
        print("=======================================================")
        permission = 0
