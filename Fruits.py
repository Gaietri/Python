# Create a list of fruits iterate over it and add "milkshake" at the end and print on console

fruits = ["apple", "banana", "avocado", "mango"]
for i in fruits:
    print(i + " milkshake")
fruits[0]
print(fruits[0:2:1])    # first two fruits
print(fruits[0:5])      # first five elements
print(fruits[1:3])      # start to finish
print(fruits[:5:2])     # [start:end:step]
print(fruits[-1::-1])   # reverse
print(fruits[-1:-3:-2])

# sort function
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)


fruits.append('pineapple')
print(fruits)

# treat list as a stack and remove top element
# popped_el = fruits.pop()
# print(fruits)
# print(popped_el)
