"""
for i in range(0, 10):
    print(i)

for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print(i)

list_range = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in list_range:
    print(i)

    1 - Tallarin Saltado
id is an identifier
"""

foods_list = ['Tallarin Saltado', 'Arroz chaufa', 'Olluquito', 'Menestron']
print('Manual enumarate')
id = 1
for food in foods_list:
    print('{} - {}'.format(id,food))
    id = id+1

print('Improved enumerate')
for new_id, food in enumerate(foods_list):
    print('{} - {}'.format(new_id+1,food))


