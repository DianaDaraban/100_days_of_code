from menu import MENU

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

def insert_coins(money):
    print('Insert coins!')
    try:
        quarters = int(input('How many quarters? ')) * 0.25
        dimes = int(input('How many dimes? ')) * 0.1
        nickles = int(input('How many nickles? ')) * 0.05
        pennies = int(input('How many pennies? ')) * 0.01
    except ValueError:
        print('Invalid number!')
    all_coins = []
    all_coins.append(quarters)
    all_coins.append(dimes)
    all_coins.append(nickles)
    all_coins.append(pennies)
    passed_coins = sum(all_coins)
    if passed_coins == money:
        return True
    elif passed_coins > money:
        return f'Here is ${passed_coins-money:.2f} dollars in change.'
    else:
        return False

def check_report(water, milk, coffee, money, choice):
    updated_report = {}

    updated_report['water'] = report['water'] - water
    updated_report['milk'] = report['milk'] - milk
    updated_report['coffee'] = report['coffee'] - coffee

    if updated_report["water"] <=0:
        print('Sorry there is not enough water.')
        ask_for_coffee()
    elif updated_report['milk'] <=0:
        print('Sorry there is not enough milk.')
        ask_for_coffee()
    elif updated_report['coffee'] <=0:
        print('Sorry there is not enough coffee.')
        ask_for_coffee()
    else:
        insert = insert_coins(money)

        if insert:
            update_report(water, milk, coffee, money)
            if type(insert) == str:
                print(insert)
            print(f"Here is your {choice}. Enjoy!")
        else:
            print('Sorry that`s not enough money. Money refunded.')



def ask_for_coffee():
    coffee_served = True
    while coffee_served:
        choice = input('What would you like? (espresso/latte/cappuccino):\n').lower()

        if choice == 'report':
            update_report(0,0,0,0)
            print(f"""
            Water: {report['water']}ml
            Milk: {report['milk']}ml
            Coffee: {report['coffee']}g
            Money: ${report['money']}
        """)
        elif choice == 'espresso':
            check_report(50, 0, 18, 1.5, choice)
            print(report)
        elif choice == 'latte':
            check_report(200, 150, 24, 2.5, choice)
            print(report)
        elif choice == 'cappuccino':
            check_report(250, 100, 24, 3, choice)
            print(report)
        elif choice == 'off':
            coffee_served = False
        else:
            print('Enter a valid choice!')
            ask_for_coffee()

ask_for_coffee()