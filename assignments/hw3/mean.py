"""
Name: Steve Ford
mean.py

Certificate of Authenticity:
I certify that this assignment is entirely my own work.

Pseudo Code and Process:
1.) The program will take values and convert them into all RMS/Harmonic/Geometric averages
2.) My inputs will be the amount of numbers I will want averaged and then the numbers.
    my outputs will be 3 floating point values associated with their average type

3.)

    ----RMS pseudo---
1-- I will prompt the user for # of #'s being averaged
2-- Loop with range of length #of#'s will prompt user for a value to be
     added to a list (the list of all values to be averaged)
3-- establish an accumulator set to 0
3-- begin RMS loop with a range of list's length
4-- will loop through list squaring the value then adding it to the accumulator
5-- divide accumulator by length of list
6-- take square root of accumulator
---- ended up hacking the list because it seems to not go
    with the test module
---can now get values correctly but test module is not happy likely need
   to just do all the others also

   ----Harmonic pseudo----
1-- user is already prompted for length of numbers
2-- run multiple accumulators through our RMS loop as it is now grabbing
     input of specific values along the way
---restructure input statement to be outside of assignment statement---
---input value is a changing variable now set before accumulator math
3 -- harmonic accumulator will be the value that is dividing one
     then added to itself
4--- divide 2 by the harmonic accumulator
5--- print it
---forgot to round harmonic value like the RMS before printing---

    ----geometric pseudo---
1. will follow exact same style of input/output
2. will initialize a third accumulator = geometric (1 instead of 0 because * )
3. each iteration of the loop will multiple the accumulator by user input
4. when loop is complete take the X root of accumulator while x is the amount
   of #'s inputted
5. round and print


"""

import math


def main():

    amount_of_values = int(input("How many numbers will be averaged together? "))

    rms_accumulator = 0
    harmonic_acc = 0
    geometric_acc = 1

    for i in range(amount_of_values):
        user_input = eval(input("What is value #" + str(i + 1)))
        rms_accumulator = rms_accumulator + user_input ** 2
        harmonic_acc = harmonic_acc + (1/user_input)
        geometric_acc = geometric_acc * user_input

    rms_accumulator = rms_accumulator/amount_of_values
    rms_accumulator = round(math.sqrt(rms_accumulator), 3)
    print(rms_accumulator)

    harmonic_acc = round(amount_of_values/harmonic_acc, 3)
    print(harmonic_acc)

    geometric_acc = (geometric_acc ** (1/amount_of_values))
    geometric_acc = round(geometric_acc, 3)
    print(geometric_acc)


if __name__ == "__main__":
    main()
