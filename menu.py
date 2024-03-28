# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered


# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")
Orders_list = [];
total = 0.0;
# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("\nFrom which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            # 2. Ask customer to input menu item number
            menu_selection = input("\nEnter the ID of the item you'd like to select: ")

            # 3. Check if the customer typed a number
            if menu_selection.isdigit():
                # Convert the menu selection to an integer
                menu_selection = int(menu_selection)

                # 4. Check if the menu selection is in the menu items
                if menu_selection in menu_items.keys():
                    # Store the item name as a variable
                    #print(f"\nYou have selected menu {menu_selection['Item name']}")
                    quantity = 1
                    # Ask the customer for the quantity of the menu item
                    quantity = input("\nEnter the quantity: ")

                    # Check if the quantity is a number, default to 1 if not
                    if quantity.isdigit() and int(quantity) > 0:
                        print(f"\nYou have selected:  {menu_items[menu_selection]['Item name']} and quantity is :{quantity}")
                    
                        #Customer enter valid manu and quantity, add it to order list
                        new_order = {"order": menu_items[menu_selection]['Item name'], "price": float(menu_items[menu_selection]['Price']), "quantity":  quantity } 
                        Orders_list.append(new_order);
                    else:
                        print( "\n Invalid selection. " )
                    # Tell the customer that their input isn't valid
                else: 
                    print( "\n Invalid selection" )

                # Tell the customer they didn't select a menu option

        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    while True:
       # Ask the customer if they would like to order anything else
        keep_ordering = input("\nWould you like to keep ordering? (Y)es or (N)o ")

        # Check the customer's input
        match keep_ordering.lower():
            # Customer chose yes
            case 'y':
                # Keep ordering
                place_order = True
                # Exit the keep ordering question loop
                break
            # Customer chose no
            case 'n':
                # Complete the order
                place_order = False
                # Since the customer decided to stop ordering, thank them for their order
                print("\n******Thank you for your order.*******")
                # Exit the keep ordering question loop
                break
            # Customer typed an invalid input
            case _:
                # Tell the customer to try again
                print("I didn't understand your response. Please try again.")

#check if user has place any order
if len(Orders_list)>0:
    # Print out the customer's order
    print("This is what we are preparing for you.\n")
    print("Item name                 | Price     | Quantity")
    print("--------------------------|---------- |-all----------")
    # 6. Loop through the items in the customer's order
    for order in Orders_list:
        # 8. Calculate the number of spaces for formatted printing
        num_item_spaces = 26 - len(order['order']);   
        # 9. Create space strings 
        item_spaces = " " * num_item_spaces
        print(f"{order['order']}{item_spaces}| ${order['price']}     | {order['quantity']}")
      
     
    # 11. Calculate the cost of the order using list comprehension
    total = sum(float(order['price']) * int(order['quantity']) for oitem in Orders_list)
    print("-------------------------------------------------")
    # and print the prices.
    print(f"Your Total is :                    ${total}           ")
    print("\n")

    