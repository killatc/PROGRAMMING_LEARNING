"""
Output:
Option 1
Food: xxxxxxx
Drink: xxxxxxxx

Option 2:
Food: yyyyyyy
Drink: yyyyyy

....
"""
foods = ['Lomo saltado','Arroz con Pato', 'Pescado a lo macho']
drinks =['Coffee','Pisco sour','Lemonade']
# id = 1
# for i in range(0,len(foods)):
#     for j in range(0, len(drinks)):
#         food = foods[i]
#         drink = drinks[j]
#         print('Option {} \nFood: {} \nDrink: {}\n'.format(id,food, drink))
#         id = id +1

id = 1
for food in foods:
    for drink in drinks:
        print('Option {}:\n Food: {}\n Drink: {}\n'.format(id,food,drink))
        id +=1

