phones = ['iPhone Xs', 'Samsung Galaxy S10', 'Xiaomi Mi8']
print(phones)
print(len(phones))

phones.append('iPhone Xs')
print(len(phones))

print(phones.count('iPhone Xs'))
print(phones.count('iPhone 9'))

print(phones[1])
#print(phones[6]) --net takogo index

print(phones[1:3])
print(phones[:2])
print(phones[-1])

print(phones.index('Xiaomi Mi8'))
phones.sort()
print(phones)
print(phones.index('Xiaomi Mi8'))

print('iPhone Xs' in phones)
print('iPhone 6' in phones)

del phones[1]
print(phones)
phones.remove('iPhone Xs')
print(phones)
#phones.remove('Xiaomi Mi8') --esli net value to vidaet error (udalili cherez del)