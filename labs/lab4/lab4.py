"""
Name: Steve Ford
Lab4.py
"""

from graphics import *
import math


def squares():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move a square")
    instructions.draw(win)

    # builds a circle
    shape = Rectangle(Point(50, 50), Point(70, 70))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        p = win.getMouse()
        shape = Rectangle(Point(p.getX() - 10, p.getY() - 10), Point(p.getX() + 10, p.getY() + 10))
        shape.setOutline("red")
        shape.setFill("red")
        shape.draw(win)

    instructions.undraw()
    instructions.setText("Click to close")
    instructions.draw(win)
    win.getMouse()
    win.close()


def rectangle():
    """
    This program displays information about a rectangle drawn by the user.
    Input: Two mouse clicks for the opposite corners of a rectangle.
    Output: Draw the rectangle.
         Print the perimeter and area of the rectangle.
    Formulas: area = (length)(width)   and    perimeter = 2(length+width)
    """
    height = 400
    width = 400
    win = GraphWin("Rectangle", width, height)
    p1 = win.getMouse()
    p2 = win.getMouse()
    r = Rectangle(p1, p2)
    r.draw(win)
    text_anchor = Point(width / 2, height - 10)
    text_anchor2 = Point(width / 2, height - 30)
    text_anchor3 = Point(width / 2, height - 50)

    width = abs(p1.getX() - p2.getX())
    height = abs(p1.getY() - p2.getY())
    rect_perimeter = Text(text_anchor, "Perimeter of rectangle is: " + str(width*2 + height*2))
    rect_perimeter.draw(win)
    rect_area = Text(text_anchor2, "Area of Rectangle is: " + str(width*height))
    rect_area.draw(win)
    instructions = Text(text_anchor3, "Click to close window")
    instructions.draw(win)

    win.getMouse()
    win.close()


def circle():
    # setting up window
    width = 400
    height = 400
    win = GraphWin("Circle", width, height)

    # setting up UI
    text_anchor = Point(width/2, height - 10)
    instructions = Text(text_anchor, "Click for circle center")
    instructions.draw(win)

    # user input
    circle_center = win.getMouse()

    # UI cycled
    instructions.undraw()
    instructions = Text(text_anchor, "Click for circle radius")
    instructions.draw(win)

    # user input
    p_radial = win.getMouse()

    # assignment for convenience
    center_x = circle_center.getX()
    center_y = circle_center.getY()
    point_x = p_radial.getX()
    point_y = p_radial.getY()

    # computation
    radius = ((center_x - point_x)**2 + (center_y - point_y)**2)**(1/2)
    user_circle = Circle(circle_center, radius)
    user_circle.draw(win)

    # UI cycled
    instructions.undraw()
    instructions = Text(text_anchor, "The radius is: " + str(round(radius, 3)) + "...Click to close the window!")
    instructions.draw(win)

    win.getMouse()
    win.close()


def pi2():
    n = int(input("How many refinements will be made? "))

    accumulator = 0
    for i in range(0, n):
        sign = (i % 2)
        sign = (sign * 2) - 1
        sign = sign * (-1)
        denominator = i * 2 + 1

        fraction = 4/denominator

        accumulator = accumulator + (sign * fraction)

    print(accumulator)
    accuracy = math.pi - accumulator
    print("Calculation is " + str(accuracy) + " away from Pi")


def main():
    squares()
    rectangle()
    circle()
    pi2()


main()
