
# Creating a dictionary for groceries with nested lists
groceries = {
    'Fruit': ['apple', 'banana', 'avocado', 'mango'],
    'Dairy': ['cheese', 'milk', 'yogurt', 'bread'],
    'Staples': ['rice', 'noodles', 'pasta'],
    'Veggies': ['onion', 'tomato', 'potato'],
}
# Accessing items in the 'Fruit' category
fruit_items = groceries['Fruit']
print("Fruit items:", fruit_items)

# Accessing items in the 'Dairy' category
dairy_items = groceries['Dairy']
print('Dairy items:', dairy_items)

# Accessing 3rd item in the 'Veggies' category
Veggies = groceries.get('Veggies', [])[2]
print("Veggies:", Veggies)