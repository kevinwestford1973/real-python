# 3.2) Streamline your 'print' statements


# Another way to combine strings together is the string format() method

# 3.2 review exercises
weight = 0.2
animal = 'newt'

print('Print without using the format() string method')
print(str(weight), "kg is the weight of the", animal)
print()
print('Print using format() and empty {}')
print('{} kg is the weight of the {}.'.format(weight, animal))
print()
print('Print using {} place-holders and index numbers')
print('{0} kg is the weight of the {1}.'.format(weight, animal))
print()
print('Print using new string and float objects inside the format() method')
print('{a_weight} kg is the weight of the {a_animal}.'.format(a_weight=0.2,
                                                              a_animal='newt'))
