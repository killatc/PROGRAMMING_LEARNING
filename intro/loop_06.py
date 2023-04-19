products = {}


id = 1
continue_loop = True 
while continue_loop:
    product = input('Product name: ')
    price = float(input('Price of the product: '))
                                             
    continue_input = input("Insert new product [Yes No]: ")
    while continue_input != 'Yes' and continue_input != 'No':
        print('Invalid Option, try again! ')
        continue_input = input("Insert new product [Yes No]: ")
   
    if continue_input == 'No':
        continue_loop = False
    item = {'name': product,'price': price}
    products[id] = item
    id+=1

#print('Products: {}'.format(products))
for code,product in products.items():
    print('code: {}'.format(code))
    print('name: {}'.format(product['name']))
    print('price: {}'.format(product['price']))
    print()

    