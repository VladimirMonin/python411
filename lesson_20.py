"""
19.01.2025
Тема: ООП Ч5. Наследование. Множественное. Иерархическое. MRO. Урок: 20
- Взаимозависимость классов
- Вызов метода наследника через родителя
- Пример иерархического наследования с вызовом инициализаторов предков и передачей атрибутов
- Пример иерархического наследования с вызовом инициализаторов предков и передачей атрибутов через словарь и **kwargs
"""

# Цепочка наследования A - B - C
# Альтернативный вариант
# Много минусов. Потому что сложно отследить типы данных, сами данные и т.п.

class A:
    def __init__(self, **kwargs):
        print("Инициализация класса A")
        self.attr_a = kwargs.get('attr_a')
    
    def method_a(self):
        print("Метод A")

class B(A):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("Инициализация класса B")
        self.attr_b = kwargs.get('attr_b')
    
    def method_b(self):
        print("Метод B")

class C(B):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("Инициализация класса C")
        self.attr_c = kwargs.get('attr_c')
    
    def method_c(self):
        print("Метод C")

# Создание экземпляра с передачей всех атрибутов через kwargs
c = C(attr_a="A", attr_b="B", attr_c="C")

c.method_a()
c.method_b()
c.method_c()