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

- __str__ - строковое представление объекта
- __repr__ - строковое представление объекта для разработчика
"""

class MusicComposition:
    def __init__(self, name:str, author:str, year:int, duration:int):
        self.name = name
        self.author = author
        self.year = year
        self.duration = duration

    def __str__(self):
        return (
            f"Название: {self.name}\n"
            f"Автор: {self.author}\n"
            f"Год выпуска: {self.year}\n"
            f"Продолжительность: {self.duration}"
        )
    
    def __repr__(self):
        return f"MusicComposition(name='{self.name}', author='{self.author}', year='{self.year}', duration='{self.duration}')"


class PlayList:
    def __init__(self, name):
        self.name = name
        self.tracks: list[MusicComposition] = []

    def __len__(self):
        return len(self.tracks)
    
    def __str__(self):
        return f"Название плейлиста: {self.name}\n" f"Количество треков: {len(self)}"
    
    def __iadd__(self, other: MusicComposition) -> "PlayList":
        if not isinstance(other, MusicComposition):
            raise TypeError("Неверный тип данных")
        self.tracks.append(other)
        return self
    
    def __add__(self, other: MusicComposition) -> "PlayList":
        return self.__iadd__(other)
    


composition1 = MusicComposition(
    name="Nothing Else Matters",
    author="James Hetfield, Lars Ulrich",
    year=1991,
    duration=390
)

# Создание экземпляра для песни "Nothing Else Matters" (Apocalyptica)
composition2 = MusicComposition(
    name="Nothing Else Matters",
    author="James Hetfield, Lars Ulrich (исполнение Apocalyptica)",
    year=1996,
    duration=390  # Длительность в секундах (6 минут 30 секунд)
)

playlist = PlayList(name="Best of Metallica")

playlist += composition1
playlist = playlist + composition2

print(playlist)

compositions = [composition1, composition2]
print(compositions)
print(compositions[0])

# Получим строковое представление объекта из repr
rep = repr(composition1) # MusicComposition(name=Nothing Else Matters, author=James Hetfield, Lars Ulrich, year=1991, duration=390)

obj = eval(rep)    # Выполнит строку как python код

