# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них

a = int(input('Input first number: '))
b = int(input('Input second number: '))
c = int(input('Input third number: '))


def compare(x, y, z):
    return max(x, y, z)


# compare = lambda *args: max(*args)

print(compare(a, b, c))
