# 5.4) Break out of the pattern


print('Example')
for i in range(0, 4):
    if i == 2:
        break
    print(i)
print('Finished with i =', str(i))
print('Example complete')

print('Review exercise')
while True:
    user_input = input('Type q or Q if you want to quit: ')
    if user_input.lower() == 'q':
        break

for i in range(1, 51):
    if i % 3 == 0:
        continue
    print(i)

