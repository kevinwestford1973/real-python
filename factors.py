# Assignment 5.3: Find the factors of a number


user_num = int(input('Enter an integer: '))

def find_factors(num):
    for i in range(1, num + 1):
        if num % i == 0:
            print("{} is a divisor of {}".format(i, num))

find_factors(user_num)
