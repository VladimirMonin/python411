"""
01.02.2025

Тема: ООП Ч8. Разбор ДЗ. Погружение в Dataclasses Урок: 23

- Магические методы математика
- __add__ - сложение
- __sub__ - вычитание
- __mul__ - умножение
- __truediv__ - деление
- __floordiv__ - целочисленное деление
- __mod__ - остаток от деления
- __pow__ - возведение в степень
- __abs__ - модуль числа
- __round__ - округление
- __ceil__ - округление вверх
- __floor__ - округление вниз
- __int__ - преобразование в целое число
- __float__ - преобразование в число с плавающей точкой

Инплейс операции

- __iadd__ - +=
- __isub__ - -=
- __imul__ - *=
- __itruediv__ - /=
- __ifloordiv__ - //=

- __str__ - строковое представление объекта
- __repr__ - строковое представление объекта для разработчика


СРАВНЕНИЕ НА БОЛЬШЕ МЕНЬШЕ
- less then - __lt__ - меньше чем <
- great then - __gt__ - больше чем >
- less or equal - __le__ - меньше или равно <=
- great or equal - __ge__ - больше или равно >=
- equal - __eq__ - равно ==
- not equal - __ne__ - не равно !=


Достаточно 2 магических метода чтобы Python просчитал остальные
eq - равенство
lt - меньше чем

from functools import total_ordering
"""

# ДАТАКЛАССЫ

from dataclasses import dataclass, field

@dataclass(order=True)
class MusicCompositionData:
    name: str = field(compare=False)
    author: str = field(compare=False)
    year: int = field(compare=False)
    duration: int


composition1 = MusicCompositionData(
    name="Nothing Else Matters",
    author="James Hetfield, Lars Ulrich",
    year=1991,
    duration=290,
)

# Создание экземпляра для песни "Nothing Else Matters" (Apocalyptica)
composition2 = MusicCompositionData(
    name="Nothing Else Matters",
    author="James Hetfield, Lars Ulrich (исполнение Apocalyptica)",
    year=1996,
    duration=490,  # Длительность в секундах (6 минут 30 секунд)
)

# Распечатаем
print(composition1)
# Repr распечатаем
print(repr(composition1))
# MusicCompositionData(name='Nothing Else Matters', author='James Hetfield, Lars Ulrich', year=1991, duration=290)

print(composition1 == composition2)
print(composition1 < composition2)


compositions_list = [composition1, composition2]

#PRACTICE 
"""
Сделайте 3 экземпляра датакласса MusicCompositionData
Поместите их в список
Попробуйте сравнить на больше меньше 2 из них
Попробуйте применить к списку .sort() c reverse=True и без него

"""