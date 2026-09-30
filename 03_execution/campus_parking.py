def calculate_parking_fee():
    hours = float(input("Please enter the number of hours you have parked or will park for: "))
    cost = 2.0
    dollars = hours * cost
    print("The fee for parking for " + str(hours) + " hours is $" + str(dollars))

calculate_parking_fee()