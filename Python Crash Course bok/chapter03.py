# About lists

kids = [ 'victoria', 'arthur', '"The third one..."']
# Print the entire list in an ugly way:
print(kids)

# Print one item:
print(kids[0])
print(kids[0].title())

# Accessing the last element is by using -1, second last by -2 etc.:
print(kids[-1])

# Example with a f-string and a list:
msg = f"My second kid was {kids[1].title()}"
print(msg)

# Now naming the third kid (changing an item in a list):
kids[-1]='Elmar'
print(kids[-1])

# Aaaand having a fourth kid:
kids.append('"yet another"')
print(kids)

# This can be used for easily adding to even an empty list:
animals=[]
animals.append('nyx')
animals.append('niké')
animals.append('kit')
print(animals)

# But if I would like an ooold animal to be inserted first now:
animals.insert(0, 'nelli')
animals.insert(1, 'mulle')
# Hey, there were a few more even before again:
animals.insert(0, 'stribemis')
animals.insert(1, 'gråmis')
animals.insert(2, 'shiela')
# And one more again!:
animals.insert(2, 'vicky')
print(animals)

# But a few of them are no more, and can be removed by using:
del animals[5]
del animals[4]
del animals[3]
del animals[2]
del animals[1]
del animals[0]
print(animals)

# We could also "pop" an item, removing the last one into a popped variable, e.g.
youngest_animal=animals.pop()
print(youngest_animal)
# So now kit is removed from animals, which actually makes animals just the cats:
cats=animals
print(cats)

# We can also pop from the beginning:
oldest_animal=animals.pop(0)
print(oldest_animal)

# If we know the value of an item, we can also just remove it by the value:
kids.remove('"yet another"')
print(kids)

# Sorting lists can be done by using sort, e.g. alphabetically:
kids.sort()
print(kids)
# or reversed:
kids.sort(reverse=True)
print(kids)

# To just represent a sorted list for a while, without actually changing the list, use sorted instead:
print(kids)
print(sorted(kids))

# Reversing a list completely is by using:
print(kids)
kids.reverse()
print(kids)

# Finding the lenght of a list:
print("I have "+str(len(kids))+" kids!")

