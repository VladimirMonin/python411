"""
Тема: Функции. Аннотации типов. Typing. Декораторы. Урок: 26
"""

from typing import Callable


def fucn(a):
    # a - хранится тут
    def inner():
        # a - используется тут
        print(a)
    return inner

banan = print
banan("Привет!")

# Вызов функции 8
foo = fucn("пирожок")
foo()

# Функция счетчик - работающая на замыканиях

def counter(start_value: int) -> Callable[[], int]:
    def step() -> int:
        nonlocal start_value
        start_value += 1
        return start_value
    return step

# Создаем пару счетчиков с разным стартовым значением

counter1 = counter(10)
counter2 = counter(20)

print(counter1())
print(counter2())
print(counter1())
print(counter2())
print(counter1())
print(counter2())
