"""
15.02.2025
Тема: Генераторы и Итераторы. Урок: 27
"""
string = "Банан"
my_list = ["банан", "яблоко", "апельсин"]

"""
Служебные объекты-генераторы в Python
dict.keys()
dict.values()
dict.items()
range()
map()
filter()
zip() создает генератор из кортежей, объединяя
enumerate() генерирует пары индекс-значение
reversed() - генератор для обратного прохода по последовательности
"""

MIN_VALUE = 0
# OverflowError: Python int too large to convert to C ssize_t
# MemoryError
MAX_VALUE = 1_000_000_000_000_000

# nums_list = list(range(MIN_VALUE, MAX_VALUE))

range_nums = range(MIN_VALUE, MAX_VALUE)

# Обработка фильтром. Хочу четные числа
even_nums = filter(lambda x: x % 2 == 0, range_nums)

# Обработка MAP
string_nums = map(lambda x: str(x) + " число", even_nums)

# 7 нулей - десять миллионов
# Так как мы пишем только четные - это 5 миллионов записей
# Мой файл весит 100 мб
STOP_ITEM = "10000000 число"
# построчная запись в файл
# with open("nums.txt", "w", encoding="utf-8") as file:
#     for num in string_nums:
#         if num == STOP_ITEM:
#             break
#         file.write(num + "\n")


SEARCH_STRING = "9900982"

# Прочитаем построчно, поищем нужную строку и распечатаем
with open("nums.txt", "r", encoding="utf-8") as file:
    for line in file:
        if SEARCH_STRING in line:
            print(line.strip())
            break

