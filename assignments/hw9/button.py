"""
Name: <Christopher Hamilton, II>
<button>.py

Problem: This program simulates a button

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


from graphics import Text


class Button:
    """
    Creates an interactive button on a graphical window
    """
    def __init__(self, shape, label):
        self.shape = shape
        center = self.shape.getCenter()
        self.text = Text(center, label)

    def get_label(self):
        return self.text.getText()

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        p1_shape = self.shape.getP1()
        p2_shape = self.shape.getP2()
        p_x = point.getX()
        p_y = point.getY()
        p1_x = p1_shape.getX()
        p1_y = p1_shape.getY()
        p2_x = p2_shape.getX()
        p2_y = p2_shape.getY()
        return p1_x <= p_x <= p2_x and p1_y <= p_y <= p2_y

    def color_button(self, color):
        self.shape.setFill(color)

    def set_label(self, label):
        self.text.setText(label)
