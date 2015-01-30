# 6.3) Store relationships in dictionaries


print('6.3 Review exercises')
birthdays = {}

birthdays['Luke Skywalker'] = '5/24/19'
birthdays['Obi-Wan Kenobi'] = '3/11/57'
birthdays['Darth Vader'] = '4/1/41'

if 'Yoda' not in birthdays:
    birthdays['Yoda'] = 'unknown'

if 'Darth Vader' not in birthdays:
    birthdays['Darth Vader'] = 'unknown'

for person in birthdays:
    print(person, birthdays[person])

print()
del(birthdays['Darth Vader'])
print(birthdays)
print()

print('Bonus: make dict passing in initial values')
extra_birthdays = dict([('Princess', '12/25/19'), ('R2D2', 'unknown')])
print(extra_birthdays)
