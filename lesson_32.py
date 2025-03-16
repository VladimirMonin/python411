"""
Lesson 32 - Поведенческие паттерны
16.03.2025
Пример паттерна Стратегия на примере технического анализа котировок крипты
"""

from abc import ABC, abstractmethod


class TechAnalysContext:
    def __init__(self, strategy: "AbstractStrategy") -> None:
        self.strategy = strategy

    def set_strategy(self, strategy: "AbstractStrategy") -> None:
        self.strategy = strategy

    def execute_strategy(self, message: str) -> str:
        return self.strategy.execute(message)


class AbstractStrategy(ABC):

    @abstractmethod
    def execute(self, message: str) -> str:
        pass


class StrategyAnalysOne(AbstractStrategy):
    def execute(self, message: str) -> str:
        return f"Анализ 1: {message}"


class StrategyAnalysTwo(AbstractStrategy):
    def execute(self, message: str) -> str:
        return f"Анализ 2: {message}"


# Тестируем. 1. Делаем ветвление. 2. Спрашиваем у пользователя что он хочет. 3. Создаем контекст с подходящей стратегией. 4. Запускаем

user_choice = input('Введите статегию анализа (1|2): ')

try:
    int_choice = int(user_choice)

except ValueError:
    print('Введите 1 или 2')
    exit(1)

if int_choice == 1:
    strategy = StrategyAnalysOne()
elif int_choice == 2:
    strategy = StrategyAnalysTwo()

context = TechAnalysContext(strategy)
message = input('Введите сообщение для анализа: ')
result =context.execute_strategy(message)
print(result)