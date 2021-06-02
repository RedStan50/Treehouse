# This program sells a set number of tickets at a set price and decreases the number of
# tickets as they are sold until sold out

import sys

#Set the ticket price
TICKET_PRICE = 10

#Set the tickets remaining
tickets_remaining = 100  

while tickets_remaining >= 1:
    # Shows how many tickets are left
    print(f"There are {tickets_remaining} ticket(s) left.\n")
    # Asks the user for their name and how many tickets they want
    name = input("Hello, what is your name? ")
    number_of_tickets = input(f"Hi {name}, how many tickets would you like? ")
    # Makes sure there are a valid number of tickets left
    try:
        number_of_tickets = int(number_of_tickets)
        if number_of_tickets > tickets_remaining:
            raise ValueError("There are not that many tickets available")
    except ValueError as err:
        print(f"ERROR! Invalid input")
    else:
        ticket_cost = number_of_tickets * TICKET_PRICE
        
        print(f"\nThe total cost of your tickets is {ticket_cost}\n")
        
        # Confirms the user wishes to proceed with the ticket purchase allowing only y or n
        proceed = None
        while proceed not in("y", "n"):
            proceed = input(f"Do you wish to proceed with the purchase {name}?\n (y or n): ")
            proceed = str(proceed)
            
            if proceed.lower() == "y":
                print("SOLD!\n")
                tickets_remaining -= number_of_tickets
            
            elif proceed.lower() == "n":
                print(f"Goodbye {name}\n")
            else:
                print("Press y or n only!")

print("The tickets are SOLD OUT!")

