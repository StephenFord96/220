"""
Name: Steve Ford
greeting.py

Certificate of Authenticity:
I certify that this assignment is entirely my own work.
"""

import math
from graphics import *
import time

win = GraphWin("Valentines Card", 700, 700)


def main():

    radius = 1600
    lower_bound = int(radius/4 * -1)
    upper_bound = int(radius/4)

    x_origin = 350
    y_origin = 300

    taper_rating = 5
    taper_rating_2 = 4

    valley_rating = -1.5
    peak_rating = 0.75

    first_heart_structure = []
    second_heart_structure = []

    """
    ~~~~arrow feather algorithm~~~~
    
    shaft = graph x value which intercepts shaft, default 5
    feather length = amount to be subtracted from shaft, default 5
    
    new point is based off of shaft since arrow is x=y
    
    use i in loop to modulate 2 giving 0 1 0 1 0 1 pattern after subtracting 1
    offset sequence for y and x so one is being negated at a time
    
    each feather length x and y is multiplied by either 1 or 0 
    in body of loop subtract feather length from shaft.x shaft.y
    
    new point is appended to arrow list
    add feather length back to shaft to reset for other side of arrow
    
    this loop is reset and rerun but with a different shaft rating which--
    --is pulled from an outer loop's i
    
    
    """

    arrow_size_general = 1

    feather_rating = 10 * arrow_size_general
    arrow_length = 45 * arrow_size_general
    feather_spacing = 3 * arrow_size_general
    arrow_blueprint = []
    arrow_blueprint.append(Point(0, 0))
    arrow_blueprint.append(Point(arrow_length, arrow_length))

    for s in range(int(feather_rating/2), int(arrow_length/3), int(feather_spacing)):
        for i in range(2):
            position = Point(s, s)
            arrow_blueprint.append(position)
            mod_x = i % 2
            mod_y = (i-1) % 2
            feather_y = feather_rating * mod_y
            feather_x = feather_rating * mod_x
            arrow_point = Point(position.getX() - feather_x, position.getY() - feather_y)
            arrow_blueprint.append(arrow_point)
            arrow_blueprint.append(position)

    arrow = Polygon(arrow_blueprint)
    arrow.setOutline("grey")
    arrow.draw(win)

    # start of base heart construction
    # bottom half of heart
    for i in range(upper_bound, lower_bound, -1):
        x_input = i/10
        y_output = (valley_rating * (math.sqrt(radius - (x_input**2))) + (math.sqrt(abs(x_input))) * (taper_rating + 1)) * (-1)

        new_point = Point(x_input + x_origin, y_output + y_origin)
        # new_point.draw(win)
        first_heart_structure.append(new_point)

    print("test bottom half")

    # top half od heart
    for i in range(lower_bound, upper_bound):
        x_input = i/10
        y_output = (peak_rating * (math.sqrt(radius - (x_input**2))) + (math.sqrt(abs(x_input)) * taper_rating)) * (-1)

        new_point = Point(x_input + x_origin, y_output + y_origin)
        # new_point.draw(win)
        first_heart_structure.append(new_point)

    print("test top half")

    # start of ghost heart construction
    # bottom half of heart
    for i in range(upper_bound, lower_bound, -1):
        x_input = i/10
        y_output = (valley_rating * (math.sqrt(radius - (x_input**2))) + (math.sqrt(abs(x_input))) * (taper_rating_2 + 1)) * (-1)

        new_point = Point(x_input + x_origin, y_output + y_origin)
        second_heart_structure.append(new_point)

    # top half of heart
    for i in range(lower_bound, upper_bound):
        x_input = i/10
        y_output = ((peak_rating + 0.10) * (math.sqrt(radius - (x_input**2))) + (math.sqrt(abs(x_input)) * taper_rating_2)) * (-1)

        new_point = Point(x_input + x_origin, y_output + y_origin)
        second_heart_structure.append(new_point)

    # shape assignments
    heart_ghost = Polygon(second_heart_structure)
    heart_ghost.setFill("red")

    heart = Polygon(first_heart_structure)
    heart.setFill("pink")
    heart.draw(win)

    # heart throbbing & action loop!
    for _ in range(16):
        time.sleep(.25)
        arrow.move(2, 3)
        heart.undraw()
        heart_ghost.draw(win)
        heart_ghost.move(2, 3)
        time.sleep(.75)
        heart_ghost.undraw()
        heart_ghost.move(-2, -3)
        heart.draw(win)
        arrow.move(15, 12)


    # closing section
    win.getMouse()
    win.close()


if __name__ == "__main__":
    main()
