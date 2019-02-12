# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

def current_dir_name():
    return os.getcwd()

def dir_making(name):
    dir_path = os.path.join(current_dir_name(), f'{name}')
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        print('Такая директория уже существует')

def dir_delete(name):
    os.rmdir(name)

for i in range(1, 10):
    name = f'dir_{i}'
    dir_making(name)

for i in range(1, 10):
    name = f'dir_{i}'
    dir_delete(name)

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def look_into_current_dir():
    lst_from_dir = os.listdir(path=f"{os.getcwd()}")
    return lst_from_dir

def checking_isdir(name):
    if os.path.isdir(name):
        print(name)

lst = look_into_current_dir()
print(f'Текущая директория содержит папки:')
for i in lst:
    checking_isdir(i)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import shutil, sys

shutil.copy(sys.argv[0], f'{sys.argv[0].split(".")[0]}_copy.py')
