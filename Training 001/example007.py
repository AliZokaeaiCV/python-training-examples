"""
Area if a circle can simply be evaluated using following formula.
Area = pi * r^2
Where is radius of circle
"""

# Python program to find Area of a circle
import math


def findArea(r):
    PI = math.pi
    return PI * (pow(r, 2))


def findcircumference(r):
    PI = math.pi
    return PI * r * 2


def find_Sphere_value(r):
    PI = math.pi
    return (4 * (PI) * pow(r, 3)) / 3


def find_Surface_area(r):
    PI = math.pi
    return 4 * (PI) * pow(r, 2)


def define_radius_of_area(Area):
    PI = math.pi
    return (math.sqrt(Area)) / PI


def define_radius_of_circumference(circumference):
    PI = math.pi
    return circumference / (PI * 2)


def define_radius_of_Sphere_value(Sphere_value):
    PI = math.pi
    return math.sqrt(((Sphere_value * 3) / (4 * (PI))), 3)


def define_radius_of_Surface_area(Surface_area):
    PI = math.pi
    return math.sqrt((Surface_area / (4 * PI)), 2)

    # Drive method


answer = "start"
while (answer != "exit"):
    print("==============================================")
    print("Please Choice an option:"
          "\n 1: I have radius;"
          "\n 2: I have Area and want radius;"
          "\n 3: I have circumference and want radius;"
          "\n 4: I have Sphere value and want radius;"
          "\n 5: I have Surface area and want radius;"
          "\n 6: to exit of program")
    print("==============================================")

    choice = int(input("Please enter your option: "))

    if (choice == 1):
        print("---Radius--------------------------------------")
        radius = abs(float(input("Please enter your radius: ")))

        print(">> Area is %.6f " % findArea(radius))
        print(">> Circumference is %.6f " % findcircumference(radius))
        print(">> Surface area %.6f " % find_Surface_area(radius))
        print(">> Surface value %.6f " % find_Sphere_value(radius))

    elif (choice == 2):
        print("---Area----------------------------------------")
        area = abs(float(input("Please enter your Area: ")))

        print(">> Radius is %.9f " % define_radius_of_area(area))

    elif (choice == 3):
        print("---Circumference--------------------------------")
        circumference = abs(float(input("Please enter your Circumference: ")))

        print(">> Radius is %.9f " % define_radius_of_circumference(circumference))

    elif (choice == 4):
        print("---Sphere value---------------------------------")
        Sphere_value = abs(float(input("Please enter your Sphere value: ")))

        print(">> Radius is %.9f " % define_radius_of_Sphere_value(Sphere_value))

    elif (choice == 5):
        print("---Surface area--------------------------------")
        Surface_area = abs(float(input("Please enter your Surface area: ")))

        print(">> Radius is %.9f " % define_radius_of_Surface_area(Surface_area))

    elif (choice == 6):
        answer = "exit"
    else:
        continue
