# 5.6) Simulate events and calculate possibilities
from random import randint

print('Review exercise')
print()

print('Simulate die toss')
print(randint(1, 6))
print()

print('Average of 10,000 die tosses')
sum = 0
for throw in range(0, 10000):
    toss = randint(1, 6)
    sum += toss
average = sum / 10000
print('The average of 10,000 die tosses was {}'.format(average))
print()
