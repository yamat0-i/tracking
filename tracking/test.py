def func(a, b, c):
    x = a + b
    y = b + c
    return x, y

a = 1
b = 2
c = 10

l, m = func(a, b, c)

print('l:', l)
print('type(l):', type(l))
print('m:', m)
print('type(m):', type(m))