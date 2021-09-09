"""
Name: Steve Ford
interest.py

Certificate of Authenticity:
I certify that this assignment is entirely my own work.
"""


def main():

    annual_interest = eval((input("annual interest ")))
    cyc_length = eval(input("Days in month "))
    net_bal = eval(input("Previous Balance "))
    payment_made = eval(input("Payment made "))
    day_made = eval(input("Day of Payment "))
    sum_charge = ((net_bal*cyc_length - payment_made * (cyc_length - day_made))/cyc_length)
    interest_charge = sum_charge * (annual_interest/1200)
    interest_charge = round(interest_charge, 2)
    print(interest_charge)


if __name__ == '__main__':
    main()
