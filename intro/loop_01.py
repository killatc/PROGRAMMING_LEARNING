"""
range(start, end-1)
start and end are required
ex. range(1, 11)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

range(start, end-1, step)
ex. range(1, 11, 2)
[1, 3, 5, 7, 9]

list (mutable)
fruits = ['apple', 'pear', 'pinaple', 'banana']
fruits.append('mango') (correct)
print('fruit is: {}'.format(fruits[4]))


tuple (unmutable)
fruits = ('apple', 'pear', 'pinaple', 'banana')
fruits.append('mango') (incorrect)
print('fruit is: {}'.format(fruits[2]))
"""
# for number in range(10, 0, -2):
#     print('Number: {}'.format(number))



fruits_list = ['Apple', 'Pear', 'Pinaple', 'Banana']
fruits_list.append('Mango')
print('Fruit from list is: {}'.format(fruits_list))
print('Running List')


# 1 - apple
# 2 - pear
# 3 - pinaple
#...
len_list = len(fruits_list)
for i in range(0, len_list):
    print('{} - {}'.format(i+1, fruits_list[i]))


fruits_tuple = ('Peach', 'Blueberry', 'Grape', 'Orange') 
print('Fruit from tuple is: {}'.format(fruits_tuple))

print('Running Tuple')
len_tuple = len(fruits_tuple)
for i in range(0, len_tuple):
    print('{} - {}'.format(i+len_list+1, fruits_tuple[i]))
