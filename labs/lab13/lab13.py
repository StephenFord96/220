"""
Name: Stephen Ford
Lab13.py
"""

from graphics import Rectangle, Point


def iib(search, values):
    mid = len(values)//2
    if values[mid] == search:
        return True
    while values[mid] != search or len(values) != 1:
        print("length is " + str(len(values)))
        print("mid pos " + str(mid))
        print("middle value " + str(values[mid]))
        print("remaining is " + str(values))
        if values[mid] == search:
            return True
        if values[mid] < search:
            values = values[mid + 1:]
        else:
            values = values[:mid]
        mid = len(values)//2
    if values[0] == search:
        return True
    print(values[0])
    print(len(values))
    return False


def selection_sort(values):

    # initialize new values
    # initialize new values
    new_values = []
    while len(values) > 0:
        # assume first value is lowest
        lowest = values[0]
        pos = 0

        for i in range(len(values)):
            if values[i] < lowest:
                lowest = values[i]
                pos = i
        new_values.append(values.pop(pos))
    return new_values


def rect_sort(rectangles):
    areas = []
    d = {}
    for rect in rectangles:
        d[get_area(rect)] = rect
    for rect in rectangles:
        areas.append(get_area(rect))
    areas = selection_sort(areas)
    print(areas)
    for i in range(len(areas)):
        rectangles[i] = d[areas[i]]
    print(rectangles)


def get_area(shape):
    width = abs(shape.getP1().getX() - shape.getP2().getX())
    height = abs(shape.getP1().getY() - shape.getP2().getY())
    return width * height


def trade_alert(filename):
    infile = open(filename, "r")
    data = infile.read().split()
    for i in range(len(data)):
        data[i] = int(data[i])
    for i in range(len(data)):
        if data[i] >= 500 and data[i] < 830:
            print("warning, traffic is " + str(data[i]))
        if data[i] >= 830:
            print("ALERT, traffic is " + str(data[i]))


def main():

    rect1 = Rectangle(Point(1, 1), Point(2, 2))
    rect2 = Rectangle(Point(1, 1), Point(3, 3))
    rect3 = Rectangle(Point(1, 1), Point(-1, -1))
    rect4 = Rectangle(Point(1, 1), Point(0, 0))
    rect5 = Rectangle(Point(1, 1), Point(5, 5))

    my_rectangles = [rect1, rect2, rect3, rect4, rect5]

    my_search = 6
    my_list = [3, 4, 5, 10]

    print(iib(my_search, my_list))
    # print(selection_sort(my_list))
    # print(rect_sort(my_rectangles))
    # print(trade_alert("trades.txt"))


main()
