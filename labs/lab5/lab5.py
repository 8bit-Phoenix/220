"""
Name: <Christopher Hamilton, II>
<lab5>.py
"""

from graphics import *
import math

def target():
    win_width = 500
    win_height = 500
    win = GraphWin("Archery Target", win_width, win_height)

    # Add code here to get the dimensions and draw the target

    # Wait for another click to exit
    win.getMouse()
    win.close()


def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)

    # Add code here to accept the mouse clicks, draw the triangle.
    point1 = win.getMouse()
    point2 = win.getMouse()
    point3 = win.getMouse()
    l1 = Line(point1, point2)
    l2 = Line(point2, point3)
    l3 = Line(point3, point1)
    l1.draw(win)
    l2.draw(win)
    l3.draw(win)
    # and display its area in the graphics window.
    line1 = math.sqrt((point1.getX() - point2.getX() ** 2 + (point1.getY() - point2.getY()) ** 2))
    line2 = math.sqrt((point2.getX() - point3.getX() ** 2 + (point2.getY() - point3.getY()) ** 2))
    line3 = math.sqrt((point3.getX() - point1.getX() ** 2 + (point3.getY() - point1.getY()) ** 2))
    perimeter = line1 + line2 + line3
    x = perimeter / 2
    area = math.sqrt(x * (x - line1) * (x - line2) * (x - line3))
    perimeter_text = Text(Point(250, 400), "The perimeter is: " + str(perimeter))
    area_text = Text(Point(250, 425), "The area is: " + str(area))
    perimeter_text.draw(win)
    area_text.draw(win)
    # Wait for another click to exit
    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")
    red_box = Entry(Point(210, 240), 3)

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")
    green_box = Entry(Point(210, 270), 3)

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")
    blue_box = Entry(Point(210, 300), 3)

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)
    red_box.draw(win)
    green_box.draw(win)
    blue_box.draw(win)

    # Change color
    for c in range(5):
        win.getMouse()
        red = int(red_box.getText())
        green = int(green_box.getText())
        blue = int(blue_box.getText())
        shape.setFill(color_rgb(red, green, blue))

        # Wait for another click to exit
    win.getMouse()
    win.close()


def process_string():
    string = eval(input("Enter the string: "))
    print (string[-1])
    print (string[2-6])
    print (string[0] + string[-1])
    print (string[0-3] * 10)
    for i in string:
        print (i)


def process_list():
    pt = Point(5, 18)
    values = (5, "hi", 2.5, "there", pt, "7.2")
    x = values[1] + values[3]
    print(x)
    x = values[0] + values[2]
    print(x)
    x = values[1] * 5
    print(x)
    x = values[2-5]
    print(x)
    x = values
    print(x)
    x = values[0] + values[2] + float(values[2])
    print(x)
    x = len(values)
    print(x)


def another_series():
    c = eval(input("Enter number of terms: "))
    acc = 0
    for i in range(c):
        y = 2 + (2 * (i % 3))
        print(y, end=" ")
        acc = acc + y
    print(" ")
    print(acc)



def main():
    # target()
    triangle()
    color_shape()
    process_string()
    process_list()
    another_series()

main()
