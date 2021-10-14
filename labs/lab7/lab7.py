"""
Name: Steve Ford
lab7.py
"""
import math


def cash_conversion():
    cash_input = eval(input("How many dollars do you have? "))
    print("${}.00".format(cash_input))


def encode():
    message = str(input("What is the message? "))
    shift = int(input("How much do you want to shift? "))
    secret_acc = ""
    for i in range(len(message)):
        new_letter = ord(message[i])
        new_letter += shift
        secret_acc += chr(new_letter)
    print(secret_acc)


def sphere_area(radius):
    answer = 4 * math.pi * (radius**2)
    answer = round(answer, 3)
    return answer


def sphere_volume(radius):
    answer = (4/3) * math.pi * (radius ** 3)
    answer = round(answer, 3)
    return answer


def sum_n(n):
    acc = 0
    for i in range(n + 1):
        acc += i
    return acc


def sum_n_cubes(n):
    acc = 0
    for i in range(n + 1):
        acc += i**3
    return acc


def file_stuff():
    in_file = open("read_write_file_test.py", "r")
    print(in_file.read())


def encode_better():
    message = str(input("What message to encode? "))
    key = str(input("what is your key? "))
    acc = ""
    for i in range(len(message)):
        key_mod = key[i % len(key)]
        new_letter = ord(message[i]) + ord(key_mod)
        acc += chr(new_letter - 97)
    print("Your secret code is: " + acc)


def main():
    cash_conversion()
    encode()
    print(sphere_area(10))
    print(sphere_volume(10))
    print(sphere_area(15))
    print(sphere_volume(15))
    print(sum_n(4))
    print(sum_n_cubes(4))
    file_stuff()
    encode_better()


main()
