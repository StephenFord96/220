"""
Name: Steve Ford
mean.py

Certificate of Authenticity:
I certify that this assignment is entirely my own work.

---Pseudo Code---

Define problem: we want an application that accepts a large amount of data
from a traffic camera/observation post that ultimately gives us orderly averages
of a variable amount of rounds from a variable amount of observed time

I/O: Inputs: # of roads surveyed, # of days per road, # of cars per day of each road
     Outputs: average cars per day of each road, total # of cars observed,
              average # of cars (rounded to 2 decimals)

Design:
request the # of roads and store in road_total
first/outer loop will have a range of road_total
outer loop iterator "i" will be used to reference which road is being drawn from
the top of the body of outer loop will request how many---
 ---days road "i" will be observed; store in _days_

car_single_road accumulator will be initialized/reset to vale of zero
a new loop will begin inside the body of outer loop; the inner loop
inner loop will have a range of _days_
inner loops body will request the # of cars observed on that day and---
---add it to the accumulator: car_single_road

outside of inner loop now at bottom of outer loop
the car_single_road accumulator will be added to car_total accumulator
the road's average will be calculated with _days_ and car_single_road
average will be printed

this will repeat until the outer loop is completed

outside of outer loop and now below it program will print the car_total accumulator
road_total and car_total will be used to calculate the average # of cars per road

"""


def main():

    total_roads = int(input("How many roads were surveyed? "))
    car_total = 0

    for road in range(total_roads):

        days = int(input("How many days was Road " + str(road + 1) + " surveyed?"))
        cars_single_road = 0

        for day in range(days):
            cars_single_road += int(input("How many cars travelled on day " + str(day + 1) + "?"))

        car_total += cars_single_road
        road_average = round(cars_single_road/days, 2)
        print("Road " + str(road + 1) + "average vehicles per day: " + str(road_average))

    print("Total number of vehicles on all roads: " + str(car_total))
    total_average = round(car_total/total_roads, 2)
    print("Average number of vehicles per road: " + str(total_average))


if __name__ == "__main__":
    main()
