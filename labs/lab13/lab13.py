"""
Name: <Christopher Hamilton, II>
<lab13>.py
"""


from graphics import Rectangle, Point


def is_in_binary(search_val, values):
    mid = len(values) // 2
    while values[mid] != search_val and len(values) != 1:
        if values[mid] > search_val:
            values = values[:mid]
        else:
            values = values[mid:]
        mid = len(values) // 2
    if len(values) == 1 and values[0] != search_val:
        return False
    else:
        return True


def selection_sort(values):
    for i in range(0, len(values)):
        lowest = values[1]
        position = i
        for j in range(i + 1, len(values)):
            if values[j] < lowest:
                lowest = values[j]
                position = j
        values[i], values[position] = values[position], values[i]


def calc_area(rect):
    p1 = rect.getP1()
    p2 = rect.getP2()
    dx = abs(p1.getX() - p2.getX())
    dy = abs(p1.getY() - p2.getY())
    return dx * dy


def rect_sort(rectangles):
    d = {}
    a = []
    for rect in rectangles:
        d[calc_area(rect)] = rect
        a.append(calc_area(rect))
    selection_sort(a)
    for i in range(0, len(a)):
        rectangles[i] = d[a[i]]
    print(rectangles)


def star_find(filename):
    file = open(filename, "r")
    s = file.read().split()
    found = []
    for i in s:
        if 4000 <= int(i) <= -5000:
            found.append(i)
        if len(found) <= 5:
            last = i
            break
        if len(found) < 5:
            print("Five signals could not be found")
        print("Ay look we found {0} signals ".format(len(found)))
        print("This signal power lvl is: {0}".format(found))
        print("WOOOO YA BABY WE DID IT and it only took {0} searches".format(last))


def main():
    print(is_in_binary(1, [1, 2 , 3, 4, 5, 6, 7, 8, 9, 10]))
    print(is_in_binary(11, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    selection_sort([100, 39, 48, 275, 2, 588, 42])
    rect1 = Rectangle(Point(10, 10), Point(3, 3))
    rect2 = Rectangle(Point(10, 10), Point(9, 2))
    rect3 = Rectangle(Point(10, 10), Point(10, 7))
    rectangles = [rect2, rect1, rect3]
    rect_sort(rectangles)
    star_find("signals.txt")
    pass


main()
