"""
Lesson 17
11.01.2025
Инкапсуляция. Приватные методы и атрибуты.
"""

class Car:
    def __init__(self, color: str, mark: str, serial_number: int):
        self.color = color
        self.mark = mark
        self.__serial_number = serial_number

    def __str__(self):
        return f'Автомобиль {self.mark}.\nСерийный номер {self.__serial_number}'

"""
Два уровня сокрытия атрибута или метода
_ - защищенный - условно нет доступа из вне. Есть доступ у наследников
__ - приватный - сложный доступ из вне. Нет доступа у наследников
"""

car = Car("черный", "Ёмобиль", 777)
# print(car.__serial_number) # AttributeError: 'Car' object has no attribute '__serial_number'
print(car.__dict__)
print(car._Car__serial_number) # 777


car._Car__serial_number = 555
print(car)
# car.__serial_number = 222
print(car.__dict__)

