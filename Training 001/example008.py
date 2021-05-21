"""
Find all Prime numbers in an interval
"""

# Python program to print all
# prime numbers in an interval
# number should be greater than 1


def find_prime_number(start, end):
    # sanitize input numbers
    start_num = abs(int(start))
    end_num = abs(int(end))

    # make a list
    list_of_prime_numbers = []

    # a loop for find the prime number
    for i in range(start, end+1):
        print("**************")
        if i > 1:
            for j in range(2, i):
                print("j{0},i{1}".format(j,i))
                if (i % j == 0):
                    print("break")
                    break
                else:
                    print("enter")
                    list_of_prime_numbers.append(i)
    return list_of_prime_numbers


start = int(input("Please enter an integer and positive number for start: "))
end = int(input("Please enter an integer and positive number for number: "))

print(find_prime_number(start, end))
