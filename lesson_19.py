"""
Lesson 19
18.01.2025

Тема: ООП Ч4. Наследование. Abstractmethod. Super. Переопределение и расширение. Урок: 19
- Базовый пример на следования
- __str__ - метод, который возвращает строку с описанием объекта
"""

class Animal:
    def __init__(self, name: str):
        self.name = name
        print("Инициализация животного")
    
    def voice(self):
        print("Животное издает звук")

    def __str__(self):
        return f"Животное по имени {self.name}"


class Dog(Animal):
    pass


dog = Dog("Шарик")
print(dog)
print(type(dog))

dog.voice()

# Инициализация животного
# Животное по имени Шарик
# <class '__main__.Dog'>
# Животное издает звук