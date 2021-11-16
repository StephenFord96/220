"""
Name: Steve Ford
three_door_game.py

Certificate of Authenticity:
I certify that this assignment is entirely my own work.
"""

from random import randint
from graphics import (Rectangle, Point, GraphWin, Text)
from button import Button


def main():

    window = GraphWin("Three Door Game", 800, 800)
    top_instructions = Text(Point(400, 50), "I have a secret door")
    bottom_instructions = Text(Point(400, 750), "click to choose a door")

    button1 = Button(Rectangle(Point(150, 400), Point(250, 500)), "Door1")

    button2 = Button(Rectangle(Point(350, 400), Point(450, 500)), "Door2")

    button3 = Button(Rectangle(Point(550, 400), Point(650, 500)), "Door3")

    top_instructions.draw(window)
    bottom_instructions.draw(window)

    button1.draw(window)
    button2.draw(window)
    button3.draw(window)

    # initialize game data
    secret = randint(1, 3)

    # grabs user mouse input
    user_input = window.getMouse()

    # check if button 1 was clicked
    if button1.is_clicked(user_input):
        if secret == 1:
            button1.color_button("green")
            set_text(top_instructions, "You Win!", window)
        elif secret != 1:
            button1.color_button("red")
            set_text(top_instructions, "You Lost!", window)
            set_text(bottom_instructions, "Door" + str(secret) + " was my secret door", window)
        reset_game(window)

    # check if button 2 was clicked
    if button2.is_clicked(user_input):
        if secret == 2:
            button2.color_button("green")
            set_text(top_instructions, "You Win!", window)
        elif secret != 2:
            button2.color_button("red")
            set_text(top_instructions, "You Lost!", window)
            set_text(bottom_instructions, "Door" + str(secret) + " was my secret door", window)
        reset_game(window)

    # check if button 3 was clicked
    if button3.is_clicked(user_input):
        if secret == 3:
            button3.color_button("green")
            set_text(top_instructions, "You Win!", window)
        elif secret != 3:
            button3.color_button("red")
            set_text(top_instructions, "You Lost!", window)
            set_text(bottom_instructions, "Door" + str(secret) + " was my secret door", window)
        reset_game(window)


def set_text(text, msg, window):
    text.undraw()
    text.setText(msg)
    text.draw(window)


def reset_game(window):
    window.getMouse()
    window.close()
    main()


if __name__ == "__main__":
    main()
