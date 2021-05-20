"""
Formula to calculate compound interest annually is given by:
A=P(1+R/100)^t
Compound Interest = A - P
Where:
A: is a amount
P: is principle amount
R: is the rate
T: is the time span

Example:
    input: Principle (amount): 1200
            Time : 2
            Rate : 5.4
    Output: Compound Interest = 133.099243
"""


# Python 3 program to find compound
# Interest for given values.


def compound_interest(principle, rate, time):
    # Calculate compound interest
    total = principle * (pow((1 + rate / 100), time))
    interest = total - principle
    print("Principle is: ", principle)
    print("Rate is: ", rate)
    print("Time is: ", time)
    print("Compound in interest is: ", interest)
    print("Total payment is: ", total)


principle = float(input("Please input your principle: "))
rate = float(input("Please input your rate: "))
time = float(input("Please input your time: "))

compound_interest(principle, rate, time)
