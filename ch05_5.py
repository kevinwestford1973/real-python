# 5.5) Recover from errors


print('5.5 Review exercise')
while True:
    try:
        number = int(input('Type an integer: '))
        print(number)
        break
    except ValueError:
        print('Try again')
