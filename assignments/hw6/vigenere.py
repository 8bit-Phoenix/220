"""
Name: <Christopher Hamilton, II>
<vigenere>.py

Problem: This program creates an encoded message from inputs

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


from graphics import *


def code(message, keyword):
    message = message.replace(" ", "")
    message = message.upper()
    keyword = keyword.upper()
    acc = ""
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(message)):
        m = ord(message[i]) - 65
        i_loop = i % len(keyword)
        k = ord(keyword[i_loop]) - 65
        abc_index = (m + k) % 26
        letter = abc[abc_index]
        acc = acc + letter
    return acc


def draw_text(point, text, win):
    printer = Text(point, text)
    printer.setTextColor("White")
    printer.draw(win)
    return printer


def main():
    win = GraphWin("Vigenere", 650, 650)
    win.setBackground("pink")
    win.setCoords(0, 0, 10, 10)

    draw_text(Point(2, 8), "Message to code", win)
    draw_text(Point(2, 7), "Enter Keyword", win)

    message_entry = Entry(Point(6, 8), 35)
    keyword_entry = Entry(Point(5, 7), 20)
    message_entry.draw(win)
    keyword_entry.draw(win)

    encode_box = Rectangle(Point(4, 4), Point(6, 6))
    encode_box.draw(win)
    encode_text = draw_text(Point(5, 5), "Encode", win)

    fake = 0
    while fake == 0:
        idk = win.getMouse()
        got_it = idk.getX()
        it_got = idk.getY()
        if 4 <= got_it <= 6 and 4 <= it_got <= 6:
            fake = 1

    message = message_entry.getText()
    keyword = keyword_entry.getText()
    encode_box.undraw()
    encode_text.undraw()
    encryption = code(message, keyword)

    draw_text(Point(5, 5), "Resulting Message", win)
    draw_text(Point(5, 4), encryption, win)

    draw_text(Point(5, 1), "Click anywhere to close", win)
    win.getMouse()
    win.close()


if __name__ == "__main__":
    main()
