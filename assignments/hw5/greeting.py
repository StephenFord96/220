"""
Name: Steve Ford
greeting.py

Certificate of Authenticity:
I certify that this assignment is entirely my own work.
"""

import math
import time
from graphics import (Point, Polygon, GraphWin, Text)

win = GraphWin("Valentines Card", 700, 700)
win.setBackground("Light Grey")

first_message = Text(Point(350, 50), "Happy Valentines Day!")
first_message.setFill("Magenta")
first_message.setSize(18)
first_message.draw(win)

RADIUS = 1600
LOWER_BOUND = int(RADIUS / 4 * -1)
UPPER_BOUND = int(RADIUS / 4)

X_ORIGIN = 350
Y_ORIGIN = 300

TAPER_RATING = 5
TAPER_RATING_2 = 4

VALLEY_RATING = -1.5
PEAK_RATING = 0.75

FIRST_HEART_STRUCTURE = []
SECOND_HEART_STRUCTURE = []

ARROW_SIZE_GENERAL = 1

FEATHER_RATING = 10 * ARROW_SIZE_GENERAL
ARROW_LENGTH = 45 * ARROW_SIZE_GENERAL
FEATHER_SPACING = 3 * ARROW_SIZE_GENERAL
ARROW_BLUEPRINT = [Point(0, 0), Point(ARROW_LENGTH, ARROW_LENGTH)]


def main():

    for shaft_pos in range(int(FEATHER_RATING / 2), int(ARROW_LENGTH / 3), int(FEATHER_SPACING)):
        for i in range(2):
            position = Point(shaft_pos, shaft_pos)
            ARROW_BLUEPRINT.append(position)
            feather_y = FEATHER_RATING * ((i-1) % 2)
            feather_x = FEATHER_RATING * (i % 2)
            arrow_point = Point(position.getX() - feather_x, position.getY() - feather_y)
            ARROW_BLUEPRINT.append(arrow_point)
            ARROW_BLUEPRINT.append(position)

    arrow = Polygon(ARROW_BLUEPRINT)

    # start of base heart construction
    # bottom half of heart
    for i in range(UPPER_BOUND, LOWER_BOUND, -1):
        x_input = i/10

        y_output = VALLEY_RATING * (math.sqrt(RADIUS - (x_input ** 2)))
        y_output = y_output + (math.sqrt(abs(x_input))) * (TAPER_RATING + 1)
        y_output = y_output * (-1)

        FIRST_HEART_STRUCTURE.append(Point(x_input + X_ORIGIN, y_output + Y_ORIGIN))

    print("test bottom half")

    # top half od heart
    for i in range(LOWER_BOUND, UPPER_BOUND):
        x_input = i/10

        y_output = PEAK_RATING * (math.sqrt(RADIUS - (x_input ** 2)))
        y_output = y_output + (math.sqrt(abs(x_input))) * TAPER_RATING
        y_output = y_output * (-1)

        FIRST_HEART_STRUCTURE.append(Point(x_input + X_ORIGIN, y_output + Y_ORIGIN))

    print("test top half")

    # start of ghost heart construction
    # bottom half of heart
    for i in range(UPPER_BOUND, LOWER_BOUND, -1):
        x_input = i/10

        y_output = VALLEY_RATING * (math.sqrt(RADIUS - (x_input ** 2)))
        y_output = y_output + (math.sqrt(abs(x_input))) * (TAPER_RATING_2 + 1)
        y_output = y_output * (-1)

        SECOND_HEART_STRUCTURE.append(Point(x_input + X_ORIGIN, y_output + Y_ORIGIN))

    # top half of heart
    for i in range(LOWER_BOUND, UPPER_BOUND):
        x_input = i/10

        y_output = (PEAK_RATING + 0.10) * (math.sqrt(RADIUS - (x_input ** 2)))
        y_output = y_output + (math.sqrt(abs(x_input))) * TAPER_RATING_2
        y_output = y_output * (-1)

        SECOND_HEART_STRUCTURE.append(Point(x_input + X_ORIGIN, y_output + Y_ORIGIN))

    # shape assignments
    heart_ghost = Polygon(SECOND_HEART_STRUCTURE)
    heart_ghost.setFill("red")

    heart = Polygon(FIRST_HEART_STRUCTURE)
    heart.setFill("pink")
    heart.draw(win)

    # heart throbbing & action loop!
    for _ in range(7):
        time.sleep(.25)
        heart.undraw()
        heart_ghost.draw(win)
        heart_ghost.move(2, 3)
        time.sleep(.75)
        heart_ghost.undraw()
        heart_ghost.move(-2, -3)
        heart.draw(win)

    arrow.draw(win)
    for _ in range(88):
        arrow.move(3, 2.5)
        time.sleep(0.015)

    finish()


def finish():

    first_message.undraw()

    instructions = Text(Point(350, 650), "Click anywhere to close the window!")
    instructions.setFill("Magenta")
    instructions.setSize(18)
    instructions.draw(win)

    win.getMouse()
    win.close()


if __name__ == "__main__":
    main()
