def format_price(price):
    pr = int(price)
    return f"Цена: {pr} руб."


number = 56.24
print(format_price(number))


def discounted(price, discount):
    price_with_discount = price - (price * discount / 100)
    print(price_with_discount)


price1 = 100
discount1 = 10
discounted(price1, discount1)

def discounted2(price, discount):
    price = abs(float(price))
    discount = abs(float(discount))
    if discount >= 100:
        price_with_discount = price
    else:
        price_with_discount = price - (price * discount / 100)
    return price_with_discount

#price2 = 100
#discount2 = 180
#discounted2(price2, discount2)

product = {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0, 'discount': 5}
product['price_discounted'] = discounted2(product['price'],product['discount'])
print(product)

def discounted3(price, discount, max_discount=20):
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    if max_discount > 99:
        raise ValueError('Slishkom bolshoe max skidka')
    if discount >= max_discount:
        return price
    else:
        return price - (price * discount / 100)