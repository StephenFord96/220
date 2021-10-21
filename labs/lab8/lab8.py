"""
Name: Steve Ford
Lab8.py
"""

from encryption import (encode, encode_better)


def number_words(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    output = open(out_file_name, "w+")
    i = 1
    for line in infile:
        words = line.split()
        for word in words:
            output.write((str(i) + " " + word + "\n"))
            i += 1
    output.close()
    infile.close()


def hourly_wage(in_file_name, out_file_name):
    pay_bump = 1.65

    infile = open(in_file_name, "r")
    output = open(out_file_name, "w+")

    for line in infile:
        parts = line.split()
        wage = float(parts[2])
        wage = wage + pay_bump
        weekly_pay = wage * int(parts[3])
        output.write(str(parts[0]) + " " + str(parts[1]) + " " + str(weekly_pay) + "\n")
    output.close()
    infile.close()


def calc_check_sum(isbn):
    acc = 0
    for i in range(10):
        pos = 10 - i
        acc += (pos * int(isbn[i]))
    return acc


def send_message(file, friend):

    infile = open(file, "r")
    output = open(friend + ".txt", "w+")
    for line in infile:
        output.write(line)
    infile.close()
    output.close()


def send_safe_message(file, friend, key):

    infile = open(file, "r")
    output = open(friend + ".txt", "w+")
    for line in infile:
        output.write(encode(line, key))
    infile.close()
    output.close()


def send_uncrackable_message(file, friend, key_location):

    infile = open(file, "r")
    output = open(friend + ".txt", "w+")
    in_key = open(key_location, "r")
    key = in_key.read()
    for line in infile:
        output.write(encode_better(line, key))
    infile.close()
    output.close()
    in_key.close()


def main():
    # number_words("Walrus.txt", "Walrus_Out.txt")
    # hourly_wage("hourly_wages.txt", "wages_spreadsheet.txt")
    # print(calc_check_sum("0072946520"))
    # send_message("message.txt", "Francis_The_Friend")
    # send_safe_message("message.txt", "Francis_The_Friend", 3)
    send_uncrackable_message("message.txt", "Francis_The_Friend", "pad.txt")


main()
