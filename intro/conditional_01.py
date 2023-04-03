value = input('type number: ')
value_fmt = int(value)
type_value = type(value_fmt)
print('the value is {}'.format(value))
print('The type of value is {}'.format(type_value))

# the value 14 is greather than 10!
if value_fmt > 10:
    print("the value {} is greather than 10".format(value_fmt))
elif value_fmt < 10:
    print('The value {} is less than 10'.format(value_fmt))
    
else:
    print('The value {} is equals'.format(value_fmt))


"""
SE CONDICAO 1 FOR VERDADEIRA, ENTÃO:
    CASO 1
SENAO, SE A CONDICAO 2 FOR VERDADEIRA, ENTAO:(ELIF)
    CASO 2
SENÃO:
    CASO 3
"""