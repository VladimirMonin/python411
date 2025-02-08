from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional, Set
import json
from random import choice


@dataclass
class City:
    """Датакласс для хранения информации о городе"""
    name: str
    population: int
    subject: str
    district: str
    latitude: float
    longitude: float
    is_used: bool = field(default=False, init=False, repr=False)


class JsonFile:
    """Класс для работы с JSON файлом"""
    
    def __init__(self, filename: str):
        """
        Инициализация класса
        Args:
            filename: путь к JSON файлу
        """
        self.filename = filename
    
    def read_data(self) -> List[Dict[str, Any]]:
        """
        Чтение данных из JSON файла
        Returns:
            List[Dict]: список словарей с данными о городах
        """
        with open(self.filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def write_data(self, data: List[Dict[str, Any]]) -> None:
        """
        Запись данных в JSON файл
        Args:
            data: данные для записи
        """
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)


class CitiesSerializer:
    """Класс для сериализации данных о городах"""
    
    def __init__(self, city_data: List[Dict[str, Any]]):
        """
        Инициализация класса
        Args:
            city_data: список словарей с данными о городах
        """
        self.cities: List[City] = []
        self._serialize_cities(city_data)
    
    def _serialize_cities(self, city_data: List[Dict[str, Any]]) -> None:
        """
        Сериализация данных о городах
        Args:
            city_data: список словарей с данными о городах
        """
        for city in city_data:
            self.cities.append(
                City(
                    name=city['name'],
                    population=city['population'],
                    subject=city['subject'],
                    district=city['district'],
                    latitude=float(city['coords']['lat']),
                    longitude=float(city['coords']['lon']),
                )
            )
    
    def get_all_cities(self) -> List[City]:
        """
        Получение списка всех городов
        Returns:
            List[City]: список объектов City
        """
        return self.cities


class CityGame:
    """Класс игровой логики"""
    
    def __init__(self, cities_serializer: CitiesSerializer):
        """
        Инициализация класса
        Args:
            cities_serializer: экземпляр класса CitiesSerializer
        """
        self.cities = cities_serializer.get_all_cities()
        self.cities_set: Set[str] = {city.name for city in self.cities}
        #TODO Зачем тут эта история с сетами, если блин у нас ДАТАКЛАСС! Выходит 2 класса просто выкинули (Сериализатор и City)
        self.used_cities: Set[str] = set()
        self.computer_city: str = ''
        self.bad_letters: Set[str] = self._calculate_bad_letters()
    
    def _calculate_bad_letters(self) -> Set[str]:
        """
        Расчет "плохих" букв
        Returns:
            Set[str]: множество "плохих" букв
        """
        all_letters = {city.name[-1].lower() for city in self.cities}
        first_letters = {city.name[0].lower() for city in self.cities}
        return all_letters - first_letters
    
    def start_game(self) -> str:
        """
        Начало игры
        Returns:
            str: первый город компьютера
        """
        #TODO Нафиг нам рандом если мы используем сет
        self.computer_city = choice(list(self.cities_set))
        self.cities_set.remove(self.computer_city)
        self.used_cities.add(self.computer_city)
        return self.computer_city
    
    def human_turn(self, city: str) -> bool:
        """
        Ход человека
        Args:
            city: название города
        Returns:
            bool: True если ход валидный, False если нет
        """
        if city not in self.cities_set:
            return False
        
        if self.computer_city and city[0].lower() != self.computer_city[-1].lower():
            return False
        
        self.cities_set.remove(city)
        self.used_cities.add(city)
        return True
    
    def computer_turn(self, human_city: str) -> Optional[str]:
        """
        Ход компьютера
        Args:
            human_city: город, названный человеком
        Returns:
            Optional[str]: город компьютера или None если ход невозможен
        """
        last_letter = human_city[-1].lower()
        
        for city in self.cities_set:
            if city[0].lower() == last_letter and city[-1].lower() not in self.bad_letters:
                self.computer_city = city
                self.cities_set.remove(city)
                self.used_cities.add(city)
                return city
        return None


class GameManager:
    """Фасад игры"""
    
    def __init__(self, json_file: JsonFile, cities_serializer: CitiesSerializer, city_game: CityGame):
        """
        Инициализация класса
        Args:
            json_file: экземпляр класса JsonFile
            cities_serializer: экземпляр класса CitiesSerializer
            city_game: экземпляр класса CityGame
        """
        self.json_file = json_file
        self.cities_serializer = cities_serializer
        self.city_game = city_game
    
    def __call__(self) -> None:
        """Запуск игры"""
        self.run_game()
    
    def run_game(self) -> None:
        """Основной игровой цикл"""
        print("Игра 'Города' начинается!")
        print(f"Компьютер называет город: {self.city_game.start_game()}")
        
        while True:
            human_city = input("Введите название города: ")
            
            if not self.city_game.human_turn(human_city):
                print("Неверный ход! Вы проиграли.")
                break
            
            computer_city = self.city_game.computer_turn(human_city)
            if not computer_city:
                print("Компьютер не может найти подходящий город. Вы победили!")
                break
                
            print(f"Компьютер называет город: {computer_city}")


if __name__ == "__main__":
    json_file = JsonFile("cities.json")
    cities_serializer = CitiesSerializer(json_file.read_data())
    city_game = CityGame(cities_serializer)
    game_manager = GameManager(json_file, cities_serializer, city_game)
    game_manager()
