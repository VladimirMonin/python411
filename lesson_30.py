"""
Тема: ООП Ч11. Порождающие паттерны. Практика. Урок: 30
- Строитель (Builder)
"""

from dataclasses import dataclass
from typing import List, Optional, Self

@dataclass
class Pizza:
    avalible_products = ["сыр", "грибы", "колбаса", "оливки", "перец", "томаты", "анчоусы", "лосось"]
    avalible_sizes = ["Маленькая", "Средняя", "Большая", ""]
    
    size: str
    cheese_bord: bool
    additional_ingredients: List[str]

    def __post_init__(self) -> None:
        if any(ingredient.lower() not in self.avalible_products for ingredient in self.additional_ingredients):
            raise ValueError("Один или несколько ингредиентов не доступны")
        
        if self.size.capitalize() not in self.avalible_sizes:
            raise ValueError("Недопустимый размер пиццы")
        

    def __str__(self) -> str:
        return f"Пицца. Размер: {self.size}, Сырный борт: {self.cheese_bord}, Дополнительные ингредиенты: {self.additional_ingredients}"


# Сразу сделаем обычного строителя.
class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza(size="", cheese_bord=False, additional_ingredients=[])

    def set_size(self, size) -> Self:
        self.pizza.size = size
        return self
    
    def add_cheese_bord(self) -> Self:
        self.pizza.cheese_bord = True
        return self
    
    def add_ingredient(self, *ingredient):
        self.pizza.additional_ingredients.extend(list(ingredient))
        return self
    
    def build(self) -> Pizza:
        return self.pizza
    

# Директор в виде менеджера
class PizzaManager:
    def __init__(self) -> None:
        self.builder = PizzaBuilder()
        self.pizza: Optional[Pizza] = None

    def make_pizza(self, size: str, cheese_bord: bool, *ingredients) -> Pizza:
        # Собираем базовую пиццу. Потом проверим на сырный борт
        self.pizza = self.builder.set_size(size).add_ingredient(*ingredients).build()
        
        # Если сырный борт, то добавляем
        if cheese_bord:
            self.pizza = self.builder.add_cheese_bord().build()
        return self.pizza
    

if __name__ == "__main__":
    manager = PizzaManager()
    # Сделаем большую пиццу с сырным бортом и добавим колбасу и оливки
    pizza = manager.make_pizza("Большая", True, "колбаса", "оливки", "томаты")
    print(pizza)
