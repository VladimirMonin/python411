"""
25.01.2025
Тема: ООП Ч4. Разбор ДЗ. Магические методы Урок: 19
- Разбор ДЗ с Наследованием и абстрактным классом Файл.
- Повторение миксинов

- Макгические методы
- __init__ - инициализатор - вызывается при создании объекта
- __str__ - метод, который возвращает строку с описанием объекта
- __repr__ - тоже описание объекта, но дргуое. Либо техническое описание, либо строка для создания объекта
- __len__ - метод, который возвращает длину объекта len(obj)
- __call__ - метод, который вызывается при вызове объекта как функции
- __bool__ - метод, который возвращает True или False в зависимости от состояния объекта
"""

class Duck:
    default_status = "alive"

    def __init__(self, name: str, weight: float):
        self.name = name
        self.status = self.__class__.default_status
        self.weight = weight

    def __str__(self):
        return f"Утка {self.name} - {self.status}"
    
    def __repr__(self):
        return f"Duck({self.name}, {self.weight})"

    def __call__(self, cooking_type: str):
        self.status = cooking_type
        # print(f"Утка {self.name}: {cooking_type}")

    def __len__(self):
        return round(self.weight)
    
    def __bool__(self):
        return self.status != self.__class__.default_status


duck1 = Duck("Дональд", 8)
duck2 = Duck("Марго", 2)

ducks = [duck1, duck2]

[print(duck) for duck in ducks]
[print(len(duck)) for duck in ducks]

sorted_ducks = sorted(ducks, key=len)
print(sorted_ducks)

# Пожарим Доналда на вертеле на костре
duck1("Пожарена")

# Проверяем как if вызывает __bool__
if duck2:
    print("Утка готова.", duck2.status)
else:
    print("Утка не готова.", duck2.status)
