"""
Тема: Функции. Анонимные функции. Map Filter Sorted. Урок: 24
- синтаксис анонимных функций
"""
from marvel import small_dict, full_dict, simple_set

def foo_0(x):
    return x + 10

foo = lambda x: x + 10

print(foo_0(10))
print(foo(10))

# 1. Сделаю список из Simple set
simple_list = list(simple_set)

# 2. Обход циклом simple_list
new_simple_list = []

for film in simple_list:
    new_simple_list.append(film)

# list comprehension
new_simple_list = [film for film in simple_list]


# 3. Мы хотим это отфильтровать (фильмы с "чел" в названии)
result_list_3 = []

for film in simple_list:
    if 'чел' in film.lower():
        result_list_3.append(film)

# list comprehension
result_list_3= [film for film in simple_list if 'чел' in film.lower()]

# filter - функция высшего порядка.
# Высшего порядка - значит она принемает в себя другую функцию.
# Принемает 2 аргумента: функцию и итерируемый объект.
# Функция должна вернуть булево

def search_string(string):
    return "чел" in string.lower()

result_list_3 = list(filter(search_string, simple_list))

result_list_3 = list(filter(lambda film: "чел" in film.lower(), simple_list))

print(result_list_3)