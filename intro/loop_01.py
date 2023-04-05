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



fruits_list = ['apple', 'pear', 'pinaple', 'banana']
fruits_list.append('mango')
print('Fruit from list is: {}'.format(fruits_list[4]))


fruits_tuple = ('apple', 'pear', 'pinaple', 'banana') 
print('Fruit from tuple is: {}'.format(fruits_tuple[2]))