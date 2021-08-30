def calc_area():
    length = eval (input("Enter the length:"))
    width = eval (input("Enter the width:"))
    area = length * width
    print("Area =",area)
def calc_volume():
    length = eval (input("Enter the length:"))
    width = eval (input("Enter the width:"))
    height = eval (input("Enter the height:"))
    area = length * width * height
    print("Area =",area)
def calc_shot():
    totalshots = eval(input("Enter the total shots:"))
    shotsmade = eval(input("Enter the shots made:"))
    precnt = shotsmade / totalshots
    print("Precnt =",precnt)
def calc_coffee():
    numberofpounds = eval(input("Enter the numberofpounds:"))
    coffecost = 10.50
    shippingcost = 0.86
    fixedcost = 1.50
    cost = numberofpounds * coffecost + numberofpounds * shippingcost + fixedcost
    print("Cost =",cost)
def calc_kilometers():
    kilometers = eval(input("Enter the numberofkilometers:"))
    kilometerstomiles = 1.61
    miles = kilometers / kilometerstomiles
    print("Miles =",miles)