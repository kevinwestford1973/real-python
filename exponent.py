# Assignment 4.1


print('This script will raise a given base number to a given power')
base = input('Enter a base: ')
power = input('Enter an exponent: ')
result = float(base) ** float(power)
print("{b} to the power of {p} is {ans}".format(b=base, p=power, ans=result))
