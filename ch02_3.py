# Chapter 2.3
# Use objects and methods


# Methods are just functionts that *belong* to objects and are called 
# with () using dot notation: my_object.some_method()
# 
# len() function was called differently because it is a general purpose
# function that can ge called on many different objects but it doesn't
# *belong* to one single object.

# Playing with string methods
loud_voice = 'Can you hear me yet?'
print(loud_voice.upper())

user_input = input("Hey, what's up? ")
print('You said:', user_input)

response = input('What should I shout? ')
response = response.upper()
print('Well if you insist...', response)

review_header = 'Review exercises'
print(review_header)
print('-' * len(review_header))

whisper_phrase = input('What should I whisper? ').lower()
print("I'm going to whisper:", whisper_phrase)
