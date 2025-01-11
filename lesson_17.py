"""
Lesson 17
11.01.2025
Инкапсуляция. Приватные методы и атрибуты.
- Приватные атрибуты
- Приватные методы
- Защищенные атрибуты
- Защищенные методы
- Доступ из вне
"""

class Employee:
    def __init__(self, name:str, age: int, salary:int, threshold_percent_salary: int = 50) -> None:
        self.name = name
        self._age = age
        self.__salary = salary
        self.__threshold_percent_salary: int = 50

    def get_salary(self) -> int:
        return self.__salary
    
    def set_salary(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("Зарплата должна быть числом")
        if value < 0:
            raise ValueError("Зарплата не может быть меньше 0")
        # Проверим чтобы зарплата не колебалась более чем на __threshold_percent_salary
        if abs(self.__salary - value) > self.__salary * self.__threshold_percent_salary / 100:
            raise ValueError(f"Зарплата не может колебаться более чем на {self.__threshold_percent_salary}%")
        
        self.__salary = value
        

manager = Employee("Владимир", 30, 100000)
print(manager.get_salary())
manager.set_salary("пирожок")
print(manager.get_salary())