# 4.2 Create your own functions

def square(number):
    sqr_num = number ** 2
    return sqr_num

input_num = 5
output_num = square(input_num)
print(output_num)

def return_difference(num1, num2):
    '''Return the difference between two numbers.
       Subtracts num2 from num1.'''
    return num1 - num2

'''
Once a function returns a value with the 'return' command, the function is
done running. So, any code run after the 'return' statement will never be run.
'''
print(return_difference(3, 5))

### Review Exercises
def cube(number):
    return number * number * number

print(cube(8))
print(cube(12))
print(cube(3))

def multiply(num1, num2):
    return num1 * num2

result = multiply(2, 5)
print(result)
