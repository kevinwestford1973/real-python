# 7.1 Review exercises


print('7.1 review exercises')

print('Looping through using readlines() method')
input_file = open('poem.txt', 'r')
for line in input_file.readlines():
    print(line)
input_file.close()
print()

print('Reading a file using "with" keyword')
with open('poem.txt', 'r') as input_file:
    for line in input_file.readlines():
        print(line)
print()

print('Write text file "output.txt" that contains same lines as "poem.txt"')
input_file = open('poem.txt', 'r')
output_file = open('output.txt', 'w')
for line in input_file.readlines():
    output_file.writelines(line)
input_file.close()
output_file.close()
print()

print('Do previous exercise using "with" keyword')
with open('poem.txt', 'r') as input_file:
    with open('output.txt', 'w') as output_file:
         for line in input_file.readlines():
             output_file.writelines(line)
print()

file_to_append = open('output.txt', 'a')
next_line = file_to_append.writelines('Add this to the end')
file_to_append.close()
