"""
Name: <Christopher Hamilton, II>
<bumper>.py

Problem: This program simulates bumper cars

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import math
from random import randint
from graphics import *


def main():
    win = GraphWin("Bumper", 500, 500, autoflush=False)
    circle = Circle(Point(randint(30, 470), randint(30, 470)), 30)
    circle.setFill(get_random_color())
    circle.draw(win)
    circle2 = Circle(Point(randint(30, 470), randint(30, 470)), 30)
    circle2.setFill(get_random_color())
    circle2.draw(win)
    x_move = get_random(30)
    y_move = get_random(30)
    a_move = get_random(30)
    b_move = get_random(30)
    fake = 0
    while fake == 0:
        circle.move(x_move, y_move)
        circle2.move(a_move, b_move)
        if hit_vertical(circle, win) or did_collide(circle, circle2):
            x_move = -x_move
        if hit_vertical(circle2, win) or did_collide(circle, circle2):
            a_move = -a_move
        if hit_horizontal(circle, win) or did_collide(circle, circle2):
            y_move = -y_move
        if hit_horizontal(circle2, win) or did_collide(circle, circle2):
            b_move = -b_move
        update(4)
        if win.checkMouse():
            break
    win.close()


def get_random(move_amount):
    num = randint(-move_amount, move_amount)
    return num


def get_random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = color_rgb(r, g, b)
    return color


def hit_horizontal(circle, win):
    center = circle.getCenter()
    radius = circle.getRadius()
    top_dist = math.sqrt((center.getY() - 0) ** 2)
    bottom_dist = math.sqrt((center.getY() - win.getHeight()) ** 2)
    return top_dist <= radius or bottom_dist <= radius


def hit_vertical(circle, win):
    center = circle.getCenter()
    radius = circle.getRadius()
    left_dist = math.sqrt((center.getX() - 0) ** 2)
    right_dist = math.sqrt((center.getX() - win.getWidth()) ** 2)
    return left_dist <= radius or right_dist <= radius


def did_collide(circle1, circle2):
    center1 = circle1.getCenter()
    center2 = circle2.getCenter()
    dist = math.sqrt((center1.getX() - center2.getX()) ** 2 + (center1.getY() - center2.getY()) ** 2)
    return dist <= (circle1.getRadius() + circle2.getRadius())


if __name__ == "__main__":
    main()
