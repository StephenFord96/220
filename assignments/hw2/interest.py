"""Calculates Interest"""


def main(ann_interest, cyc_length, net_bal, payment_made, day_made):
    interest_charge = (((net_bal*cyc_length - payment_made * (cyc_length - day_made))/cyc_length)*(ann_interest/1200))
    print(interest_charge)
    return interest_charge


main(15.84, 31, 850, 400, 20)
