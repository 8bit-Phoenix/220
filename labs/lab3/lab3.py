"""
Name: <Christopher Hamilton, II>
<Lab3>.py
"""


import math


def average():
    number = eval(input("Enter the number of grades you want to enter: "))
    acc = 0
    for i in range(1, number + 1):
        grade = eval(input("Enter your grade on HW" + str(i) + ":"))
        acc = acc + grade
    grade_average = acc / number
    print(grade_average)


def tip_jar():
    tippers = 5
    acc = 0
    for i in range(1, tippers + 1):
        total = eval(input("Enter total amount tipped: "))
        acc = acc + total
    print(acc)


def newton():
    x = eval(input("Enter what x is: "))
    times = eval(input("Enter how many times to improve the approximation: "))
    approximation = x / 2
    for i in range(times):
        approximation = (approximation + x / approximation) / 2
    print(approximation)


def sequence():
    terms = eval(input("Enter the number of terms: "))
    for i in range(terms):
        print(1 + 1 // 2 * 2, end="")


def pi():
    n = eval(input("Enter the number of terms: "))
    acc = 1
    for i in range(n):
        num = 2 + (1 // 2 * 2)
        den = 1 + ((1 + 1) // 2 * 2)
        acc = acc * (num / den)
    print(acc)


average()
tip_jar()
newton()
sequence()
pi()