TICKET_PRICE = 10
tickets_remaining = 100
SERVICE_CHARGE = 2


def calculate_price(number_of_tickets):
    return (number_of_tickets * TICKET_PRICE) + SERVICE_CHARGE


while tickets_remaining >= 1:
    print('There are {} tickets remaining'.format(tickets_remaining))
    users_name = input('What is your name?   ')
    user_tickets = input('How many tickets would you like, {}?  '.format(users_name))
    try:
        ticket_cost = calculate_price(int(user_tickets))
        if int(user_tickets) > tickets_remaining:
            raise ValueError("There are only {} remaining".format(tickets_remaining))
    except ValueError as err:
        print('Oh No! We ran into an error!, {}. Please try again'.format(err))
    else:
        print("The total due is {}".format(ticket_cost))
        user_continue = input("Do you wish to continue? (y/n)")
        user_continue = user_continue.capitalize()
        if user_continue == 'Y':
            print('Sold! Thank you for your purchase')
            tickets_remaining -= int(user_tickets)
        else:
            print('Thank you for stopping by the store today {}'.format(users_name))

print('All tickets have now been sold!')
