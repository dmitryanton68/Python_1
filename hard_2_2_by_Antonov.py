# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
date = '01.11.1985'

# Примеры некорректных дат
# date = '01.22.1001'
# date = '1.12.1001'
# date = '-2.10.3001'

a = date.split('.')

month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if len(a[0]) == 2 and len(a[1]) == 2 and len(a[2]) == 4 and 0 < int(a[1]) < 12:
    if a[0].isdigit() and 0 < int(a[0]) < month[int(a[1]) - 1] and 1 < int(a[2]) < 9999:
        print(f'Дата {date} записана корректно.')
    else:
        print(f'Дата {date} записана НЕкорректно.')
else:
    print(f'Дата {date} записана НЕкорректно.')
