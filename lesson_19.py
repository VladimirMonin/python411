"""
Lesson 19
18.01.2025

Тема: ООП Ч4. Наследование. Abstractmethod. Super. Переопределение и расширение. Урок: 19
- Базовый пример на следования
"""

class Animal:
    pass


class Dog(Animal):
    pass


dog = Dog()
print(dog)
print(type(dog))

# <__main__.Dog object at 0x00000165C1236F90>
# <class '__main__.Dog'>