"""
Name: Steve Ford
lab5.py
"""

import math
from graphics import *


def target():
    win_width = 500
    win_height = 500
    win = GraphWin("Archery Target", win_width, win_height)

    radius = win_width / 10
    center = Point(win_width/2, win_height/2)

    colors = ["white", "black", "blue", "red", "yellow"]

    for i in range(5, 0, -1):
        circle = Circle(center, radius * i)
        circle.setFill(colors[i - 1])
        circle.draw(win)

    # Wait for another click to exit
    win.getMouse()
    win.close()


def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)

    p1 = win.getMouse()
    p2 = win.getMouse()
    p3 = win.getMouse()

    my_triangle = Polygon(p1, p2, p3)
    my_triangle.draw(win)

    d1_x = abs(p2.getX()-p1.getX())
    d1_y = abs(p2.getY()-p1.getY())
    d1 = math.sqrt(d1_x**2 + d1_y**2)

    d2_x = abs(p3.getX()-p1.getX())
    d2_y = abs(p3.getY()-p1.getY())
    d2 = math.sqrt(d2_x**2 + d2_y**2)

    d3_x = abs(p2.getX()-p3.getX())
    d3_y = abs(p2.getY()-p3.getY())
    d3 = math.sqrt(d3_x**2 + d3_y**2)

    perimeter_gui = Text(Point(250, 450), "The Perimeter is: " + str(round(d1+d2+d3, 2)))
    perimeter_gui.draw(win)

    s = (d1 + d2 + d3)/2
    area = math.sqrt(s * (s - d1) * (s - d2) * (s - d3))

    area_gui = Text(Point(250, 400), "The area is: " + str(round(area, 2)))
    area_gui.draw(win)

    instructions = Text(Point(250, 50), "Click to close window")
    instructions.draw(win)

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
    red_input = Entry(Point((win_width / 2 + 10), (win_height / 2 + 40)), 5)
    red_input.draw(win)

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")
    green_input = Entry(Point((win_width / 2 + 10), (win_height / 2 + 70)), 5)
    green_input.draw(win)

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")
    blue_input = Entry(Point((win_width / 2 + 10), (win_height / 2 + 100)), 5)
    blue_input.draw(win)

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    for i in range(5):

        instructions = Text(Point(win_width/2, 50), "You can change the circle " + str(5-i) + " more times")
        instructions.draw(win)

        win.getMouse()

        instructions.undraw()

        red = eval(red_input.getText())
        green = eval(green_input.getText())
        blue = eval(blue_input.getText())

        shape.setFill(color_rgb(red, green, blue))

    # Wait for another click to exit
    win.getMouse()
    win.close()


def process_string():
    msg = str(input("What string do you want to modify? "))
    length = len(msg)

    # first character
    print(msg[0])

    # last character
    print(msg[length - 1])

    # characters inclusively 2-5
    print(msg[2:6])

    # concatenation of first and last
    print(msg[0] + msg[length - 1])

    # first 3 characters repeated 10 times
    for _ in range(10):
        print(msg[0:3], end="")
    print()

    # each character printed per line once at a time
    for letter in msg:
        print(letter)

    # lengths of message
    print(length)


def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]

    # "hi there"
    data = values[1] + values[3]
    print(data)

    # sum of 5 and 2.5
    data = values[0] + values[2]
    print(data)

    # print hi 5 times
    for _ in range(5):
        data = values[1]
        print(data, end="")
    print()

    # new list 2.5, "there", pt
    data = [values[2], values[3], values[4]]
    print(data)

    # new list: 2.5, "there", 5
    data = [values[2], values[3], values[0]]
    print(data)

    # new list: 2.5, 5, 7.2
    data = [values[2], values[0], float(values[5])]
    print(data)

    # sum of 5 + 2.5 + 7.2
    data = float(values[0]) + float(values[2]) + float(values[5])
    print(data)

    # number of items in values
    data = len(values)
    print(data)


def another_series():
    terms = int(input("How many terms do you want? "))

    acc = 0
    for i in range(terms):
        num = (2 + (2 * (i % 3)))
        print(num)
        acc += num
    print(acc)


def main():
    target()
    triangle()
    color_shape()
    process_string()
    process_list()
    another_series()
    pass


main()
