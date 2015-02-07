# 7.1 continued


my_input_file = open('hello.txt', 'r')
print('Line 0 (first line):', my_input_file.readline())
my_input_file.seek(0)
print('Line 0 again:', my_input_file.readline())
print('Line 1:', my_input_file.readline())
my_input_file.seek(8)
print('Line 0 (starting at 9th character):', my_input_file.readline())
my_input_file.seek(10, 1)
print('Line 1 (starting at 11th character):', my_input_file.readline())
my_input_file.close()

