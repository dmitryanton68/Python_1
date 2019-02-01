# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов

def compare(*args):
    max_num = 0
    for i in args:
        if len(i) > max_num:
            max_num = len(i)
            result = i
    return result


print(compare('asd', 'jhvjh', 'jgfhjgfhf', 'jkjfhtrsesrqw'))
