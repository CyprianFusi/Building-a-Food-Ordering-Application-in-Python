# Global Variables

APP_NAME = 'WUNA DONG CHOP'

MENU = {'sku1': {'Hamburger': 6.51},
        'sku2': {'Cheeseburger': 7.75},
        'sku3': {'Milkshake': 5.99},
        'sku4': {'Fries': 2.39},
        'sku5': {'Sub': 5.87},
        'sku6': {'Ice Cream': 1.55},
        'sku7': {'Fountain Drink': 3.45},
        'sku8': {'Cookie': 3.15},
        'sku9': {'Brownie': 2.46},
        'sku10': {'Sauce': 0.75},
       }

ACTIONS = {1: 'Add a new menu item to cart',
           2: 'Remove an item from the cart',
           3: 'Modify a cart item\'s quantity',
           4: 'View cart',
           5: 'Checkout',
           6: 'Exit'
          }

TAX_RATE = 0.03

CART = {}

# Displaying the Menu

def display_menu():
    '''
    This function displays the available menu to users
    '''
    
    print('\n------------------------')
    print('***  Available Menu  ***')
    print('------------------------')
    print('Code   Item   Unit Price')
    print('------------------------')
    for sku, menu in MENU.items():
        for item, price in menu.items():
            print(f'({sku[3:]})', f'{item}: ${price}')
            
# Add Menu Items to the Cart

def add_to_cart(code, qty):
    '''
    The function adds items to cart
    code: item key
    qty: quantity to add
    '''
    sku = f'sku{code}'
    if sku in MENU:
        if sku in CART:
            CART[sku] += qty
        else:
            CART[f'sku{code}'] = qty
        item, price = list(MENU[sku].items())[0]
        print(f'\n{qty} {item}(s) added to cart...\n')
    else:
        print('Invalid menu item\n')
        
# Display cart content to user

def display_cart_content():
    '''
    The function displays cart content
    '''
    print('\n------------------------')
    print('***   Items in cart  ***')
    print('------------------------')
    total = 0
    for sku in CART:
        menu = MENU[sku]
        item, price = list(menu.items())[0]
        total += price * CART[sku]
        print(f'({sku[3:]})', f'{item}, Quantity: {CART[sku]}, Price: ${price * CART[sku]}\n')
    print(f'Total: ${total: .2f}')
    
# Removing Items from the Cart

def delete_from_cart(code):
    '''
    The function removes items from cart
    code: item key
    '''
    sku = f'sku{code}'
    if sku in CART:
        qty = CART.pop(sku)
        item, _ = list(MENU[sku].items())[0]
        print(f'{qty} {item}(s) deleted from cart\n')
    else:
        print(f'Item not found in cart!\n')
        
# Modifying Item Quantities in the Cart

def modify_cart(code, qty, add = True):
    '''
    The function adds or removes items to/from cart
    code: item key
    qty: quantity to add
    add: flag indicating add/remove item
    '''
    sku = f'sku{code}'
    if add:
        add_to_cart(code, qty)
    else:
        qty = -qty
        add_to_cart(code, qty)
    if CART[sku] <= 0:
        delete_from_cart(code)
        
# Viewing Cart Contents

def view_cart():
    '''
    The function displays cart content
    '''
    print('\n------------------------')
    print('***   Items in cart  ***')
    print('------------------------')
    total = 0
    for sku in CART:
        menu = MENU[sku]
        item, price = list(menu.items())[0]
        total += price * CART[sku]
        print(f'{CART[sku]} x ', f'{item}, Price: ${price * CART[sku]}\n')
    print(f'Sub-Total: ${total: .2f}')
    print(f'\nTOTAL: ${total * (1 + TAX_RATE): .2f}')

# Checking out

def checkout():
    view_cart()
    print('=============================\n')
    print('Your order has been submitted. Thank you!')
    print('\nChecking out...')
    
# Prompting for User Input

def get_user_request():
    code = input('\nWhat do you wish to order?\nEnter item code (Eg 1): ').strip()
    if code.isdigit():
        code = int(code)
    else:
        print('Invalid code')
    qty = input('Enter quanity (Eg 1): ').strip()
    if qty.isdigit():
        qty = int(qty)
    else:
        print('Invalid quantity')
    return code, qty

# Display Actions

def display_actions():
    print('\n-------------------------------')
    print('****   Available Options   ****')
    print('\nCode       Option            ')
    print('-------------------------------')
    for code in ACTIONS:
        print(f'({code}) {ACTIONS[code]}')
        
# Building the Ordering Loop

def process_user_request():
    print(f'Welcome to {APP_NAME}\n')
    in_process = True
    
    while in_process:
        display_actions()
        num = input('Enter corresponding code to continue (Eg 1): ').strip()
        if num.isdigit():
            num = int(num)
        else:
            print('Invalid code')
        if num == 1:
            display_menu()
            code, qty = get_user_request()
            add_to_cart(code, qty)
            
        elif num == 2:
            display_menu()
            code, qty = get_user_request()
            delete_from_cart(code)
            
        elif num == 3:
            display_menu()
            mod = input('Do you wish to add or subtract item? (A/S): ').strip()
            mod = mod.lower()
            code, qty = get_user_request()
            if mod == 's':
                modify_cart(code, qty, add = False)
            else:
                modify_cart(code, qty, add = True)
                
        elif num == 4:
            view_cart()
            ans = input('Do you have any other wish...?(Y/N): ').strip()
            if ans.lower() == 'n':
                checkout()
                in_process = False
            else:
                continue
        elif num == 5:
            checkout()
            in_process = False
            
        elif num == 6:
            in_process = False
        else:
            print('Invalid action')
