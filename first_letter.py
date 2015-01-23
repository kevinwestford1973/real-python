# Assignment 2.3: Pick apart your user's input

"""
Write a script that prompts the user for input. Then determine the first
letter of that input, convert it to upper-case, and display it to
the user.
"""


user_input = input('Tell me your password: ')
first_letter_uppercased = user_input[0].upper()
print('The first letter you entered was:', first_letter_uppercased)
