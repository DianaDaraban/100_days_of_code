from menu import MENU

coffee_served = True

def serve_coffee():
    coffee_served = True

report = {
            'water': 300,
            'milk': 200,
            'coffee': 100,
            'money': 0,
    }

def update_report(water, milk, coffee, money):
    report['water'] -= water
    report['milk'] -= milk
    report['coffee'] -= coffee
    report['money'] += money

    return f"""
        Water: {report['water']}ml
        Milk: {report['milk']}ml
        Coffee: {report['coffee']}g
        Money: ${report['money']}
"""




# input for asking a coffee
while coffee_served:
    choice = input('What would you like? (espresso/latte/cappuccino):\n').lower()

    if choice == 'report':
        print(update_report(0,0,0,0))
    elif choice == 'espresso':
        print(update_report(50, 0, 18, 1.5))
    elif choice == 'latte':
        print(update_report(200, 150, 24, 2.5))
    elif choice == 'cappuccino':
        print(update_report(250, 100, 24, 3))
