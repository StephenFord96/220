"""
Name: <Stephen Ford>

Problem: This function calculates the area of a rectangle
"""


def calc_area():
    """this takes user input and calculates the area of a rectangle"""
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)


def calc_volume():
    """this takes user input and calculates the volume of a rectangular prism"""
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Area =", volume)


def shooting_percentage():
    """this takes user input and calculates their accuracy in basketball"""
    shots_taken = eval(input("How many shots did you take: "))
    shots_made = eval(input("How many shots did you make: "))
    accuracy = (shots_made/shots_taken) * 100
    print("Your shooting percentage is: ", round(accuracy, 2), "%", sep="")


def coffee():
    """this calculates the cost of a store managers order of coffee"""
    pounds_ordered = eval(input("How many pounds of coffee are you ordering: "))
    cost_of_order = (10.5 * pounds_ordered)+(0.86 * pounds_ordered) + 1.5
    print("Your order costs:", cost_of_order)


def kilometers_to_miles():
    """this converts kilometers to miles"""
    kilometers = eval((input("How many Kilometers is your trip: ")))
    print("You will drive", round(kilometers/1.61, 2), "miles")

