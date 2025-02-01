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
    name="Последний Герой",
    author="Виктор Цой",
    year=1987,
    duration=390,
)

# Создание экземпляра для песни "Nothing Else Matters" (Apocalyptica)
composition2 = MusicCompositionData(
    name="Группа Крови",
    author="Кино",
    year=1982,
    duration=290,
)

# Создание экземпляра для песни "Nothing Else Matters" (Apocalyptica)
composition3 = MusicCompositionData(
    name="Elevation",
    author="U2",
    year=1991,
    duration=270,
)

music_list = [composition1, composition2, composition3]

music_list.sort()
print(music_list)
print(f'{"*"*20}')
music_list.sort(reverse=True)
print(music_list)


# PRACTICE
"""
Сделайте 3 экземпляра датакласса MusicCompositionData
Поместите их в список
Попробуйте сравнить на больше меньше 2 из них
Попробуйте применить к списку .sort() c reverse=True и без него

"""


# Dataclass city


@dataclass
class City:
    name: str
    population: int
    is_used: bool = field(default=False)


##### Проверка проблемы общих коллекций


@dataclass
class Employee:
    name: str
    age: int
    position: str
    hourly_rate: float
    worked_hours: list = field(default_factory=list)

    def get_salary(self):
        return self.hourly_rate * sum(self.worked_hours)


direcotor = Employee("Bob", 60, "Director", 100)

worker = Employee("Alice", 30, "Worker", 20)

# Добавим Alice часы
worker.worked_hours.append(8)
worker.worked_hours.append(8)
worker.worked_hours.append(8)

print(worker.worked_hours)
print(direcotor.worked_hours)
# Проверим зарплаты
print(worker.get_salary())
print(direcotor.get_salary())