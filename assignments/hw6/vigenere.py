"""
Name: Steve Ford
vigenere.py

Certificate of Authenticity:
I certify that this assignment is entirely my own work.


~~~Pseudo Code~~~

define problem: we want to be able to convert plain text into a safe
                and encrypted form by using the vigenere cypher. The
                main problem is knowing which letters to be swapped with
                what.

Inputs/Outputs: we will be able to type in a message, the message can use the 26
                english characters, caps, mixed, or lower; and spaces. Additionally
                we will be able to take mouse input for the button to encode

                Our only outputs will be: flavor text, instructions, and the
                encoded message.

Design: I will create shift() which takes two characters. Converts them both into unicode
        adds their values then converts the sum into text with chr(), need a modular/
        wrapping effect for letters like Z getting added unto. This function returns
        a single character

        the inputted plain text will be converted to uppercase for unicode continuity

        the plain text will then remove all its spaces

        repeat both steps for the key phrase

        modified plain text and key phrase are identified

        invoke code() with the modified strings

        code function initializes local accumulator

        from here in code() a loop will begin which iterates through the length of the
        modified plain text message

        In the body of the loop "i" will be used to index the message and i % length of
        key phrase will be used to determine what the shift character is

        with both the shift characters identified I will invoke shift(), it will return the
        new character which will be added to the accumulator

        when code() loop is done end of function will return the accumulator aka the encoded
        message
"""
from graphics import(GraphWin, Text, Entry, Point, Rectangle)

# capital A = 65 capital Z = 90
# A=0 and Z=25


def main():
    win = GraphWin("Vigenere", 700, 500)
    win.setBackground("Dark Grey")

    instructions(100, 150, "Message to encode:", win)
    instructions(100, 225, "Enter keyword:", win)
    button = Text(Point(350, 375), "Click to encode")
    button.draw(win)
    button_rect = Rectangle(Point(290, 350), Point(410, 400))
    button_rect.draw(win)

    message_input = Entry(Point(435, 150), 50)
    key_input = Entry(Point(300, 225), 20)
    message_input.draw(win)
    key_input.draw(win)

    win.getMouse()

    secret_message = code(message_input.getText(), key_input.getText())

    button.undraw()
    button_rect.undraw()
    instructions(350, 350, "Resulting message:", win)
    instructions(350, 375, secret_message, win)
    instructions(350, 450, "Click to close the window", win)

    win.getMouse()
    win.close()


def code(message, keyword):
    secret = streamline(message)
    key = streamline(keyword)
    acc = ""
    for letter in range(len(secret)):
        acc += shift(secret[letter], key[letter % len(key)])
    return acc


def shift(base, rate):
    base = ord(base) - 65
    rate = ord(rate) - 65
    new_letter = chr(((base + rate) % 26) + 65)
    return new_letter


def streamline(text_input):
    new_text = str(text_input).upper()
    new_text = new_text.replace(" ", "")
    return new_text


def instructions(pos_x, pos_y, words, window):
    built_text = Text(Point(pos_x, pos_y), words)
    built_text.setSize(16)
    built_text.setTextColor("Blue")
    built_text.draw(window)


if __name__ == "__main__":
    main()
