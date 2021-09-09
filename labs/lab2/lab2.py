"""
Name: <Steve Ford>
lab2.py
"""

import math


def sum_of_threes():
    bound = eval(input("What is upper bound? "))
    accumulation = 0
    for x in range(0, bound + 1, 3):
        accumulation = x + accumulation

    print(accumulation)


def multiplication_table():
    table_size = eval(input("What is multiplication table length? "))
    for h in range(1, table_size+1):
        for w in range(1, table_size+1):
            if w != table_size:
                if w*h < 10:
                    print(w*h, end="  ")
                elif w*h >= 10:
                    print(w*h, end=" ")
            else:
                print(w*h)


def triangle_area():
    a = eval(input("What is the first lengths of the triangle? "))
    b = eval(input("What is the second lengths of the triangle? "))
    c = eval(input("What is the third lengths of the triangle? "))
    s = (a+b+c)/2
    area = math.sqrt(s*((s-a)*(s-b)*(s-c)))
    print(area)


def sumSquares():
    start = eval(input("What is your starting point? "))
    ending = eval(input("What is your ending point? "))
    accumulation = 0
    for i in range(start, ending + 1):
        accumulation = accumulation + (i**2)
    print(accumulation)


def power():
    base = eval(input("What is the base? "))
    exponent = eval(input("What is the exponent? "))
    accumulation = 1
    for i in range(0, exponent):
        accumulation = accumulation * base
    print(accumulation)
