value = int(input('Show the Age: '))

# This is when the conditional is "Chained" 
print('CHAINED CONDITIONAL')
if value >= 18:
    if value < 60:
        print('The vote is mandatory for Age {}'.format(value))
    else:
        print('The vote is not mandatory for Age {} beacuse is greather than 59'.format(value))
else:
    print('The vote is not mandatory for Age {} beacuse is less than 18'.format(value)) 


# This is when the conditionals are aggregated
print("CONDITIONAL AGGREGATED")
if value >= 18 and value < 60:
    print(' So the vote is mandatory for Age {}'.format(value))
else:
    print('The vote is not mandatory for Age {} beacuse is less than 18 or greather than 59'.format(value))