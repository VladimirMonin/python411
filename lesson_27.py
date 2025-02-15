"""
15.02.2025
Тема: Генераторы и Итераторы. Урок: 27
- встроенные в Python генераторы
- отличие генераторов от списков
- работа с большими последовательностями (нехватка ОЗУ)
- передача генераторов из одного в другой (цепочка генераторов)
- генераторы в функциях и yield
- аннотация типов для генераторов
- генераторы Generator[YieldType, SendType, ReturnType]
- send в циклах
- итераторы классы
- тест 
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

from random import choice
from typing import Generator

fruit_list = ["яблоко", "банан", "апельсин", "груша", "киви", "ананас", "мандарин", "персик", "грейпфрут"]

class CoctailGenerator:
    def __init__(self, products: list[str]):
        self.products = products
        
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.products:
            raise StopIteration
        
        fruit = choice(self.products)
        # Удаляем выбранный фрукт из списка
        self.products.remove(fruit)
        return f'{fruit.title()} использован(а)'
    

# Тестируем
coctail_gen = CoctailGenerator(fruit_list)

for coctail in coctail_gen:
    print(coctail)
