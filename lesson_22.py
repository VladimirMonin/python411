"""
26.01.2025

Тема: ООП Ч7. Магические методы. Математика. Сравнение. Знакомство с Dataclasses Урок: 22

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
"""

class MusicComposition:
    def __init__(self, name:str, author:str, year:int, duration:int):
        self.name = name
        self.author = author
        self.year = year
        self.duration = duration


class PlayList:
    def __init__(self, name):
        self.name = name
        self.tracks: list[MusicComposition] = []



composition1 = MusicComposition(
    name="Nothing Else Matters",
    author="James Hetfield, Lars Ulrich",
    year=1991,
    duration=390
)

playlist = PlayList(name="Best of Metallica")

# Это не работает - нет описания логики сложения и инплейс сложения
# playlist + composition1
# playlist += composition1
