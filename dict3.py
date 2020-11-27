product = {
    'name': 'iPhone Xs',
    'stock': 24,
    'price': 65432.1
}

print(len(product))

#add column and modify
product['memory'] = 64
print(product)
product['name'] = 'iPhone Xs Plus'
print(product)

print(product['price'])
print(product['stock'])

#print(product['discount']) --esli net key, to error

print(product.get('name'))
print(product.get('discount'))

print(product.get('discount', 0))
print(product.get('country', 'US'))

#delete
del product['memory']
print(product)

#del product['discount'] -esli net key, to error

phones = ['Samsung Galaxy S10', 'iPhone Xs']
product['recomended'] = phones
print(product)

print(product['recomended'])
product['recomended'].append('Xiaomi Mi8')
print(product)
print(len(product['recomended']))

print(product['recomended'][0])

#dict
stock = [
    {'name': 'iPhone Xs Plus', 'stock': 24, 'price': 65432.1,
     'recomended': ['Samsung Galaxy S10', 'iPhone Xs']},
    {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0, 'discount': 5000},
    {'name': 'Xiaomi Mi8', 'stock': 42, 'price': 38000.5}
]

print(stock[2])

stock[2]['price'] = stock[2]['price'] - 8000
print(stock[2]['price'])
print(stock[0]['recomended'][1])

print(type(stock))
print(type(stock[0]))