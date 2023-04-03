number = int((input('Type a number: ')))

#print if number has one digit or another digits, iclude negative numbers
if number >= -9 and number <= 9:
    print('The number {} has one digit'.format(number))
else:
    print('The number {} has more than one digit'.format(number))
    