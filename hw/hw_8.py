from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
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

    def get_first_letter(self) -> str:
        """Получение первой буквы города в нижнем регистре"""
        return self.name[0].lower()

    def get_last_letter(self) -> str:
        """Получение последней буквы города в нижнем регистре"""
        return self.name[-1].lower()


class JsonFile:
    """Класс для работы с JSON файлом"""
    
    def __init__(self, filename: str):
        self.filename = filename
    
    def read_data(self) -> List[Dict[str, Any]]:
        """Чтение данных из JSON файла"""
        with open(self.filename, 'r', encoding='utf-8') as f:
            return json.load(f)


class CitiesSerializer:
    """Класс для сериализации данных о городах"""
    
    def __init__(self, city_data: List[Dict[str, Any]]):
        self.cities: List[City] = []
        self._serialize_cities(city_data)
    
    def _serialize_cities(self, city_data: List[Dict[str, Any]]) -> None:
        """Сериализация данных о городах"""
        for city in city_data:
            self.cities.append(
                City(
                    name=city['name'],
                    population=city['population'],
                    subject=city['subject'],
                    district=city['district'],
                    latitude=float(city['coords']['lat']),
                    longitude=float(city['coords']['lon'])
                )
            )
    
    def get_all_cities(self) -> List[City]:
        """Получение списка всех городов"""
        return self.cities


class CityGame:
    """Класс игровой логики"""
    
    def __init__(self, cities_serializer: CitiesSerializer):
        self.cities: List[City] = cities_serializer.get_all_cities()
        self.current_computer_city: Optional[City] = None
        self.bad_letters = self._calculate_bad_letters()

    def _calculate_bad_letters(self) -> set[str]:
        """Расчет букв, на которые нет городов"""
        all_last_letters = {city.get_last_letter() for city in self.cities}
        all_first_letters = {city.get_first_letter() for city in self.cities}
        return all_last_letters - all_first_letters

    def get_available_cities(self) -> List[City]:
        """Получение списка доступных городов"""
        return [city for city in self.cities if not city.is_used]

    def find_city_by_name(self, name: str) -> Optional[City]:
        """Поиск города по имени"""
        for city in self.cities:
            if city.name.lower() == name.lower() and not city.is_used:
                return city
        return None

    def start_game(self) -> City:
        """Начало игры - первый ход компьютера"""
        available_cities = self.get_available_cities()
        self.current_computer_city = choice(available_cities)
        self.current_computer_city.is_used = True
        return self.current_computer_city

    def validate_human_turn(self, city: City) -> bool:
        """Проверка хода человека"""
        if self.current_computer_city:
            return city.get_first_letter() == self.current_computer_city.get_last_letter()
        return True

    def make_computer_turn(self, human_city: City) -> Optional[City]:
        """Ход компьютера"""
        available_cities = self.get_available_cities()
        for city in available_cities:
            if (city.get_first_letter() == human_city.get_last_letter() and 
                city.get_last_letter() not in self.bad_letters):
                city.is_used = True
                self.current_computer_city = city
                return city
        return None


class GameManager:
    """Фасад игры"""
    
    def __init__(self, city_game: CityGame):
        self.city_game = city_game
    
    def __call__(self) -> None:
        self.run_game()
    
    def run_game(self) -> None:
        """Основной игровой цикл"""
        print("Игра 'Города' начинается!")
        computer_city = self.city_game.start_game()
        print(f"Компьютер называет город: {computer_city.name} "
              f"({computer_city.subject}, население: {computer_city.population})")
        
        while True:
            human_input = input("Введите название города: ")
            human_city = self.city_game.find_city_by_name(human_input)
            
            if not human_city:
                print("Такого города нет или он уже использован!")
                break
                
            if not self.city_game.validate_human_turn(human_city):
                print("Город должен начинаться на последнюю букву предыдущего города!")
                break
            
            human_city.is_used = True
            computer_city = self.city_game.make_computer_turn(human_city)
            
            if not computer_city:
                print(f"Поздравляем! Вы победили! Компьютер не смог найти город на букву '{human_city.get_last_letter()}'")
                break
                
            print(f"Компьютер называет город: {computer_city.name} "
                  f"({computer_city.subject}, население: {computer_city.population})")


if __name__ == "__main__":
    json_file = JsonFile("cities.json")
    cities_serializer = CitiesSerializer(json_file.read_data())
    city_game = CityGame(cities_serializer)
    game_manager = GameManager(city_game)
    game_manager()
