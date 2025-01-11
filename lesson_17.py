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
    def __init__(self, name:str, age: int, salary:int) -> None:
        self.name = name
        self._age = age
        self.__salary = salary

    def get_salary(self) -> int:
        return self.__salary
    
    def set_salary(self, value: int) -> None:
        self.__salary = value

