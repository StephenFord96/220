"""
Name: Steve Ford
weighted_average.py

Certificate of Authenticity:
I certify that this assignment is entirely my own work.

---Pseudo Code---
inputs: grades.txt as such that <name:> <weight> <grade> <weight> <grade>....etc
        <name>'s can have spaces
Output: names with associated averages and the class's average all rounded to 1 decimal point

Design: search a string to find ":" slice string there for name to be stored, ignore following space
        string2[0], pick apart string parts using a loop with i+1 to grab weight and average/skip all
        in one iteration.
"""


def main():
    weighted_average("grades.txt", "avg.txt")


def weighted_average(in_filename, out_filename):
    infile = open(in_filename, "r")
    out_filename = open(out_filename, "w")

    total_acc = 0
    population_acc = 0
    for line in infile:

        name_marker = line.find(":")
        name = line[0:name_marker]

        grades = line[name_marker + 1:]
        grades = grades.split()

        student_acc = 0
        weight_acc = 0
        for i in range(0, len(grades), 2):
            if i < len(grades) - 1:
                student_acc += eval(grades[i]) * eval(grades[i + 1])
                weight_acc += eval(grades[i])

        if weight_acc == 100:
            student_acc = student_acc/100
            total_acc += student_acc
            student_acc = round(student_acc, 1)
            out_filename.write(name+"'s average: " + str(student_acc) + "\n")
            population_acc += 1
        elif weight_acc < 100:
            out_filename.write(name + "'s average: " "Error: The weights are less than 100." + "\n")
        else:
            out_filename.write(name + "'s average: " "Error: The weights are more than 100." + "\n")

    total_acc = total_acc/population_acc
    total_acc = round(total_acc, 1)
    out_filename.write("Class average: " + str(total_acc))


if __name__ == "__main__":
    main()
