"""
Name: Steve Ford
greeting.py

Certificate of Authenticity:
I certify that this assignment is entirely my own work.


~~~Pseudo Code~~~
Define Problem: we want a little animation to play of a heart being struck
by an arrow with some flavor text involved. Animation should be spiced up

I/O's: no inputs; program is hard coded animation
       outputs: graphical animation, described above
       outputs continued: I want a really smooth heart that beats, no gimmicks

Design: Find an easy to modify equation of a heart that will allow me
        re-write it in a way that it is expressed as y = x + some math
        rather than fixed radius = x + y

        replace coefficients to allow me to choose a nice looking heart from
        testing and generate two kinds of heart to cycle between, giving a
        "beating" visual

        I will have to actually separate the equation of the heart into
        two equations (total of 4 because its two hearts) as the equation
        of a "semi heart", I will do this in the same fashion as my pre-
        -calc class taught me to find the equation of a semi circle, as
        both are conical equations

        I will need to run many points (use a loop) through the semi-
        heart equation to receive enough output points to draw smooth
        curves, peaks, and valleys of the heart

        I will assemble all the output points into a list, then each
        semi heart lists will come together as one big list to feed
        into the graphic.polygon() parameter

Maintain: I decided the heart beat looks better if the heart slightly moves
          between it's two render options and also changes in color slightly

          Instead of typing out each point in the polygon of an arrow in a
          long boring wall of text I wrote a loop that automates the process
          and even allows for me to edit the scaling and certain features of
          the arrow, not user friendly, its all hard coded constants

          Arrow algo creeps up the shaft of the arrow which has a slope of
          y = x, approaches from 0,0 in a positive direction on both axis
          so if I take the point (x,x) and subtract a value(feather length)
          of just one of the values of the coordinate pair the resulting
          point is where the feather would extend to from the shaft (x,x)
          the loop reverts this and then does the opposite thanks to some
          modular arithmetic

          I played with the color of the background, arrow, and, text to
          make it seem more appealing

          I cut things around and made some variable global constants, even
          added a new function to close the program in order to fit the linter's
          requirements on the # of statements and variables

Note to the reader: the above pseudo code is a recreation of what I initially had;
                    which was messy and created issues with the test module due
                    to my own user error.

Maintain Cont: with what I now know from chapter 6 I definitely could create
               a new function for the semi circle math which re-occurs 4 times

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
