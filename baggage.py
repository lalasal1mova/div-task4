weight = int(input("Enter your a weight of your baggage: "))
ticket = str(input("Enter your ticket type(econom/business): "))

if ticket == 'econom':
    if weight < 23:
        print("Free")

    elif weight >= 23 and weight <=32:
        print("Extra 30 AZN")

    else:
        print("The baggage is not accepted")

if ticket == 'business':
    if weight <= 32:
        print("Free")

    else:
        print("The baggage is not accepted")