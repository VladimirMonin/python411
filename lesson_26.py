"""
Тема: Функции. Аннотации типов. Typing. Декораторы. Урок: 26
"""

from typing import Callable


# Функция с кешированием

def cach_sorter() -> Callable[[list[str]], list[str]]:
    cach = []
    last_input = []
    
    def sorter(data: list[str]) -> list[str]:
        nonlocal cach, last_input
        if data != last_input:
            print('Делаем сортировку')
            cach = sorted(data)
            last_input = data.copy()
            return cach
        print("Возвращаем кеш!")
        return cach
    
    return sorter


sorter_ = cach_sorter()
shop_list = ["Iphone", "Ipad", "MacBook", "Пирожок"]

# Тестируем
print(sorter_(shop_list))
print(sorter_(shop_list))
shop_list.append("RTX5090")
print(sorter_(shop_list))
print(sorter_(shop_list))
