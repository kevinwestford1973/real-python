# 4.3) Run in circles


print('while loop example')
n = 1
while (n < 5):
    print("n =", n)
    n = n + 1
print('Loop finished\n')

print('for loop example')
for n in range(1, 5):
    print('n =', n)
print('Loop finished\n')

print('loops inside of loops example')
for n in range(1, 4):
    for j in (['a', 'b', 'c']):
        print('n =', n, 'and j =', j)
print('Loop finished\n')

print('for loop that prints 2 through 10 using range() function')
for n in range(2, 11):
    print(n)
print('Loop finished\n')

print('while loop that prints 2 through 10')
n = 2
while n < 11:
    print(n)
    n += 1
print('Loop finished\n')

print('doubles() function that double a number three times)')
def doubles(num):
    num = num * 2
    for n in range(0, 3):
        print(num)
        num = num * 2
doubles(2)
print('doubles() function finished\n')

