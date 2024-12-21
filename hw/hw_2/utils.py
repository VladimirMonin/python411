"""

1. **Функция `get_weather`**
- Аргументы:
- `city: str`: Название города для получения прогноза погоды.
- `api_key: str`: Ключ API для доступа к сервису.
- Возвращает:
- `dict`: Словарь с данными о погоде.
- Описание: Выполняет запрос к API и возвращает данные о погоде в виде словаря.

2. **Функция `format_weather_message`**
- Аргументы:
- `weather_dict: dict`: Словарь с данными о погоде.
- Возвращает:
- `str`: Форматированное сообщение о погоде.
- Описание: Форматирует данные о погоде в удобочитаемое сообщение.

3. **Функция `notify_weather`**
- Аргументы:
- `message: str`: Сообщение о погоде для уведомления.
- Возвращает:
- `None`
- Описание: Отправляет уведомление пользователю с информацией о погоде.

4. **Функция `main`**
- Описание: Запускает программу, выполняет вызовы вышеуказанных функций и обрабатывает вывод.

"""

import requests
from plyer import notification


CITY = "Усть-Каменогорск"
API_KEY = "23496c2a58b99648af590ee8a29c5348"
UNITS = "metric"
LANGUAGE = "ru"


def get_weather(
    city: str = CITY,
    api_key: str = API_KEY,
    units: str = UNITS,
    language: str = LANGUAGE,
) -> dict:
    """
    Функция получения информации о погоде

    Keyword Arguments:
        city -- (default: {CITY}) - Название города для получения прогноза погоды.
        api_key -- (default: {API_KEY})  - Ключ API для доступа к сервису.
        units --  (default: {UNITS}) - Единица измерения температуры (metric, imperial, standard).
        language -- (default: {LANGUAGE}) - Язык интерфейса (ru, en, etc.).

    Returns:
        Возвращает словарь с информацией о погоде
    """

    url = rf"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={units}&lang={language}"
    response = requests.get(url)
    return response.json()




def format_weather_message(weather_dict: dict) -> str:
    """
    Функция форматирования сообщения о погоде. Возвращает строку с информацией о погоде.

    Arguments:
        weather_dict -- словарь с данными о погоде (ответ погодного API)

    Returns:
       Строка с информацией о погоде формата 'Температура: {temp}°C\nОщущается как: {feels_like}°C\nОписание: {description}'
    """

    temp = weather_dict["main"]["temp"]
    feels_like = weather_dict["main"]["feels_like"]
    description = weather_dict["weather"][0]["description"]

    return (
        f"Температура: {temp}°C\nОщущается как: {feels_like}°C\nОписание: {description}"
    )
