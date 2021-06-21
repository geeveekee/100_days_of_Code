import logo 
import sys
from data import MENU, resources

COFFEE = 1000
MILK = 2000
WATER = 2000

logo.print_logo()
def check_availability(water, milk, coffee):
  global COFFEE
  global MILK
  global WATER
  if COFFEE >= coffee and MILK >= milk and WATER >= water:
    return True
  else:
    if COFFEE < coffee:
      print("We are out of coffee")
    elif MILK < milk:
      print("We are out of milk")
    if WATER < water:
      print("We are out of water")
    return False
  
def calculate_money(cost):
  print("Please enter coins: ")
  quarters = int(input("How many quarters?: "))
  dimes = int(input("How many dimes?: "))
  nickles = int(input("How many nickles?: "))
  pennies = int(input("How many pennies?: "))
  total = ((0.25*quarters)+(0.10*dimes)+(0.05*nickles)+(0.01*pennies))
  if total > cost:
    change = total-cost
  elif total < cost:
    change = 0
    print("Insufficient money. Please order again!")
    game()
  else:
    change = 0  
  print(f"Here is ${change} in change.")

def report():
  global WATER
  global MILK 
  global COFFEE
  print(f"Water: {WATER}ml")
  print(f"Milk: {MILK}ml")
  print(f"Coffee: {COFFEE}g")

def update_resources(water, milk, coffee):
  global WATER
  WATER = WATER - int(water)
  global MILK
  MILK = MILK - int(milk)
  global COFFEE
  COFFEE = COFFEE - int(coffee)

def espresso():
  drink = "espresso"
  ingredients = MENU['espresso']['ingredients']
  water_e = ingredients['water']
  coffee_e = ingredients['coffee']
  milk_e = 0
  cost_e = MENU['espresso']['cost']
  if check_availability(water_e, 0, coffee_e):
    calculate_money(cost_e)
    print(f"Here is your {drink}. Enjoy!")
    update_resources(water_e, milk_e, coffee_e)
 
  else:
    print("Sorry for the inconvenience!")

  return 
def latte():
  drink = "latte"
  ingredients = MENU['latte']['ingredients']
  water_l = ingredients['water']
  coffee_l = ingredients['coffee']
  milk_l = ingredients['milk']
  cost_l = MENU['latte']['cost']
  if check_availability(water_l, milk_l, coffee_l):
    calculate_money(cost_l)
    print(f"Here is your {drink}. Enjoy!")
    update_resources(water_l, milk_l, coffee_l)
 
  else:
    print("Sorry out of resources!")

  return 
def cappuccino():
  drink = "cappuccino"
  ingredients = MENU['cappuccino']['ingredients']
  water_c = ingredients['water']
  coffee_c = ingredients['coffee']
  milk_c = ingredients['milk']
  cost_c = MENU['cappuccino']['cost']
  if check_availability(water_c, milk_c, coffee_c):
    calculate_money(cost_c)
    print(f"Here is your {drink}. Enjoy!")
    update_resources(water_c, milk_c, coffee_c)
 
  else:
    print("Sorry out of resources!")

  return 

def check_order(order):
  if order == 'e':
    espresso()
  elif order == 'l':
    latte()
  elif order == 'c':
    cappuccino()
  elif order == 'off':
    sys.exit()

  else:
    report()

  return

def game():
  order = input("What would you like?(espresso[e]/latte[l]/cappuccino[c]/report[r]/[off]: ")
  check_order(order)
  game()

game()