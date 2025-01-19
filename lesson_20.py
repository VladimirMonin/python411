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

class SwimMixin:
    def __init__(self, swim_speed=10, *args, **kwargs):
        self.swim_speed = swim_speed
        super().__init__(*args, **kwargs)
    
    def swim(self):
        return f"{self.__class__.__name__} плавает со скоростью {self.swim_speed} км/ч"

class FlyMixin:
    def __init__(self, max_altitude=100, *args, **kwargs):
        self.max_altitude = max_altitude
        super().__init__(*args, **kwargs)
    
    def fly(self):
        return f"{self.__class__.__name__} летит на высоте {self.max_altitude} метров"

class RunMixin:
    def __init__(self, run_speed=20, *args, **kwargs):
        self.run_speed = run_speed
        super().__init__(*args, **kwargs)
    
    def run(self):
        return f"{self.__class__.__name__} бежит со скоростью {self.run_speed} км/ч"

class Animal:
    def __init__(self, name, age, *args, **kwargs):
        self.name = name
        self.age = age
        super().__init__(*args, **kwargs)

    def eat(self):
        return f"{self.name} кушает"

class Duck(Animal, SwimMixin, FlyMixin):
    def __init__(self, name, age, swim_speed=8, max_altitude=50):
        super().__init__(name=name, age=age, swim_speed=swim_speed, max_altitude=max_altitude)

    def make_sound(self):
        return "Кря-кря!"

class Penguin(Animal, SwimMixin, RunMixin):
    def __init__(self, name, age, swim_speed=15, run_speed=10):
        super().__init__(name=name, age=age, swim_speed=swim_speed, run_speed=run_speed)

    def make_sound(self):
        return "Ква-ква!"


# Создаём животных с атрибутами
print(Duck.mro()) # [<class '__main__.Duck'>, <class '__main__.Animal'>, <class '__main__.SwimMixin'>, <class '__main__.FlyMixin'>, <class 'object'>]
donald = Duck(name="Дональд", age=5, swim_speed=12, max_altitude=60)
rico = Penguin(name="Рико", age=3, swim_speed=20, run_speed=15)

# Проверяем атрибуты и методы
print(donald.swim())  # Дональд плавает со скоростью 12 км/ч
print(donald.name, donald.age)  # Дональд 5
print(donald.max_altitude)  # 60

print(rico.swim())  # Рико плавает со скоростью 20 км/ч
print(rico.run())   # Рико бежит со скоростью 15 км/ч
