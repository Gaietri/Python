# Initialize an empty inventory
inventory = {}

# Add items to the inventory
inventory['apples'] = 5
inventory['bananas'] = 3
inventory['oranges'] = 2

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
