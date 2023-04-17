stock_foods = {
    'chuño': 10,
    'Papas nativas': 20,
    'Helado de lucma': 2,
    'Maca': 15,
    'Chocolate princesa': 24
}

for product, amount in stock_foods.items():
    print('Product: {}'.format(product))
    print('Amount: {}'.format(amount))

    if amount < 10:
        print('Status: Critical')
    elif amount >= 10 and amount < 20:
        print("Status: Attention")
    else:
        print('Status: Normal')

    print()