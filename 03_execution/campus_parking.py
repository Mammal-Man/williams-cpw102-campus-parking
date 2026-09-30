def main():
    found_hours = ask_for_hours()
    fee = calculate_parking_fee(found_hours)
    returnfee(found_hours, fee)

def ask_for_hours():
    hours = float(input("Please enter the number of hours you have parked or will park for: "))
    return hours

def calculate_parking_fee(hrs):
    rate = 2.0
    dollars = hrs * rate
    return dollars

def returnfee(hrs, cost):
    print("The fee for parking for " + str(hrs) + " hours is $" + str(cost))

main()