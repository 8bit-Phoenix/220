"""
Name: <Christopher Hamilton, II>
<lab9>.py
"""


import math
from graphics import GraphWin, Line, Point, Circle, Polygon, Text, update


def addTen(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10


def sqaureEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2


def sumList(nums):
    acc = 0
    for i in range(len(nums)):
        acc += nums[i]
    return acc


def toNumbers(strlist):
    for i in range(len(strlist)):
        strlist[i] = float(strlist[i])


def writeSumOfSquares():
    infile = input("Enter file name")
    outfile = input("Enter File name")
    readfile = open(infile, "r")
    writefile = open(outfile, "w")
    for line in readfile:
        nums = line.split()
        toNumbers(nums)
        sqaureEach(nums)
        add = sumList(nums)
        writefile.write("sum of sqaures = " + str(add))
    readfile.close()
    outfile.close()


def starter():
    weight = float(input("Enter player weight: "))
    wins = int(input("Enter the number of wins: "))
    if 150 <= weight < 160 and wins >= 5:
        print("This player should start")
    elif weight > 199 and wins > 20:
        print("This player should start")
    else:
        print("This player should not start")


def leapYear(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def circleOverlap():
    win = GraphWin("Circle Shit", 400, 400)
    p1 = win.getMouse()
    p2 = win.getMouse()
    r = math.sqrt((p1.getX() - p2.getX()) ** 2 + (p1.getY() - p2.getY()) ** 2)
    c1 = Circle(p1, r)
    c1.draw(win)
    p3 = win.getMouse()
    p4 = win.getMouse()
    r2 = math.sqrt((p3.getX() - p4.getX()) ** 2 + (p3.getY() - p4.getY()) ** 2)
    c2 = Circle(p3, r2)
    c2.draw(win)
    distance = math.sqrt((p1.getX() - p3.getX()) ** 2 + (p1.getY() - p3.getY()) ** 2)
    if distance <= r + r2:
        text = Text(Point(200, 200), "The circles overlap")
    else:
        text = Text(Point(200, 200), "The circles do not overlap")
    text.draw(win)

    win.getMouse()
    win.close()


def main():
    starter()
    year = int(input("Enter a year: "))
    leap = leapYear(year)
    if leap:
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")
    circleOverlap()
    # add other function calls here
    pass


main()
