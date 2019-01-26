# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.


def person(_name, health, damage):
    a = ['name', 'health', 'damage']
    b = [_name, health, damage]
    person = dict(zip(a, b))
    return person


person1 = person('Vasya', 100, 50)
person2 = person('Fascist', 90, 40)
print("Было: ")
print(person1, person2, sep='\n')


def attack(person1, person2):
    d = person1['damage']
    h = person2['health']
    person2['health'] = h - d
    return person2


person2 = attack(person1, person2)

print(" ")
print("Стало: ")
print(person1, person2, sep='\n')
