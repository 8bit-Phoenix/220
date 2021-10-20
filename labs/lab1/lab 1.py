def calc_area():
    length = eval(input("Enter the length:"))
    width = eval(input("Enter the width:"))
    area = length * width
    print("Area =", area)


def calc_volume():
    length = eval(input("Enter the length:"))
    width = eval(input("Enter the width:"))
    height = eval(input("Enter the height:"))
    area = length * width * height
    print("Area =", area)


def calc_shot():
    total_shots = eval(input("Enter the total shots:"))
    shots_made = eval(input("Enter the shots made:"))
    percent = shots_made / total_shots
    print("Percent =", percent)


def calc_coffee():
    number_of_pounds = eval(input("Enter the number of pounds you want to buy:"))
    coffee_cost = 10.50
    shipping_cost = 0.86
    fixed_cost = 1.50
    cost = number_of_pounds * coffee_cost + number_of_pounds * shipping_cost + fixed_cost
    print("Cost =", cost)


def calc_kilometers():
    kilometers = eval(input("Enter the number of kilometers:"))
    kilometers_to_miles = 1.61
    miles = kilometers / kilometers_to_miles
    print("Miles =", miles)
