# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

a = ["яблоко", "банан", "киви", "арбуз", "макароны", "спагетти"]
b = ["макароны", "спагетти", "булка"]
c = list(set([i for i in a + b if i in a and i in b]))
print(*c)
