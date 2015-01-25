# 3.3) Find a string in a string


# string method find()
# Since it belongs to string, we call it using dot notation
# e.g. some_string.find('string to find')

# Keep in mind it is case sensitive. if it finds a match, it will return the
# index of the first occurrent of that string. 
phrase = 'the surprise is in here somewhere'
print(phrase.find('surprise')) 
# >>> 4

# If it finds nothing, it will return -1 instead.
print(phrase.find('asdfasdfasd')) 
# >>> -1

# You can call the string methods on string literals
print('another surprise is in here somehwere'.find('surprise')) # >>> 8

# The part of the string we're looking for is called a 'substring'
# If the substring appears more than once, it will return only
# the first appearance.

# find() will **only** accept a string as input
phrase_2 = 'My number is 555-555-5555'
# print(phrase.find(5)) 
# >>> TypeError: Can't convert 'int' object to str implicitly

print(phrase_2.find('5')) # >>> 13

# replace() - another string method
# replaces all occurrences of one substring with a different substring

my_story = "I'm telling you the truth; he spoke nothing but the truth!"

# replace all occurrences of 'truth' with 'lies'
print(my_story.replace('the truth', 'lies'))
# >>> I'm telling you lies; he spoke nothing but lies!

# Keep in mind that calling replace() didn't actually change myStory
# If you want to do that you have to reassign it a new value
print(my_story)
# >>> I'm telling you the truth; he spoke nothing but the truth!
my_story = my_story.replace('the truth', 'lies')
print(my_story)
# >>> I'm telling you lies; he spoke nothing but lies!


# 3.3 review exercises
print('3.2 Review exercises')
print('AAA'.find('a'))

version = 'version 2.0'
the_number = 2.0
print(version.find(str(the_number)))

user_input = input('Give me a phrase: ')
index = user_input.find('x')

if index > 0:
    print('The letter x is at {}'.format(index))
else:
    print('The letter was not found')
