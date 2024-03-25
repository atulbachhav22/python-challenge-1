menu_items = [
    {"id": 1, "item": "Spaghetti", "price": 10.99},
    {"id": 2, "item": "Pizza", "price": 12.50},
    {"id": 3, "item": "Salad", "price": 7.99},
    {"id": 4, "item": "Burger", "price": 8.99},
    {"id": 5, "item": "Soup", "price": 5.50},
    {"id": 6, "item": "Steak", "price": 15.99},
    {"id": 7, "item": "Sandwich", "price": 6.99},
    {"id": 8, "item": "Fish and Chips", "price": 11.50},
    {"id": 9, "item": "Fried Chicken", "price": 9.99},
    {"id": 10, "item": "Tacos", "price": 8.50}
]

Orders_list = [] 
total = 0.0;

# Boolean to place the order
place_order = True

print("Menu Items:")
print("ID    Item               Price")
print("-" * 30)

# loop through items and print it for user selection
for item in menu_items:
    print(f"{item['id']:2}    {item['item']:15}    ${item['price']:.2f}")


while place_order:
    is_invalidselection = False
    quantity = 1
# Prompt the user to enter their selection
    menu_selection = input("\nEnter the ID of the item you'd like to select: ")
    
    #Check if user selected right option. option should be integer between 1-10
    if menu_selection.isdigit() and int(menu_selection) <= 10 and int(menu_selection) >=1:
        menu_selection = int(menu_selection)
        selected_item = next((item for item in menu_items if item["id"] == menu_selection), None)
        #prompt user for the quantity 
        quantity = input("\nEnter the quantity: ")
        #Check if user has enter valid input
        if quantity.isdigit() and int(quantity) > 0:
            print(f"\nThis is your selection {selected_item['item']} {quantity}")
        else:
            is_invalidselection= True;
    else:    
        is_invalidselection = True;
    
    #In case of invalid menu selction or invalid quanity display error 
    if is_invalidselection:
        print( "\nError!! Invalid selction" )
    else:
       #Customer enter valid manu and quantity, add it to order list
       new_order = {"order": selected_item['item'], "price": float(selected_item['price']), "quantity":  quantity } 
       Orders_list.append(new_order);
    
    # Provide exit optiony
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

if len(Orders_list)>0:
    print("\nItem name   | Price | Quantity")
    print("------------|-------|---------")
    for order in Orders_list:
        print(f"{order['order']}      | {order['price']}        | {order['quantity']}")
        total += int(order['quantity']) * float(order['price']); 
    print("------------------------------")
    print(f"Your Total is :                    {total}           ")
    print("\n")
    
