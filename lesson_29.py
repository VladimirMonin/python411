"""
Тема: ООП Ч10. Знакомство с паттернами. Урок: 29
- Одиночка (Singleton)
    - Абстрактный прммер
    - Пример простого логера
    - Пример логгера с цветным выводом и записью в файл

- Строитель (Builder)
    - Пример пицца строителя. 
"""

"""
Опишем пример паттерна Строитель.
На примере пиццестроения.
С возможностью выбора из 2х видов пиццы (Сырный Цыплёнок, Пепперони c грибами)
А так же выбора размера (Маленькая, Средняя, Большая)
И опционально сырный борт и доп. ингридиенты.


Структура классов
- PizzaDirector - представляет директора. Можно поросить тип пиццы, а так же размер и доп. опции (сырный борт, доп. ингридиенты)

- AbstractPizzaBuilder - абстрактный класс строителя. Определяет интерфейс для создания различных типов пиццы.

- CheeseChickenPizzaBuilder - класс строителя для пиццы Сырный Цыплёнок
- PepperoniPizzaBuilder - класс строителя для пиццы Пепперони c грибами

- PizzaCheeseChiken - класс продукта
- PizzaPepperoni - класс продукта
"""

from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import List, Optional

# Размеры пиццы
class PizzaSize(Enum):
    SMALL = "Маленькая"
    MEDIUM = "Средняя"
    LARGE = "Большая"

# Дополнительные ингредиенты
class ExtraIngredient(Enum):
    CHEESE = "Дополнительный сыр"
    PEPPERONI = "Дополнительная пепперони"
    MUSHROOMS = "Дополнительные грибы"
    BACON = "Бекон"
    OLIVES = "Оливки"
    PINEAPPLE = "Ананас"

# Исключения
class PizzaException(Exception):
    pass

class CheeseBorderNotAvailableException(PizzaException):
    def __init__(self):
        super().__init__("Сырный борт доступен только для средней и большой пиццы")

# Продукты
class Pizza:
    def __init__(self, name: str):
        self.name = name
        self.size = None
        self.has_cheese_border = False
        self.extra_ingredients = []
        self.base_ingredients = []
    
    def __str__(self):
        result = f"Пицца: {self.name}\n"
        result += f"Размер: {self.size.value if self.size else 'Не указан'}\n"
        result += f"Сырный борт: {'Да' if self.has_cheese_border else 'Нет'}\n"
        result += "Базовые ингредиенты: " + ", ".join(self.base_ingredients) + "\n"
        if self.extra_ingredients:
            result += "Дополнительные ингредиенты: " + ", ".join([ing.value for ing in self.extra_ingredients]) + "\n"
        return result

class PizzaCheeseChicken(Pizza):
    def __init__(self):
        super().__init__("Сырный Цыплёнок")
        self.base_ingredients = ["Сыр", "Курица", "Сырный соус", "Специи"]

class PizzaPepperoni(Pizza):
    def __init__(self):
        super().__init__("Пепперони с грибами")
        self.base_ingredients = ["Пепперони", "Грибы", "Сыр", "Томатный соус"]

# Абстрактный строитель
class AbstractPizzaBuilder(ABC):
    @abstractmethod
    def reset(self):
        pass
    
    @abstractmethod
    def set_size(self, size: PizzaSize):
        pass
    
    @abstractmethod
    def add_cheese_border(self):
        pass
    
    @abstractmethod
    def add_extra_ingredient(self, ingredient: ExtraIngredient):
        pass
    
    @abstractmethod
    def get_pizza(self):
        pass

# Конкретные строители
class CheeseChickenPizzaBuilder(AbstractPizzaBuilder):
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.pizza = PizzaCheeseChicken()
    
    def set_size(self, size: PizzaSize):
        self.pizza.size = size
        return self
    
    def add_cheese_border(self):
        if not self.pizza.size or self.pizza.size == PizzaSize.SMALL:
            raise CheeseBorderNotAvailableException()
        self.pizza.has_cheese_border = True
        return self
    
    def add_extra_ingredient(self, ingredient: ExtraIngredient):
        self.pizza.extra_ingredients.append(ingredient)
        return self
    
    def get_pizza(self):
        pizza = self.pizza
        self.reset()
        return pizza

class PepperoniPizzaBuilder(AbstractPizzaBuilder):
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.pizza = PizzaPepperoni()
    
    def set_size(self, size: PizzaSize):
        self.pizza.size = size
        return self
    
    def add_cheese_border(self):
        if not self.pizza.size or self.pizza.size == PizzaSize.SMALL:
            raise CheeseBorderNotAvailableException()
        self.pizza.has_cheese_border = True
        return self
    
    def add_extra_ingredient(self, ingredient: ExtraIngredient):
        self.pizza.extra_ingredients.append(ingredient)
        return self
    
    def get_pizza(self):
        pizza = self.pizza
        self.reset()
        return pizza

