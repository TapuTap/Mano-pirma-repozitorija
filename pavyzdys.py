def clear(): 
    if os.name == 'nt':
         os.system('cls') 
    else:
         os.system('clear')

def add_product(name, amount):
    if name in products:
        products[name] += amount
    else:
        products[name] = amount

def remove_product(name):
    if name in products:
        del products[name]

def show_products():
    print("Product\t\tAmount")
    for name, amount in products.items():
        print(f"{name}\t\t{amount}")

def calculate_weight():
    total_weight = 0
    for name, amount in products.items():
        if name.endswith("kg"):
            total_weight += amount
        elif name.endswith("l"):
            total_weight += amount * 1  # density of liquid is 1 kg/l
        else:
            total_weight += amount * 1  # prepared dishes weigh 1 kg per portion
    return total_weight

def check_recipe():
    recipe = {}
    portions = int(input("How many portions do you want to make? "))
    while True:
        line = input("Enter an ingredient and its amount (or 'done' to finish): ")
        if line == "done":
            break
        name, amount = line.split(": ")
        recipe[name] = float(amount)
    missing_ingredients = {}
    for name, amount in recipe.items():
        if name not in products:
            missing_ingredients[name] = amount
        elif products[name] < amount * portions:
            missing_ingredients[name] = amount * portions - products[name]
    if missing_ingredients:
        print("You don't have enough of the following ingredients:")
        for name, amount in missing_ingredients.items():
            print(f"{name}: {amount}")
    else:
        total_weight = 0
        for name, amount in recipe.items():
            total_weight += amount * portions
        excess_weight = calculate_weight() - total_weight
        if excess_weight >= 0:
            print(f"You have enough ingredients for {portions} portions.")
            if excess_weight > 0:
                print(f"You will have {excess_weight} kg of excess ingredients.")
        else:
            print(f"You don't have enough space in the fridge for {portions} portions.")