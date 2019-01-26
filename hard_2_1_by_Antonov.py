# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y

a = equation.split(' ')
c = 0

for i in a:
    if 'x' in i:
        n = a.index(i)
        c = i.replace('x', ' ')
        a[n] = c
    elif 'y' in i:
        a.remove(i)

y = float(a[1]) * x + float(a[3])

print(f'Ответ: y = {y}')
