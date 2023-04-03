# what juanito will do?
# 1 - watch a movie
# 2 - go to shoopping center
# 3 - make a barbecue
# 3 - go to the beach

# weather
# 1 - rainly
# 2 - sunly

# traffic
# 1 - heavy
# 2 - light
#######################################################
# Use ELIF when have multiple scenarios (individualmente)
# Use ELSE when have all other scenarios 
#######################################################

print('What juanito will do?')
print('Options weather')
print('1 - rainly')
print('2 - sunly')
weather = input('What is the weather? ')

print('Options traffic')
print('1 - heavy')
print('2 - light')
traffic = input('What is the traffic? ')

if (weather == 'rainly' or weather == '1') and (traffic =='heavy' or traffic == '1'):
    print('So Juanito will watch movie')

elif (weather == 'rainly' or weather == '1') and (traffic =='ligth' or traffic == '2'):
    print('So Juanito will go to the shopping center')

elif (weather == 'sunly' or weather == '2') and (traffic == 'heavy' or traffic == '1'):
    print('Them Juanito will make barbecue in his house')
    
elif (weather == 'sunly' or weather == '2') and (traffic == 'ligth' or traffic == '2'):
    print('Juanito will go to the Ipanema beach')


    

