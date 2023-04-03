"""
int %d
------
1, 5, 150...
Ex1.: number = 42

float %f %.6f
------
1.55, 0.5, 18543.3215, ....
Ex1.: decimal = 26.38

str
------
'edith', "edith"
Ex1.: age = '502822222'
Ex2.: sentece = "hola baby"

bool
------
True and False (1 and 0)
Ex1.: value_valid = True
Ex2.: is_empty = False
"""
name = "Edith"
name1 = 'Tueros'
print('hello,', name, 'how are you?')
print ("Hello, %s %s How are you doing?"%(name,name1))
print ('hi {} {}, are you cute'.format(name,name1))
print (f'{name} {name1}: I am verry happy')