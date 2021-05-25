"""
simple interest formula is given by:
simple interest = (P * T * R)/ 100
where:
P: is the principle amount
T: is the time
R: is the rate
"""

"""
Example 1:
Input : P = 10000
        R = 5
        T = 5
Output:2500

We need to find simple interest on 
Rs. 10,000 at the rate of 5% fro 5
units of time

--------------------

Example 2:

Input : P = 3000
        R = 7
        T = 1
Output : 210

"""

# Python 3 program to find simple interest
# for given principal amount, time and
# rate of interest.

def simple_int(p,t,r):
    print('The Principal is: ', p)
    print('The Time period is: ', t)
    print('THe Rate of interest is: ',r)

    si =(p*t*r)/100

    print('The Simple interest is ', si)
    total= si + p
    print('The total is ', total)
    return  si


# Driver code
principle = int(input("Please enter the Principal: "))
time = int(input("Please enter the tim duration: "))
rate = int(input("Please enter the Rate: "))


simple_int(principle, time, rate)

