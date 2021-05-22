"""The idea to solve this problem is to iterate through
all the numbers starting form 2 to (N/2) using a for loop
and for every number check if it divides N. if we find any
number that divides,we return false. If we did not find any
number between 2 and N/2 which divides N then it means that
N is a prime number and we will return True."""


# python program to check if
# given number is prime or not


def check_is_prim_number(num):
    for i in range(2, int((num / 2) + 1)):
        print(i)
        # If num is divisible by any number between
        # 2 and n/2 , it isn't prime
        if num % i == 0:
            # if it divide to a number except 1 and itself the number isn't a prime
            # Then function return False
            return False
        else:
            continue
    # if a number be prime the function return True
    return True


def sanitize(num):
    """this function check input if it was a integer number
    return a absolute and positive number, otherwise return Zero"""
    number = 0
    if (type(num) == 'int'):
        number = abs(int(num))
        return number
    else:
        return 0


permission = 0
while (permission == 0):
    num = sanitize(input("Please enter a number (Positive and integer) for Prime check: "))
    print(check_is_prim_number(num))
    permission = int(input("if want continue press 0 otherwise press 1: "))
