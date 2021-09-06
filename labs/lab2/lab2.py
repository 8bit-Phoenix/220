"""
Name: <Christopher Hamilton, II>
<Lab2>.py
"""


import math


def sum_of_threes():
    number = eval(input("Enter The Upper bound:"))
    acc = 0
    for x in range(0, number+1, 3):
        acc = acc+x
    print(acc)


def muliplication_table():
    for x in range(1, 11):
        for z in range(1, 11):
            print(x * z, end=" ")
        print()


def triangle_area():
    a = eval(input("Enter The Length Of A:"))
    b = eval(input("Enter The Length Of B:"))
    c = eval(input("Enter The Length Of C:"))
    s = (a + b + c) / 2
    area = math.sqrt(s * (s-a) * (s-b) * (s-c))
    print(area)


def sumSquares():
    start = eval(input("Enter The Starting Number:"))
    finish = eval(input("Enter The Finishing Number:"))
    acc = 0
    for x in range(start, finish + 1):
        acc += (x * x)
    print(acc)


def power():
    base = eval(input("Enter Base Number:"))
    exp = eval(input("Enter Exponent:"))
    acc = 1
    for x in range(exp):
        acc = acc * base
    print(base, "^", exp, "=", acc)

sum_of_threes()
muliplication_table()
triangle_area()
sumSquares()
power()