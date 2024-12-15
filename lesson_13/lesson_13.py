"""
Урок 13
15.12.2024

Python функции. **kwargs. Модули. Библиотеки plyer и requests. Урок: 13

1. Разбор **kwargs - "распаковка" словаря

2. Работа с внешними библиотеками:
    - Установка через pip
    - Импорт модулей
    - Библиотека plyer для уведомлений
    - Библиотека requests для HTTP запросов

3. Создание модулей:
    - Разделение кода на модули
    - Импорт собственных модулей
    - Относительные и абсолютные импорты
    - __name__ == '__main__'

4. Практика:
    - Создание функций для работы с API
    - Отправка уведомлений через plyer
    - Получение данных через requests
    - Структурирование кода в модули
"""

# PIP
"""
pip list - список установленных пакетов
pip install <package_name> - установить пакет
pip install plyer requests pyinstaller
pip freeze > requirements.txt - сохранить список пакетов в файл
pip install -r requirements.txt - установить все пакеты из файла
pip uninstall <package_name> - удалить пакет
pip show <package_name> - информация о пакете
pip search <package_name> - поиск пакетов
pip upgrade <package_name> - обновить пакет
"""

"""
https://api.openweathermap.org/data/2.5/weather?&appid={API key}&units=metric&lang=ru

https://api.openweathermap.org/data/2.5/weather?q=Усть-Каменогорск&appid=23496c2a58b99648af590ee8a29c5348&units=metric&lang=ru
"""


"""
Это погодное приложение, которое работает на Python библиотеке requests, plyer.

pip install plyer requests pyinstaller

Образец ссылки https://api.openweathermap.org/data/2.5/weather?q=Москва&appid=23496c2a58b99648af590ee8a29c5348&units=metric&lang=ru

{'coord': {'lon': 37.6156, 'lat': 55.7522}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'облачно с прояснениями', 'icon': '04n'}], 'base': 'stations', 'main': {'temp': 0.93, 'feels_like': -3.44, 'temp_min': 0.24, 'temp_max': 0.93, 'pressure': 1022, 'humidity': 61, 'sea_level': 1022, 'grnd_level': 1002}, 'visibility': 10000, 'wind': {'speed': 4.47, 'deg': 214, 'gust': 11.97}, 'clouds': {'all': 64}, 'dt': 1733247335, 'sys': {'type': 2, 'id': 2095214, 'country': 'RU', 'sunrise': 1733204316, 'sunset': 1733230838}, 'timezone': 10800, 'id': 524901, 'name': 'Москва', 'cod': 200}

"""


import requests
from plyer import notification
# Просто сделаем запрос без функций

CITY = "Усть-Каменогорск"
API_KEY = "23496c2a58b99648af590ee8a29c5348"
UNITS = "metric"
LANGUAGE = "ru"

url = fr'https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units={UNITS}&lang={LANGUAGE}'

response = requests.get(url) # Сделали запрос и получили объект ответа
print(response.status_code) # Получили статус ответа
print(response.json()) # Получили объект Python из JSON


# Получим описание и температуру, и ощущается как
weather_dict = response.json()

# Temp
temp = weather_dict['main']['temp']
# Ощущается как
feels_like = weather_dict['main']['feels_like']
# Описание погоды
description = weather_dict['weather'][0]['description']

print(f'Температура: {temp}°C\nОщущается как: {feels_like}°C\nОписание: {description}')

# Уведомление
notification.notify(
    title=f"Погода в {CITY}",
    message=f"Температура: {temp}°C\nОщущается как: {feels_like}°C\nОписание: {description}",
    app_name="Погода",
    app_icon=None,
    timeout=60,
    toast=True,
)
