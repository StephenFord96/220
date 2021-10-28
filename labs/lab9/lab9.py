"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""

import math
from graphics import (GraphWin, Text, Circle, Point)


def addTen(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10


def squareEach(nums):
    # print(nums)
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2
    # print(nums)


def sumList(nums):
    acc = 0
    for i in range(len(nums)):
        acc += nums[i]
    # print(acc)
    return acc


def toNumbers(str_list):
    for i in range(len(str_list)):
        str_list[i] = float(str_list[i])


def writeSumOfSquares():
    i_file = input("What is the file name? ")
    in_file = open(i_file, "r")
    out_file = open("output.txt", "w+")
    raw_list = in_file.read()
    raw_list = raw_list.split()
    toNumbers(raw_list)
    squareEach(raw_list)
    answer = str(sum(raw_list))
    out_file.write(answer)
    out_file.close()
    in_file.close()


def starter():
    weight = eval(input("What is the weight? "))
    wins = eval(input("How many wins? "))
    if 160 > weight >= 150 and wins >= 5:
        print("This wrestler can be a starter")
    elif weight > 199 or wins > 20:
        print("This wrestler can be a starter")
    else:
        print("This wrestler is NOT a starter")


def leapYear(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def circleStuff():
    win = GraphWin("Circle Stuff", 400, 400)

    flavor_text = Text(Point(200, 350), "")
    flavor_text.setTextColor("Blue")

    p1 = win.getMouse()
    p2 = win.getMouse()
    radius = math.sqrt((p2.getX() - p1.getX()) ** 2 + (p2.getY() - p1.getY()) ** 2)
    circle = Circle(p1, radius)
    circle.draw(win)

    p3 = win.getMouse()
    p4 = win.getMouse()
    radius2 = math.sqrt((p4.getX() - p3.getX()) ** 2 + (p4.getY() - p3.getY()) ** 2)
    circle2 = Circle(p3, radius2)
    circle2.draw(win)

    distance = math.sqrt((p3.getX() - p1.getX()) ** 2 + (p3.getY() - p1.getY()) ** 2)
    if distance <= radius + radius2:
        flavor_text.setText("The circles collide")
    else:
        flavor_text.setText("The circles do NOT collide")
    flavor_text.draw(win)



    win.getMouse()
    win.close()


def main():
    nums_list = [5, 2, -3]
    steve_list = ["5", "2", "3"]
    # addTen(nums_list)
    # print(nums_list)
    # squareEach(nums_list)
    # nums_list = sumList(nums_list)
    # writeSumOfSquares()
    # starter()
    circleStuff()
    year = eval(input("What year is it? "))
    if leapYear(year):
        print(year, "is a leap year.")
    else:
        print(year, "is NOT a leap year.")


main()
