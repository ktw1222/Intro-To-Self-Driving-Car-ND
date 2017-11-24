# For loop and index
print("A less great way to loop through a list...")
for index in range(len(my_list)):
    item = my_list[index] # accessing an element in a list!
    print("item is", item)

# Slicing from front index
print("Slicing a list from beginning...")
for item in my_list[:3]:
    print("item is", item)

# Slicing to back index
print("Slicing a list to the end...")
for item in my_list[3:]:
    print("item is", item)

# Slicing in the middle
print("Slicing a list in the middle...")
for item in my_list[2:4]:
    print("item is", item)

# Enumerating
print("Enumerating a list...")
for i, item in enumerate(my_list):
    print("item number", i, "is", item)

# Another way
print("Another way to enumerate using a list 'method'...")
for item in my_list:
    index = my_list.index(item)
    print("item", item, "has index", index)
