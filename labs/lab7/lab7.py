"""
Name: <Christopher Hamilton, II>
<lab7>.py
"""


import math


def cash_conversion():
    i = int(input("Enter an integer: "))
    print("$" + "{:.2f}". format(i))


def encode():
    m = input("Enter a message to be encoded: ")
    k = int(input("Enter a integer key value: "))
    acc = ""
    for i in message:
        x = ord(i)
        numbers = chr(k + x)
        acc = acc + numbers
    print(acc)


def sphere_area(radius):
    area = 4 * math.pi * radius ** 2
    return area


def sphere_volume(radius):
    volume = 4 / 3 * math.pi * radius ** 3
    return volume


def sum_n(n):
    acc = 0
    for i in range(1, n +1):
        acc = acc + 1
    return acc


def sum_n_cumbes(n):
    acc = 0
    for i in range(1, n +1):
        acc = acc + i ** 3
    return acc

def encode_better():
    m = input("Enter a message to encode: ")
    k = int(input("Enter a key: "))
    acc = ""
    for i in range(len(message)):
        m = ord(m[i])
        k = ord(k[1])
        eva = m + k - 97
        acc = acc + chr(eva)
    print(acc)


def main():
    cash_conversion()
    encode()
    print(sphere_area(1))
    print(sphere_volume(2))
    print(sum_n(3))
    print(sum_n_cumbes(4))
    encode_better()
    pass


main()
