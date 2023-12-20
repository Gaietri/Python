# Initialize an empty inventory (key value pair)
inventory = {'apples': 5, 'bananas': 3, 'oranges': 2}

# Add items to the inventory

# Print the initial inventory
print("Initial Inventory:", inventory)

# Update the quantity of bananas
inventory['bananas'] = 7

# Print the updated inventory
print("Updated Inventory (bananas quantity updated):", inventory)

# Remove oranges from the inventory
del inventory['oranges']

# Print the final inventory
print("Final Inventory (oranges removed):", inventory)
