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

# Kwargs

# Простой пример распаковки словаря
user = {"name": "Иван", "age": 25}
name, age = user.values()  # ['Иван', 25] - раскидывается на две переменные
print(f"Имя: {name}, Возраст: {age}")


# Пример посложнее - распаковка вложенного словаря
student = {"info": {"name": "Мария", "age": 20}, "grades": {"math": 5, "physics": 4}}
info, grades = student.values()
print(f"Информация: {info}")
print(f"Оценки: {grades}")


# Распаковка с использованием **
defaults = {"host": "localhost", "port": 8000}
custom = {"port": 9000, "timeout": 30}
config = {**defaults, **custom}  # port из custom перезапишет port из defaults
print(f"Итоговая конфигурация: {config}")

# Как это было бы через Update
new_dict = {}
new_dict.update(defaults)
new_dict.update(custom)
print(f"Итоговая конфигурация: {new_dict}")


########################################


def print_user_info(*args, **user_info):
    """
    Функция для вывода информации о пользователе
    """
    print(type(user_info))  #  <class 'dict'>
    for key, value in user_info.items():
        print(f"Ключ: {key}, Значение: {value}")


print_user_info(name="Илья", last_name="Морозов", age=25)

user_info = {"name": "Екатерина", "age": 25, "city": "Москва"}

print_user_info(**user_info)
print_user_info(
    1,
    2,
    "Илья",
    hobbies=["футбол", "программирование"],
)

config_open_ai = {
    "model": "gpt-3.5-turbo",
    "temperature": 0.7,
    "max_tokens": 50,
    "top_p": 1.0,
    "frequency_penalty": 0.0,
    "api_key": "sk-...",
    "endpoints": "https://api.openai.com/v1/chat/completions",
}


def open_ai_request(**params):
    # Тут вы можете разобрать словарь и добыть нужное
    pass


def open_ai_request2(
    model: str,
    temperature: float,
    max_tokens: int,
    top_p: float,
    frequency_penalty: float,
    presence_penalty: float,
    api_key: str,
    endpoints: str,
):
    # ЭТОТ вариант,
    pass


# open_ai_request2(**config_open_ai)

open_ai_request2(
    model="gpt-3.5-turbo",
    temperature=0.7,
    max_tokens=50,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0,
    api_key="sk-...",
    endpoints="https://api.openai.com/v1/chat/completions",
)

user_info = {"name": "Екатерина", "age": 25, "city": "Москва"}


def print_user_info2(name, age, city):
    print(f"Имя: {name}, Возраст: {age}, Город: {city}")


# print_user_info2(**user_info)

# print(**user_info)

# Конфиг для принта
config = {
    "sep": "+",
    "end": "\n",
}

print("Hello", "World", **config)
