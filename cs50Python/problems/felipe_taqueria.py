menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    order = get_order()
    
    
def get_order():
    print("What's your order? ")
    total = 0
    while True:
        try:
            item = input(">> ")
        except EOFError: # detect when the user has inputted control-d
            print("\n")
            break
        else:
            try:
                item = item.strip().lower().title()
                item_cost = menu[item]
            except KeyError:
                print("Item not present in menu")
                continue
            else:
                total += item_cost 
                print(f"$ {total}")

















main()
