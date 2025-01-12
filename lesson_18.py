"""
Lesson 18
12.01.2025

Python: ООП. Ч3. Инкапсуляция. Приватные методы и атрибуты. Урок: 18
- Практика. Пишем класс для работы с погодным API
"""

import requests
from plyer import notification
from requests.exceptions import RequestException
from json.decoder import JSONDecodeError
# pip innstall plyer requests

CITY = "Усть-Каменогорск"
API_KEY = "23496c2a58b99648af590ee8a29c5348"
UNITS = "metric"
LANGUAGE = "ru"

# url = fr'https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units={UNITS}&lang={LANGUAGE}'

# response = requests.get(url) # Сделали запрос и получили объект ответа
# print(response.status_code) # Получили статус ответа
# print(response.json()) # Получили объект Python из JSON


# Получим описание и температуру, и ощущается как
# weather_dict = response.json()

class WeatherRequestError(Exception):
    """Кастомное исключение для ошибок погодного API"""
    pass

class WeatherRequst:
    def __init__(self, api_key: str, units: str = "metric", language: str = "ru"):
        self.api_key = api_key
        self.units = units
        self.language = language
        self.__url: str = ''
        self.__response: dict = {}

    def __get_request_url(self, city: str):
        """
        Метод
        :param:
        :return:
        """
        self.__url = fr'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units={self.units}&lang={self.language}'
        
    def get_weather(self, city: str):
        """
        Метод формирует URL и делает запрос к погодному API
        :param city: Название города
        :return: None
        :raises: WeatherRequestError
        """
        try:
            self.__get_request_url(city)
            response = requests.get(self.__url, timeout=5)  # добавляем timeout
            response.raise_for_status()  # проверяем статус ответа
            self.__response = response.json()
        except RequestException as e:
            raise WeatherRequestError(f"Ошибка при запросе погоды: {str(e)}")
        except JSONDecodeError:
            raise WeatherRequestError("Получен некорректный ответ от сервера")

    def get_clear_weather_data(self, city: str):
        """
        Метод очищает данные полученные из погодного API и упаковывает их в словарь,
        с 3мя ключами. Температура, ощущается как и описание погоды.
        :param city: Название города
        :return: Словарь с очищенными данными
        """
        self.get_weather(city)

        result_dict = {}

        result_dict["temp"] = self.__response["main"]["temp"]
        result_dict["feels_like"] = self.__response['main']['feels_like']
        result_dict["description"] = self.__response['weather'][0]['description']

        return result_dict
    
    def get_weather_string(self, weather_dict: dict) -> str:
        """
        Метод возвращает строку с описанием погоды
        :param weather_dict: Словарь с данными о погоде
        :return: Строка с описанием погоды
        """
        temp = weather_dict['temp']
        feels_like = weather_dict['feels_like']
        description = weather_dict['description']

        return f'Температура: {temp}°C\nОщущается как: {feels_like}°C\nОписание: {description}'
    
    def __call__(self, city: str)-> str:
        weather_dict = self.get_clear_weather_data(city)
        return self.get_weather_string(weather_dict)


# weather = WeatherRequst(API_KEY)
# result = weather("Бангкок")
# print(result)
        

class Notification:

    @staticmethod
    def send_notification(title: str, message: str):
        notification.notify(
            title=title,
            message=message,
            app_name="Погода",
            app_icon=None,
            timeout=10,
            toast=True,
        )

    def __call__(self, title: str, message: str):
        self.send_notification(title, message)


class WeatherFacade:
    def __init__(self, api_key: str, units: str = "metric", language: str = "ru"):
        self.weather = WeatherRequst(api_key, units, language)
        self.notification = Notification()

    def __call__(self, city: str):
        weather_dict = self.weather.get_clear_weather_data(city)
        title = f"Погода в {city}"
        message = self.weather.get_weather_string(weather_dict)
        self.notification(title, message)


if __name__ == '__main__':
    weather = WeatherFacade(API_KEY)
    input_city = input("Введите название города: ")
    weather(input_city)

