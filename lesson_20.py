"""
19.01.2025
Тема: ООП Ч5. Наследование. Множественное. Иерархическое. MRO. Урок: 20
- Взаимозависимость классов
- Вызов метода наследника через родителя
- Пример иерархического наследования с вызовом инициализаторов предков и передачей атрибутов
- Пример иерархического наследования с вызовом инициализаторов предков и передачей атрибутов через словарь и **kwargs
- Множественное наследование
- MRO - method resolution order - порядок разрешения методов
"""

# Цепочка наследования A - B - C
# Альтернативный вариант
# Много минусов. Потому что сложно отследить типы данных, сами данные и т.п.


class A:
    def __init__(self, attr_a) -> None:
        print("Инициализация класса A")
        self.attr_a = attr_a

    def method_a(self):
        print(f"Method A: {self.attr_a} ")


class B:
    def __init__(self, attr_b) -> None:
        print("Инициализация класса B")
        self.attr_b = attr_b

    def method_b(self):
        print(f"Method B: {self.attr_b}")


class C(A, B):
    def __init__(self, attr_a, attr_b, attr_c) -> None:
        A.__init__(self, attr_a)
        B.__init__(self, attr_b)
        print("Инициализация класса C")
        self.attr_c = attr_c

    def method_c(self):
        print(f"Method C: {self.attr_c}")


c = C(1, 2, 3)
