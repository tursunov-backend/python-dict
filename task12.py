inventory = {'apple': 10,
    'banana': 5
}

product = input('praduct: ')

if product not in inventory:
    inventory[product] = 0

print(inventory)
