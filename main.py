from menu import *


def get_price(coffee):
    price = menu[coffee]["cost"]
    return price


def check_ingredients(coffee):
    ingredients = menu[coffee]["ingredients"]
    for ingredient in resources:
        if resources[ingredient] < ingredients[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def calculate_coins():
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    return quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01


def calculate_change(coins, price):
    change = float(coins) - float(price)
    if change > 0:
        return round(change, 2)


def new_resources(coffee_price, coffee_type):
    global profit
    ingredients = menu[coffee_type]["ingredients"]
    for ingredient in resources:
        resources[ingredient] -= ingredients[ingredient]
    profit += coffee_price


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


def coffee_machine():
    global shut_down
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffee_type == 'report':
        report()
        return
    elif coffee_type == 'off':
        shut_down = True
        return
    if not check_ingredients(coffee_type):
        return
    coffee_price = get_price(coffee_type)
    print(f"{coffee_type} costs {coffee_price}$\nPlease insert coins.")
    coins_entered = calculate_coins()
    if coins_entered < coffee_price:
        print("Sorry that's not enough money. Money refunded.")
        return
    change = calculate_change(coins_entered, coffee_price)
    print(f"Here is {change}$ in change")
    print(f"Here is your {coffee_type} ☕. Enjoy!")
    new_resources(coffee_price, coffee_type)


shut_down = False
while not shut_down:
    coffee_machine()

