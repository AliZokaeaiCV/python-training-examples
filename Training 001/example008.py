"""
Find all Prime numbers in an interval
"""

# Python program to print all
# prime numbers in an interval
# number should be greater than 1

# We define two global variable for store first and second number
start_num = 0
end_num = 0


def find_prime_number(start, end):
    # sanitize input numbers and remove negative sign and decimal parts.
    start_number = abs(int(start))
    end_number = abs(int(end))
    # if first number is smaller of second number, their value are changed.
    if (start_number > end_number):
        start_num = end_number
        end_num = start_number
    else:
        start_num = start_number
        end_num = end_number

    # make a list for result
    list_of_prime_numbers = []

    # make a list for check prime number
    list_for_check = []

    # a loop for find the prime number
    for i in range(start_num, end_num + 1):
        if i > 1:
            # Here we find all remainder of divide  a number to numbers of 2 to itself
            for j in range(2, i):
                # We store all reminder in a list by string format
                list_for_check.append(str(i % j))

        # If in remainder list we have any zero, that number is not prime, so doesn't add to result list
        # If in remainder list we don't have any zero, so we add that number to our result list
        if (('0' in list_for_check) != True):
            list_of_prime_numbers.append(i)

            # Now we delete all member of reminder check list
            list_for_check = []
        else:
            # Even the number does not been a prim number we clear all member of check list for next loop
            list_for_check = []

    # now we have a list of all prime numbers
    return list_of_prime_numbers


# we here define a loop for convenience calculations
permission = 1

while (permission != 0):
    print("=============================================================")
    start = int(input("Please enter an integer and positive number for start: "))
    end = int(input("Please enter an integer and positive number for number: "))
    print(find_prime_number(start, end))
    permission = (int(input("if you want to stop press [0] otherwise press [1]: ")))
