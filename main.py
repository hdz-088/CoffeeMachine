# ===========================
# Title: CoffeeMachine (Project)
# Author: HDz(https://github.com/hdz-088)
# Date of Creation: May 02nd, 2024
# Last Update: May 02nd, 2024
# =========== HDz ===========

# Inventory 
INVENTORY = {
    "ingredients": {
        "water": 500,
        "coffee": 200,
        "milk": 300,
    },
    "money": 0,
}

# Menu
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
            "coffee": 24,
            "milk": 150,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 300,
            "coffee": 100,
            "milk": 200,
        },
        "cost": 3.0,
    },
}

# <= FUNCTIONS

def header():
    """This Functions Prints Menu"""
    print("=================================")
    print("|\tDeveloper's Cafe\t|")
    print("=================================")
    print("| 1. Espresso\t|\t$1.50\t|")
    print("| 2. Latte\t|\t$2.50\t|")
    print("| 3. Cappuccino\t|\t$3.00\t|")
    print("=================================\n")
    
def report():
    """It Prints Remained Inventory"""
    print("\n-* Machine Inventory *-")
    print(f"> Water: {INVENTORY["ingredients"]["water"]}")
    print(f"> Coffee: {INVENTORY["ingredients"]["coffee"]}")
    print(f"> Milk: {INVENTORY["ingredients"]["milk"]}")
    print(f"> Money: ${INVENTORY["money"]}\n")
    gettingInput()
    
def updateInventory(coffee, inventory):
    """It Updates Inventory Based on User's Order"""
    INVENTORY["money"] += MENU[coffee]["cost"]
    required = MENU[coffee]["ingredients"]
    for ingredient, quantity in required.items():
        inventory["ingredients"][ingredient] -= quantity
    return inventory

def makingEspresso(INVENTORY, MENU):
    """A Function to Make Espresso"""
    INVENTORY = updateInventory("espresso", INVENTORY)
    print(f"\nYour Bill is ${MENU["espresso"]["cost"]}")
    print("Enjoy Your Espresso!\n")
    gettingInput()
    
def makingLatte(INVENTORY, MENU):
    """A Function to Make Latte"""
    INVENTORY = updateInventory("latte", INVENTORY)
    print(f"\nYour Bill is ${MENU["latte"]["cost"]}")
    print("Enjoy Your Latte!\n")
    gettingInput()
    
def makingCappuccino(INVENTORY, MENU):
    """A Function to Make Cappuccino"""
    INVENTORY = updateInventory("cappuccino", INVENTORY)
    print(f"\nYour Bill is ${MENU["cappuccino"]["cost"]}")
    print("Enjoy Your Cappuccino!\n")
    gettingInput()
    
def checkingInventory(coffee, inventory):
    """This Function Checks for Inventory Before Confirming User's Order"""
    required = MENU[coffee]["ingredients"]
    for ingredient, quantity in required.items():
        if inventory["ingredients"][ingredient] < quantity:
            print("Not Enough Inventory\n")
            return False
    return True
    
def gettingInput():
    """This Function Makes Order Based on USer Input"""
    order = input("What would you Like: ")
    if order == "1":
        if checkingInventory("espresso", INVENTORY):
            makingEspresso(INVENTORY, MENU)
        else:
            gettingInput()
    elif order == "2":
        if checkingInventory("latte", INVENTORY):
            makingLatte(INVENTORY, MENU)
        else:
            gettingInput()
    elif order == "3":
        if checkingInventory("cappuccino", INVENTORY):
            makingCappuccino(INVENTORY, MENU)
        else:
            gettingInput()
    elif order == "report":
        report()
    elif order == "exit":
        print("Thank You. Have a Nice Day!\n")
    else:
        print("Invalid Input. Try Again\n")
        header()
        gettingInput()
    

# FUNCTIONS =>
# -------------------------
# <= Calling Functions
header()
gettingInput()
