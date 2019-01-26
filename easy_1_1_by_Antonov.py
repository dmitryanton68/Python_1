# Задача-1: поработайте с переменными, создайте несколько,
# выведите на экран, запросите от пользователя и сохраните в переменную, выведите на экран

a = int(input("Input number a = "))
b = float(input("Input number b = "))
c = str('opa')
print(a, b, c)

d = bool(1)
dd = bool(0)
print(d, dd)

e = [a, b, c]
print(type(e))
print(e)

f = (11, 22, 33)
print(type(f))
print(f)

g = {'first': a, 'second': b, 'third': c}
print(type(g))
print(g['third'])
