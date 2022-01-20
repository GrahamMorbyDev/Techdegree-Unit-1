import math


def spilt_check(total, number_of_people):
    if number_of_people <= 1:
        raise ValueError('More than one person is required to spilt the check')
    return math.ceil(total / number_of_people)


try:
    total_due = float(input("What is the total due?"))
    how_many = int(input("How many people are eating?"))
    amount_due = spilt_check(total_due, how_many)
except ValueError as err:
    print("Oh No! That's not a valid value. Try again...")
    print("({})".format(err))
else:
    print("Each person owes ${}".format(amount_due))
