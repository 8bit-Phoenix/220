"""
Name: <Christopher Hamilton, II>
<mean>.py

Problem: This program calculates rms, harmonic, and geometric means

Certification of Authenticity:
I certify that this is entirely my own work
"""


# 1. This program will calculate three different means: rms, harmonic, and geometric
# 2. Input: The quantity of numbers and their values.
#    Output: The rms, harmonic, and geometric means.
# 3. Ask for input: quantity of numbers
#    Loop equal to quantity of numbers: Ask for input: value of numbers
#    Calculate different means
#    Print results


import math


def main():
    quantity = int(input("Enter the values to be entered: "))
    acc = 0
    acc2 = 0
    acc3 = 1
    for _ in range(quantity):
        value = int(input("Enter value:"))
        acc = acc + value ** 2
        acc2 = acc2 + 1 / value
        acc3 = acc3 * value
    rms = round(math.sqrt(acc / quantity), 3)
    harmonic = round(quantity / acc2, 3)
    geometric = round(acc3 ** (1 / quantity), 3)
    print(rms)
    print(harmonic)
    print(geometric)


if __name__ == "__main__":
    main()
