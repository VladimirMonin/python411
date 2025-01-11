"""
Lesson 17
11.01.2025
Инкапсуляция. Приватные методы и атрибуты.
- Приватные атрибуты
- Приватные методы
- Защищенные атрибуты
- Защищенные методы
- Доступ из вне

Делаем 2 метода, которые называются одинаково
Например это salary

@property
def salary  - это для добычи данных из приватных атрибутов

@salary.setter - мы делаем сеттер для конкретного атрибута
"""

class SalaryException(ValueError):
    """
    Ошибка связанна с измененим в ЗП
    """
    pass

class Employee:
    def __init__(self, name:str, age: int, salary:int, threshold_percent_salary: int = 50) -> None:
        self.name = name
        self._age = age
        self.__salary = salary
        self.__threshold_percent_salary: int = 50

    @property
    def salary(self) -> int:
        return self.__salary
    
    @salary.setter
    def salary(self, value: int) -> None:
        if not isinstance(value, int):
            raise SalaryException("Зарплата должна быть числом")
        if value < 0:
            raise SalaryException("Зарплата не может быть меньше 0")
        # Проверим чтобы зарплата не колебалась более чем на __threshold_percent_salary
        if abs(self.__salary - value) > self.__salary * self.__threshold_percent_salary / 100:
            raise SalaryException(f"Зарплата не может колебаться более чем на {self.__threshold_percent_salary}%")
        
        self.__salary = value
        

manager = Employee("Владимир", 30, 100000)
print(manager.salary)

while True:
    new_salary = int(input("Введите новую зарплату: "))
    try:
        manager.salary = new_salary
    except SalaryException as e:
        print(e)
    else:
        print(f"Зарплата успешно изменена на {manager.salary}")
