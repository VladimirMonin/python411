"""
Lesson 17
11.01.2025
Инкапсуляция. Приватные методы и атрибуты.
"""

class Car:
    """
    Экспериментальный класс автомобиль 
    для изучения приватных и защищенных методов и атрибутов
    """
    def __init__(self, color: str, mark: str, serial_number: int):
        self.color = color
        self.mark = mark
        self.__serial_number = serial_number
        self.__engine_state: bool = False

    def __str__(self):
        return f'Автомобиль {self.mark}.\nСерийный номер {self.__serial_number}'
    
    def start_engine(self):
        self.__engine_state = True
        self.__make_noise()
        print(f'Состояние двигателя: {self.__engine_state}')

    def stop_engine(self):
        self.__engine_state = False
        print(f'Состояние двигателя: {self.__engine_state}')

    def __make_noise(self):
        print(f"Звук работы двигателя {self.mark}")

    def move(self):
        if self.__engine_state:
            print("Автомобиль едет")
            self.__make_noise()
        else:
            print("Двигатель не запущен")

    def stop(self):
        print("Автомобиль остановился")

# Создаем экземпляр класса автомобиль
car = Car("red", "Ёмобиль", 123456)

# Попробуем поехать
car.move()

# Запустим двигатель
car.start_engine()

# Поехали
car.move()

# Останавливаемся
car.stop()

# Остановим двигатель
car.stop_engine()

# Пробуем издать звук работы двигателя
# car.__make_noise() # AttributeError: 'Car' object has no attribute '__make_noise'. Did you mean: '_Car__make_noise'?