"""
19.01.2025
Тема: ООП Ч5. Наследование. Множественное. Иерархическое. MRO. Урок: 20
- Взаимозависимость классов
- Вызов метода наследника через родителя
- Пример иерархического наследования с вызовом инициализаторов предков и передачей атрибутов
- Пример иерархического наследования с вызовом инициализаторов предков и передачей атрибутов через словарь и **kwargs
- Множественное наследование
- MRO - method resolution order - порядок разрешения методов
- Mixin - 
"""

# Создаём миксины для различных способностей животных
class SwimMixin:
    def swim(self):
        return f"{self.__class__.__name__}по имени {self.name} плавает в воде"

class FlyMixin:
    def fly(self):
        return f"{self.__class__.__name__}по имени {self.name} летит по небу"

class RunMixin:
    def run(self):
        return f"{self.__class__.__name__}по имени {self.name} бежит по земле"

# Базовый класс животного
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} кушает"

# Теперь создаём конкретных животных с нужными способностями
class Duck(Animal, SwimMixin, FlyMixin):
    def make_sound(self):
        return "Кря-кря!"

class Cat(Animal, RunMixin):
    def make_sound(self):
        return "Мяу!"

class Penguin(Animal, SwimMixin, RunMixin):
    def make_sound(self):
        return "Курлык!"

class SwimingCat(Animal, SwimMixin, RunMixin):
    def make_sound(self):
        return "Мяу-мяу!"


# Создаём животных
donald = Duck(name="Дональд")
murzik = Cat(name="Мурзик")
rico = Penguin(name="Рико")

# Проверяем их способности
print(donald.swim())  # Выведет: Duck плавает в воде
print(donald.fly())   # Выведет: Duck летит по небу
print(murzik.run())   # Выведет: Cat бежит по земле
print(rico.swim())    # Выведет: Penguin плавает в воде
