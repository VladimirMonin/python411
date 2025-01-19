"""
19.01.2025
Тема: ООП Ч5. Наследование. Множественное. Иерархическое. MRO. Урок: 20
- Взаимозависимость классов
- Вызов метода наследника через родителя
"""

# Цепочка наследования A - B - C

class A:
    def __init__(self, attr_a:str):
        print("Инициализация класса A")
        self.attr_a = attr_a
    
    def method_a(self):
        print("Метод A")

class B(A):
    def __init__(self, attr_a:str, attr_b:str):
        super().__init__(attr_a)
        print("Инициализация класса B")
        self.attr_b = attr_b
    
    def method_b(self):
        print("Метод B")

class C(B):
    def __init__(self,  attr_a:str, attr_b:str, attr_c: str):
        super().__init__(attr_a, attr_b)
        print("Инициализация класса C")
        self.attr_c = attr_c
    
    def method_c(self):
        print("Метод C")


c = C("A", "B", "C")
c.method_a()
c.method_b()
c.method_c()
