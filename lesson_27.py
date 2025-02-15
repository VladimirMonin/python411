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

from time import sleep

for nums in string_nums:
    print(nums)
    sleep(0.5)
