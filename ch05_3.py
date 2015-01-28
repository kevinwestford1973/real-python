# 5.3) Control flow of your program


print('Example if statement')
if 2 + 2 == 4:
    print('2 and 2 is 4')
    print('Arithmetic works.')
else:
    print('2 and 2 is not 4')
    print('Big Brother wins.')
print()

print('Example if elif statement')
num = 10
if num < 10:
    print('number is less than 10')
elif num > 10:
    print('number is greater than 10')
else:
    print('number is equal to 10')
print()

print('5.3 Review exercise')
word = input('Give me a word: ')
if len(word) < 5:
    print('The length of the word is less than 5.')
elif len(word) > 5:
    print('The length of the word is greater than 5.')
else:
    print('The length of the word is equal to 5.')
