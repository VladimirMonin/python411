"""
Lesson 16
29.12.2024

Python: ООП. Ч1. Нейминг. Атрибуты. Методы. Урок: 16
- Нейминг.
- Атрибуты класса
- Инициализатор
- Self
- __str__
- Методы экземпляра
- Статик методы
"""

"""
UpperCamelCase - первое слово с большой буквы, остальные с маленькой. Каждое новое слово с большой буквы.

Название должно быть информативным. Передавать смысл. Как правило это существительные и или прилагательные.
"""
# __name__ - имя модуля. Если мы запускаем файл напрямую, то __name__ == __main__. Если мы импортируем модуль, то __name__ == имя модуля.

# __init__ - Инициализатор класса. Вызывается автоматически при создании объекта. Наделяет экземпляр класса атрибутами и методами.

class Car:
    def __init__(self, model:str, color:str, year:int) -> None:
        self.model = model
        self.color = color
        self.year = year
    
    def __str__(self) -> str:
        return f"Модель: {self.model}\nЦвет: {self.color}\nГод выпуска: {self.year}"
    
    def make_beep(self, count:int) -> str:
        return f"Автомобиль {self.model} сделал {'Бип ' * count}"
    
    @staticmethod # Метод который не работает ни с атрибутами экземляра ни с атрибутами класса
    def get_auto_value(width: int, height: int, depth: int) -> int:
        return width * height * depth


car_1 = Car("BMW", "red", 2020)
car_2 = Car("Жигули", "blue", 1990)

auto_list = [car_1, car_2]

for car in auto_list:
    print(car)
    print(car.make_beep(3))

print(car_1.make_beep(3))
print(car_2.make_beep(5))
