a = "Hello"
b = 'world'
l = 4
c = f'{a} {b} {l}'
print(c)

y = 'Privet'.upper()
print(y)

x = 'Privet'.lower()
print(x)

k = 'python'.capitalize()
print(k)

u = ' Privet '
print(u.strip())

g = 'Priv4t t4b4'.replace('4', 'e')
print(g)

f = 'PriveT'.replace('t', '')
print(f)

r = 'PrivetR'.lower().replace('r', '').capitalize()
print(r)

t = 'Hello world!'.replace('world', 'python')
print(t)

b = 'learn.python.ru'
print(b.split('.'))

h = 'Predlojenie iz neskolkix word'
print(len(h.split()))