# Директор
class PizzaDirector:
    def __init__(self):
        self.builder = None
    
    def set_builder(self, builder: AbstractPizzaBuilder):
        self.builder = builder
    
    def make_cheese_chicken_pizza(self, size: PizzaSize, with_cheese_border: bool = False, 
                                extra_ingredients: List[ExtraIngredient] = None):
        if not self.builder or not isinstance(self.builder, CheeseChickenPizzaBuilder):
            self.builder = CheeseChickenPizzaBuilder()
        
        self.builder.reset()
        self.builder.set_size(size)
        
        if with_cheese_border:
            try:
                self.builder.add_cheese_border()
            except CheeseBorderNotAvailableException as e:
                print(f"Ошибка: {e}")
        
        if extra_ingredients:
            for ingredient in extra_ingredients:
                self.builder.add_extra_ingredient(ingredient)
        
        return self.builder.get_pizza()
    
    def make_pepperoni_pizza(self, size: PizzaSize, with_cheese_border: bool = False, 
                            extra_ingredients: List[ExtraIngredient] = None):
        if not self.builder or not isinstance(self.builder, PepperoniPizzaBuilder):
            self.builder = PepperoniPizzaBuilder()
        
        self.builder.reset()
        self.builder.set_size(size)
        
        if with_cheese_border:
            try:
                self.builder.add_cheese_border()
            except CheeseBorderNotAvailableException as e:
                print(f"Ошибка: {e}")
        
        if extra_ingredients:
            for ingredient in extra_ingredients:
                self.builder.add_extra_ingredient(ingredient)
        
        return self.builder.get_pizza()

# Пользовательский интерфейс
def main():
    director = PizzaDirector()
    
    print("Добро пожаловать в пиццерию!")
    
    while True:
        print("\nВыберите тип пиццы:")
        print("1. Сырный Цыплёнок")
        print("2. Пепперони с грибами")
        print("0. Выход")
        
        try:
            choice = int(input("Ваш выбор: "))
            
            if choice == 0:
                print("Спасибо за заказ! До свидания!")
                break
            elif choice not in [1, 2]:
                print("Неверный выбор. Пожалуйста, выберите 1, 2 или 0.")
                continue
            
            # Выбор размера
            print("\nВыберите размер пиццы:")
            print("1. Маленькая")
            print("2. Средняя")
            print("3. Большая")
            
            size_choice = int(input("Ваш выбор: "))
            if size_choice not in [1, 2, 3]:
                print("Неверный выбор размера. Заказ отменен.")
                continue
            
            size = {1: PizzaSize.SMALL, 2: PizzaSize.MEDIUM, 3: PizzaSize.LARGE}[size_choice]
            
            # Сырный борт
            cheese_border = False
            if size_choice in [2, 3]:  # Средняя или большая
                cheese_border_choice = input("\nДобавить сырный борт? (да/нет): ").lower()
                cheese_border = cheese_border_choice in ["да", "yes", "y", "д"]
            
            # Дополнительные ингредиенты
            extra_ingredients = []
            print("\nДоступные дополнительные ингредиенты:")
            for i, ingredient in enumerate(ExtraIngredient, 1):
                print(f"{i}. {ingredient.value}")
            print("0. Закончить выбор")
            
            while True:
                ingredient_choice = int(input("Выберите ингредиент (0 для завершения): "))
                if ingredient_choice == 0:
                    break
                if 1 <= ingredient_choice <= len(ExtraIngredient):
                    extra_ingredients.append(list(ExtraIngredient)[ingredient_choice-1])
                    print(f"Добавлен ингредиент: {list(ExtraIngredient)[ingredient_choice-1].value}")
                else:
                    print("Неверный выбор ингредиента.")
            
            # Создание пиццы
            pizza = None
            if choice == 1:  # Сырный Цыплёнок
                pizza = director.make_cheese_chicken_pizza(size, cheese_border, extra_ingredients)
            else:  # Пепперони с грибами
                pizza = director.make_pepperoni_pizza(size, cheese_border, extra_ingredients)
            
            print("\nВаш заказ ГОТОВ:")
            print(pizza)
            
        except ValueError:
            print("Ошибка ввода. Пожалуйста, введите число.")
        except PizzaException as e:
            print(f"Ошибка при создании пиццы: {e}")
        except Exception as e:
            print(f"Неожиданная ошибка: {e}")

if __name__ == "__main__":
    main()
