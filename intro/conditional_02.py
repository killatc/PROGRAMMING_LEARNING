value1 = input('Type number 1: ')
value_fmt1 = int(value1)

value2 = input('Type number 2: ')
value_fmt2 = int(value2)

if value_fmt1 > value_fmt2:
    print('Them the number {} greather than {}'.format(value_fmt1,value_fmt2))
elif value_fmt1 < value_fmt2:
    print('Them the number {} less than {}'.format(value_fmt1,value_fmt2))

# else:
#     print('So the number {} equals to {}'.format(value_fmt1,value_fmt2))
elif value_fmt1 == value_fmt2:
    print('Entonces el valor {} es igual que valor{}'.format(value_fmt1,value_fmt2))


