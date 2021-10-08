"""
Name: <Christopher Hamilton, II>
<greeting>.py

Problem: This program animates a valentines greeting card

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


from graphics import GraphWin, Line, Point, Circle, Polygon, Text, update


def main():
    win = GraphWin("V-Day", 650, 650, autoflush=False)
    win.setCoords(0, 0, 10, 10)

    line_a = Line(Point(10, 9), Point(12, 11))
    line_a.setWidth(5)
    line_a.setArrow("first")
    line_a.draw(win)
    line_b = Line(Point(11.9, 11.5), Point(11.75, 10.8))
    line_b.setWidth(2)
    line_b.draw(win)
    line_c = Line(Point(12.5, 10.9), Point(11.75, 10.75))
    line_c.setWidth(2)
    line_c.draw(win)

    circle_a = Circle(Point(8, 6.5), 1.1)
    circle_a.setFill("maroon")
    circle_a.setOutline("maroon")
    circle_a.draw(win)

    circle_b = circle_a.clone()
    circle_b.move((-2), 0)
    circle_b.draw(win)

    triangle = Polygon(Point(7, 3.5), Point(9, 6.03), Point(5, 6.03))
    triangle.setFill("maroon")
    triangle.setOutline("maroon")
    triangle.draw(win)

    happy = Text(Point(2, 6), "Happy")
    happy.setSize(36)
    happy.setStyle("bold italic")
    happy.setTextColor("gold")
    happy.draw(win)

    valentines = Text(Point(2, 5), "Valentine's")
    valentines.setSize(36)
    valentines.setStyle("bold italic")
    valentines.setTextColor("gold")
    valentines.draw(win)

    for _ in range(9):
        line_a.move((-0.3), (-0.3))
        line_b.move((-0.3), (-0.3))
        line_c.move((-0.3), (-0.3))
        update(4)

    close = Text(Point(5, 2), "Click anywhere to close")
    close.draw(win)
    win.getMouse()
    win.close()


if __name__ == "__main__":
    main()
