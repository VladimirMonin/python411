"""
Lesson 32 - Поведенческие паттерны
16.03.2025
Пример паттерна Стратегия на примере технического анализа котировок крипты
Пример паттерна Наблюдатель на примере крипторынка и разных автоматизаций (Уведомления, торговые боты)
"""

from abc import ABC, abstractmethod

class AbstractMarketObserver(ABC):
    @abstractmethod
    def update(self, data: dict) -> None:
        pass


class NotifyMarketObserver(AbstractMarketObserver):
    def update(self, data: dict) -> None:
        BTC = data.get("BTC", 0)
        ETH = data.get("ETH", 0)

        if BTC > 100000:
            print("BTC подорожал больше чем на 100000")

        if ETH > 5000:
            print("ETH подорожал больше чем на 5000")


class TradeMarketObserver(AbstractMarketObserver):
    def update(self, data: dict) -> None:
        TON = data.get("TON", 0)
        LTC = data.get("LTC", 0)

        if TON > 5:
            print("Дурова выпустили из тюрьмы, TON вырос выше 5 ПРОДАЕМ!")

        if LTC > 100:
            print("LTC вырос выше 100 ПОКУПАТЬ")


class Market:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.observers = []
        self.data = {}

    
    def add_observer(self, observer: AbstractMarketObserver) -> None:
        self.observers.append(observer)

    def remove_observer(self, observer: AbstractMarketObserver) -> None:
        self.observers.remove(observer)

    def _notify_observers(self, new_data: dict) -> None:
        for observer in self.observers:
            observer.update(new_data)

    def set_data(self, new_data: dict) -> None:
        # Обновление словаря
        self.data.update(new_data)
        # Оповещение наблюдателей
        self._notify_observers(new_data)


if __name__ == "__main__":
    # Создаем рынок
    market = Market(api_key="123")
    
    # Создаем наблюдателей
    notify_observer = NotifyMarketObserver()
    trade_observer = TradeMarketObserver()

    # Регистрируем наблюдателей
    market.add_observer(notify_observer)
    market.add_observer(trade_observer)

    # Обновляем данные на рынке
    market.set_data({"NOT": 100})
    market.set_data({"TON": 10, "LTC": 200})
    market.set_data({"BTC": 10000000, "ETH": 50000})