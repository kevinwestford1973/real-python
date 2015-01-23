# Chapter 2.2
# Mess around with your words


# Using the len() function
myString = "abc"
length_of_string = len(myString)
print(length_of_string)

# Combining strings
string1 = 'abra'
string2 = 'cadabra'
magic_string = string1 + string2
print(magic_string)

# Combine strings without creating variables
# In programming, when you add strings together, 
# you say you *concatenate* them.
print('abra' + 'ca' + 'dabra')

# You can also combine strings using commas to separate them
print('abra', 'ca', 'dabra')

# Since a string is just a sequence of characters, we can access
# each character individually.

# Character:    b i r t h d a y c a ...
# Index:        0 1 2 3 4 5 6 7 8 9 ...
flavor = 'birthday cake'
print(flavor[3])

# We can also get a particular section or slice of a string by
# using square brackets and specifying the *range* of characters
# that we want.
print(flavor[0:3])  # --> outputs 'bir'
print(flavor[1:3])  # --> outputs 'ir'
                    #     flavor[1:3] says 'starting at index 1, give 
                    #     me the characters up to but not including index 3'

print(flavor[:5])   # --> outputs 'birth'
print(flavor[5:])   # --> outputs 'day cake'
print(flavor[:])    # --> outputs 'birthday cake'
                    # Using the colon says go all the way to the end of the
                    # string in that direction. But just like using ranges,
                    # the number on the left side of the colon is the starting
                    # index.

print('Review exercise')
horizontal_rule = len('review exercise')
print('-' * horizontal_rule)

some_string = 'bazinga'
print(some_string[2:6])
