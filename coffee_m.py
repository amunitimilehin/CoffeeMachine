from coffee_m_data import MENU, resources




def serve_coffee(type):
    for i in MENU:
        if i == type:
            if MENU[i]["ingredients"]["water"] <= resources["water"]:
                MENU[i]["ingredients"]["water"] -= resources["water"]
            else:
                print("Sorry there is not enough water")
            if MENU[i]["ingredients"]["milk"] <= resources["milk"]:
                MENU[i]["ingredients"]["milk"] -= resources["milk"]
            else:
                print("Sorry there is not enough milk")
            if MENU[i]["ingredients"]["coffee"] <= resources["coffee"]:
                MENU[i]["ingredients"]["coffee"] -= resources["coffee"]
            else:
                print("Sorry there is not enough coffee")


def coins():
    print("Please insert coins")
    quarters = int(input("how many quarters ")) * 0.25
    dimes = int(input("how many dimes ")) * 0.10
    nickels = int(input("how many nickels ")) * 0.05
    pennies = int(input("how many pennies ")) * 0.01
    total_cash = quarters + dimes + nickels + pennies
    return total_cash

    
order = input("What would you like? (espresso/latte/cappuccino): ")
def play(): 
    money = 0
    if order == "report":
        report = []
        for i in resources:
            report.append(resources[i])
        print(f"Water: {report[0]}\n Milk: {report[1]}\n Coffee: {report[2]}\n Money: ${money}")
    else:
        fee = coins()
        if fee >= MENU[order]["cost"]:
            money += fee
            change = round(fee - MENU[order]["cost"], 2)
            print(f"Here is ${change} in change.")
        else:
            print("Sorry that's not enough money. Money refunded.")
        serve_coffee(order)
        
        print(f"Here is your {order} ☕️. Enjoy!")
        order = input("What would you like? (espresso/latte/cappuccino): ")
        return order
    
while  play() == "off":
    play()









