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

# Мы можем определить ссылку на функцию. При этом функция без ВЫЗОВА!
banana = print
banana("Привет!")


def search_string(string):
    return "чел" in string.lower()

def my_filter(func, iterable):
    result = []

    for item in iterable:
        if func(item):
            result.append(item)

    return result

result_list_3 = my_filter(search_string, simple_list)



result_list_3 = list(filter(search_string, simple_list))

result_list_3 = list(filter(lambda film: "чел" in film.lower(), simple_list))

print(result_list_3)

######## MAP  ##########

# 4. Обход с помщью map, comprehension коллекций

result_list_4 = []

for film in simple_list:
    result_list_4.append(film.replace(' ', '_').lower())

result_list_4 = [film.replace(' ', '_').lower() for film in simple_list]

result_list_4 = list(map(lambda film: film.replace(' ', '_').lower(), simple_list))

print(result_list_4)

# 5. Опциональная обработка. Делаем эту работу ЕСЛИ в фильме есть пробел, оставляем как есть если пробела нет

result_list_5 = []

for film in simple_list:
    if ' ' in film:
        result_list_5.append(film.replace(' ', '_').lower())
    else:
        result_list_5.append(film)

result_list_5 = [film.replace(' ', '_').lower() if ' ' in film else film for film in simple_list]

result_list_5 = list(map(lambda film: film.replace(' ', '_').lower() if ' ' in film else film, simple_list))

print(result_list_5)


# 6. КОМБО! Опциональная обработка + фильтрация элементов
# ФИЛЬТР - строки длиннее 15 символов
# ОБРАБОКТА - ТАКАЯ ЖЕ

result_list_6 = []

for film in simple_list:
    if len(film) > 15:
        if ' ' in film:
            result_list_6.append(film.replace(' ', '_').lower())
        else:
            result_list_6.append(film)

result_list_6 = [film.replace(' ', '_').lower() if ' ' in film else film for film in simple_list if len(film) > 15]

result_list_6 = list(map(lambda film: film.replace(' ', '_').lower() if ' ' in film else film, filter(lambda film: len(film) > 15, simple_list)))

print(result_list_6)


# Получить список чисел от пользователя
num_list = map(int, input("Введите числа через пробел: ").split())
num_list1 = [int(num) for num in input('Введите числа через пробел: ').split()]

# Принт в комприхенш
[print(n) for n in num_list]
