# Assignment 4.2: Convert temperatures


def convert_to_f(celsius_temp):
    return celsius_temp * 9 / 5 + 32

def convert_to_c(fahr_temp):
    return (fahr_temp - 32) * 5 / 9

test1 = convert_to_c(72)
test2 = convert_to_f(37)

print('72 degrees F = {} degrees C'.format(test1))
print('37 degrees C = {} degrees F'.format(test2))
