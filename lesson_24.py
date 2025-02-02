"""
Тема: Функции. Анонимные функции. Map Filter Sorted. Урок: 24
- синтаксис анонимных функций
"""
from marvel import small_dict, full_dict

def foo_0(x):
    return x + 10

foo = lambda x: x + 10

print(foo_0(10))
print(foo(10))
