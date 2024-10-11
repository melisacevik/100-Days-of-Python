import warnings

warnings.filterwarnings("ignore")

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "cost":0
}

user_input = input("What would you like? (espresso/latte/cappucino): ")

def insert_coins():
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: " )) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def calculate_change():
    change = insert_coins() - MENU[user_input]["cost"]
    return round(change, 2)

user_want = True
while user_want == True:
    if user_input == "report":
        [print(f"{key.capitalize()}: {value}") for key, value in resources.items()]
    if user_input == "latte":
        print(f"Here is ${calculate_change()} in change.")
        print(f"Here is your latte ☕️ Enjoy!")
        resources["cost"] += MENU["latte"]["cost"]
    user_input = input("What would you like? (espresso/latte/cappucino): ")