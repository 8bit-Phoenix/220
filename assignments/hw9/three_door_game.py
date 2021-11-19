"""
Name: <Christopher Hamilton, II>
<three_door_game>.py

Problem: This program simulates a three door game

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from random import randint
from graphics import GraphWin, Point, Rectangle, Text
from button import Button


def main():
    win = GraphWin("Game_Boy", 670, 545)
    win.setCoords(0, 0, 100, 100)
    t_text = draw_text("I have a secret door", Point(50, 85), win)
    b_text = draw_text("Click to choose my door", Point(50, 15), win)

    d_1 = draw_button(Point(20, 55), Point(33.3, 45), "Door_1", win)
    d_2 = draw_button(Point(43.3, 55), Point(56.6, 45), "Door_2", win)
    d_3 = draw_button(Point(66.6, 55), Point(80, 45), "Door_3", win)
    num = randint(1, 3)
    c_d = 0
    while c_d == 0:
        click = win.getMouse()
        if d_1.is_clicked(click):
            c_d = 1
            pick_door = d_1
        elif d_2.is_clicked(click):
            c_d = 2
            pick_door = d_2
        elif d_3.is_clicked(click):
            c_d = 3
            pick_door = d_3
    if click == num:
        pick_door.color_button("lime")
        t_text.setText("The Bingo Women is you!!!")
    else:
        pick_door.color_button("crimson")
        t_text.setText("Enter Sans quote")
        draw_text("Um actually it was door{0}".format(num), Point(50, 75), win)
    b_text.setText("Click anywhere to close")
    win.getMouse()
    win.close()


def draw_text(message, point, win):
    text = Text(point, message)
    text.draw(win)
    return text


def draw_button(p_1, p_2, label, win):
    rectangle = Rectangle(p_1, p_2)
    button = Button(rectangle, label)
    button.draw(win)
    return button


if __name__ == "__main__":
    main()
