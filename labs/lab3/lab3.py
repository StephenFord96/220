"""
Name: <Steve Ford>
<Lab3>.py
"""


def homework_average():

    grade_count = int(input("How many assignment's have you done? "))
    grade_accumulation = 0

    for i in range(1, grade_count + 1):
        grade_accumulation = grade_accumulation + int(input("What was your grade on HW" + str(i)))
    grade_average = grade_accumulation/grade_count
    print(grade_average)


def tip_jar():

    jar_accumulation = 0

    for i in range(1, 6):
        jar_accumulation = jar_accumulation + eval(input("How much money are you tipping, person" + str(i)))
    print(jar_accumulation)


def newton():

    x = eval(input("What number are we squaring?"))
    refine = eval(input("How many refinements are we making?"))

    approx = x/2

    for i in range(1, refine):
        approx = (approx + (x/approx))/2
    print(approx)


def sequence():

    sequence_length = int(input("How long of a sequence do you want? "))
    for i in range(1, sequence_length + 1):
        y = 1 + (i//2)*2
        print(y)


def pi():

    accumulation = 1
    length = int(input("How many refinements are we making?"))

    for i in range(1, length + 1):
        top = 2 + ((i-1)//2)*2
        bottom = 1 + (i//2) * 2
        accumulation = accumulation * (top/bottom)

    print(2 * accumulation)
