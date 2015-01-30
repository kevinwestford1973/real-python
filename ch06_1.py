# Chapter 6
# Fundamentals: Lists and dictionaries

print('6.1 Make and update lists')
print()
print('Example list objects')
colors = ['red', 'green', 'burnt sienna', 'blue']
scores = [10, 8, 9, -2, 9]
my_list = ['one', 2, 3.0]

print(colors)
print(colors[2])
print()

print('Messing with list')
animals = []
print(animals)
animals.append('lion')
animals.append('tiger')
animals.append('frumious Bandersnatch')
print(animals)
print()

print('Removing lion')
animals.remove('lion')
print(animals)
print()

print('Using the index() method belonging to lists')
print('colors list:', colors)
print('Finding the index of "burnt sienna"')
print(colors.index('burnt sienna'))
print()

print('Reassigning lists (keep in mind lists are *mutable*)')
animals = ['lion', 'tiger', 'frumious Bandersnatch']
print('Putting large_cats = animals')
print()
large_cats = animals
print('animals list:', animals)
print('large_cats list:', large_cats)
print()
print('appending "Tigger" to large_cats')
large_cats.append('Tigger')
print('animals list:', animals)
print('large_cats list:', large_cats)
print()

why_comment = """ Both lists changed. Why?
Both large_cats and animals change even though we only appened to
large_cats because when we did animals = [...], it was only pointing our list
to an actual list object in the computer's memory. When we did
large_cats = animals, Python took large_cats and pointed it to the same list
object in memory instead of creating a whole new list object.

This wasn't a problem with strings because strings were *immutable*.

So, that means when we use list methods i.e. some_list.append('foo')
we don't need to reassign the list to itself since lists are mutable.

This is true for any method that belongs to a mutable object."""
print(why_comment)
print()
print('Converting strings into a list using string sort() method')
groceries ='eggs, spam, pop rocks, cheese'
grocery_list = groceries.split(', ')
print(grocery_list)

print('# 6.1 Review exercises')
desserts = ['ice cream', 'cookies']
desserts.sort()
print(desserts)
print(desserts.index('ice cream'))
food = desserts[:]
food.append('broccoli')
food.append('turnips')
print('desserts:', desserts)
print('food', food)
print()
food.remove('cookies')
print('First two items of food list:', food[0:2])
breakfast = 'cookies, cookies, cookies'.split(', ')
print(breakfast)
