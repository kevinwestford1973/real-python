# Chapter 7
# File Input and Output

print("7.1\) Read and write sample files")
print()

my_output_file = open('hello.txt', 'w')
my_output_file.writelines('This is my first file.')
my_output_file.close()

my_output_file = open('hello.txt', 'w')
lines_to_write = [
    'This is my first file.', 
    '\nThere are many like it,'
    '\nbut this one is mine.']
my_output_file.writelines(lines_to_write)
my_output_file.close()

my_output_file = open('hello.txt', 'a')
next_line = ('\nNON SEQUITUR!\n')
my_output_file.writelines(next_line)
my_output_file.close()

my_input_file = open('hello.txt', 'r')
print(my_input_file.readlines())
my_input_file.close()

print('Using loop with readlines()')
my_input_file = open('hello.txt', 'r')
for line in my_input_file.readlines():
    print(line, end='\n')
my_input_file.close()
print()

print('Using readline() method')
my_input_file = open('hello.txt', 'r')
while line != '':
    print(line)
    line = my_input_file.readline()
my_input_file.close()

print('Using Python with keyword')
with open('hello.txt', 'r') as my_input_file:
    for line in my_input_file.readlines():
        print(line, end=",")

print('Using Python "with" keyword and multiple statements')
with open('hello.txt', 'r') as my_input, open('hi.txt', 'w') as my_output:
    for line in my_input.readlines():
        my_output.write(line)

