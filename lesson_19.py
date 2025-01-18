"""
Lesson 19
18.01.2025

Тема: ООП Ч4. Наследование. Abstractmethod. Super. Переопределение и расширение. Урок: 19
- Базовый пример на следования
- __str__ - метод, который возвращает строку с описанием объекта
- Переопределение метода voice в наследнике
- Проверка доступа защищенных и приватных атрибутов в наследнике (защищенные доступны, приватные нет)
"""

class Animal:
    def __init__(self, name: str):
        self._name = name
        print("Инициализация животного")
    
    def voice(self):
        return "Животное издает звук"

    def __str__(self):
        return f"Животное по имени {self._name}"


class Dog(Animal):
    def __init__(self, name: str, breed: str):
        # Animal.__init__(self, name)
        super().__init__(name)
        self.breed = breed
        print("Инициализация собаки")

    def voice(self):
        # animal_voice = Animal.voice(self)
        animal_voice = super().voice()
        animal_voice += " Гав"
        return animal_voice


dog = Dog("Шарик", "Дворняга")
print(dog)
print(type(dog))

print(dog.voice())

# Инициализация животного
# Инициализация собаки
# Животное по имени Шарик
# <class '__main__.Dog'>
# Животное издает звук Гав