"""
Name: Steve Ford
button.py

Certificate of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import (Text)


class Button:
    """this is a GUI button"""

    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(self.shape.getCenter(), label)

    def get_label(self):
        return self.text.getText()

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        mouse_x = point.getX()
        mouse_y = point.getY()

        width = abs(self.shape.getP1().getX() - self.shape.getP2().getX())
        height = abs(self.shape.getP1().getX() - self.shape.getP2().getX())
        x_pos = self.shape.getCenter().getX()
        y_pos = self.shape.getCenter().getY()

        if abs(mouse_x - x_pos) <= width/2 and abs(mouse_y - y_pos) <= height/2:
            return True
        return False

    def color_button(self, color):
        self.shape.setFill(color)

    def set_label(self, label):
        self.text.setText(label)
