# Этот импорт неплох, но нам придется обращаться к элементам через название модуля
# import utils

# utils.get_weather()
# utils.CITY

# Плох. Потому что мы не знаем сколько и что импортируем.
# from utils import *
# get_weather()
# CITY

# Хорошо. Мы знаем, что импортируем. И даже что используется а что нет.
from weather_utils.utils import get_weather, format_weather_message, notify_weather

# Напишем собственную функцию main где город можно вводить через input


def main():
    city = input("Введите название города: ")
    weather_dict = get_weather(city=city)
    message = format_weather_message(weather_dict)
    print(message)
    input("Нажмите Enter для уведомления")
    notify_weather(message)

if __name__ == '__main__':
    main()