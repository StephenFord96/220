"""
Name: Steve Ford
bumper.py

Certificate of Authenticity:
I certify that this assignment is entirely my own work.

Pseudo Code:

define problem: we want to create a physics simulation of bumper cars colliding

Inputs: The program needs to be aware of the circle's position at all times

        The program needs to be able to measure circle's position to screen edges
        and other circle's position ==> use a^2 + b^2 = c^2

Outputs: Program needs to be able to output move orders in a radial fashion on
         a 2d plane

         program needs to have random speeds for bumpers

         program needs to be able to invert direction of bumpers

Design: setup an indefinite while loop which checks to see if the distance of each
        circle's center is less than the screens edges (0,0 getX, getY) or the center
        of the other circle

        if it is invert direction of said circle

        direction should be handled like slope on a 2d graph x/y relation

        Randomly generated x and y speeds come together as initial velocity

        All further velocities play off inversion of that initial velocity
        since just a simple x/y relation

Maintain: I decided to make the circle's also grab a new random color when
          they have trigger a collision

"""

import math
from random import randint
from time import sleep
from graphics import (GraphWin, Circle, Point, color_rgb)

RUNNING = True


def main():
    game_window = GraphWin("Bumper Cars", randint(300, 900), randint(300, 900))
    game_window.setBackground(get_random_color())

    bumper1 = Circle(Point(100, 100), 25)
    bumper1.setFill(get_random_color())
    bumper1.setOutline(get_random_color())
    bumper1_x_speed = get_random(10)
    bumper1_y_speed = get_random(10)
    bumper1.draw(game_window)

    bumper2 = Circle(Point(274, 274), 25)
    bumper2.setFill(get_random_color())
    bumper2.setOutline(get_random_color())
    bumper2_x_speed = get_random(15)
    bumper2_y_speed = get_random(15)
    bumper2.draw(game_window)

    while RUNNING:
        bumper1.move(bumper1_x_speed, bumper1_y_speed)
        bumper2.move(bumper2_x_speed, bumper2_y_speed)
        if did_collide(bumper1, bumper2):
            bumper1_x_speed *= -1
            bumper1_y_speed *= -1
            bumper2_x_speed *= -1
            bumper2_y_speed *= -1
            bumper1.setFill(get_random_color())
            bumper2.setFill(get_random_color())
        if hit_horizontal(bumper1, game_window):
            bumper1_y_speed *= -1
            bumper1.setFill(get_random_color())
        if hit_horizontal(bumper2, game_window):
            bumper2_y_speed *= -1
            bumper2.setFill(get_random_color())
        if hit_vertical(bumper1, game_window):
            bumper1_x_speed *= -1
            bumper1.setFill(get_random_color())
        if hit_vertical(bumper2, game_window):
            bumper2_x_speed *= -1
            bumper2.setFill(get_random_color())

        sleep(0.03)

    game_window.getMouse()


def get_random(max_velocity):
    return randint(-1 * max_velocity, max_velocity)


def did_collide(ball1, ball2):
    radius = ball1.getRadius()
    center1 = ball1.getCenter()
    center2 = ball2.getCenter()
    first_x = center1.getX()
    first_y = center1.getY()
    second_x = center2.getX()
    second_y = center2.getY()
    distance = math.sqrt((abs(second_x - first_x)) ** 2 + (abs(second_y - first_y)) ** 2)
    return distance <= radius * 2


def hit_vertical(ball, window):
    radius = ball.getRadius()
    center = ball.getCenter()
    ball_x_position = center.getX()
    _x_left = radius
    _x_right = window.getWidth() - radius
    return ball_x_position <= _x_left or ball_x_position >= _x_right


def hit_horizontal(ball, window):
    radius = ball.getRadius()
    center = ball.getCenter()
    ball_y_position = center.getY()
    _y_left = radius
    _y_right = window.getHeight() - radius
    return ball_y_position <= _y_left or ball_y_position >= _y_right


def get_random_color():
    colors = []
    for _ in range(3):
        colors.append(randint(0, 255))
    return color_rgb(colors[0], colors[1], colors[2])


if __name__ == "__main__":
    main()
