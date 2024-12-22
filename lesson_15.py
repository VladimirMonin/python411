"""
Урок 15
22.12.2024

Python: Работа с форматами данных JSON, CSV, YAML. Урок: 15

1. Формат JSON:
    - Структура и синтаксис JSON
    - Методы json.dumps() и json.loads()
    - Работа с json.dump() и json.load()
    - Обработка сложных структур данных
    
2. Работа с CSV файлами:
    - Структура CSV формата
    - Модуль csv
    - Чтение CSV через csv.reader()
    - Запись в CSV через csv.writer()
    - Работа с csv.DictReader и csv.DictWriter
    
3. Формат YAML:
    - Особенности синтаксиса YAML
    - Установка и использование PyYAML
    - Методы yaml.safe_load() и yaml.dump()
    - Конвертация между форматами
    
4. Практическое применение:
    - Сохранение конфигураций приложения
    - Работа с табличными данными
    - Парсинг внешних источников данных
    - Конвертация между форматами

Практика:
- Создание конфигурационного файла в YAML
- Обработка данных из CSV файла
- Сериализация объектов в JSON
- Конвертер данных между форматами
"""

# JSONN (JavaScript Object Notation)
# JSON - это текстовый формат данных, который используется для представления структурных данных.
# JSON поддерживает следующие типы данных:
# - строки
# - числа
# - логические значения (true, false)
# - массивы
# - объекты
# - null

# Python имеет встроенный модуль json, который позволяет работать с JSON данными.
# Модуль json предоставляет следующие функции:
# - json.dumps() - преобразует объект Python в строку JSON
# - json.loads() - преобразует строку JSON в объект Python
# - json.dump() - записывает объект Python в файл в формате JSON
# - json.load() - читает объект Python из файла в формате JSON


import json
import csv


# json_string = """[
#     "Монин Владимир Александрович",
#     "Артемьев Алексей Львович",
#     "Багаутдинов Ринат Дмитриевич",
#     "Балагуров Артем Алексеевич",
#     "Бибиков Кирилл Сергеевич",
#     "Крылов Илья Сергеевич",
#     "Кряжев Руслан Анатольевич",
#     "Кузнецов Иван Станиславович",
#     "Лапицкая Наталья Владимировна",
#     "Мазуренко Кристина Владимировна",
#     "Морозов Илья Валерьевич",
#     "Мустяцэ Иван Иванович",
#     "Никулина Екатерина Александровна"
# ]
# """

# python_data = json.loads(json_string)
# print(type(python_data))
# print(python_data)

# Обратная операция
# ensure_ascii=False - отключает кодирование символов в ASCII
# indent=4 - отступы для каждого уровня вложенности

# json_string = json.dumps(python_data, ensure_ascii=False, indent=4)
# print(type(json_string))
# print(json_string)


# Запись в файл
# students.json - файл
# w - режим записи
# encoding="utf-8" - кодировка файла
# as file - file это переменная, которая будет содержать файл
# json.dump - dump - метод для записи в файл
# python_data - данные, которые мы хотим записать в файл
# file - файл, в который мы хотим записать данные
# ensure_ascii=False - отключает кодирование символов в ASCII
# indent=4 - отступы для каждого уровня вложенности
# with open("students.json", "w", encoding="utf-8") as file:
#     json.dump(python_data, file, ensure_ascii=False, indent=4)


# Чтение из файла
# r - режим чтения
# encoding="utf-8" - кодировка файла

# with open("students.json", "r", encoding="utf-8") as file:
#     python_data = json.load(file)


# print(type(python_data))
# print(python_data)


# Как сделать дозапись?
# Проблема в том, что мы не можем использовать флаг a, потому что он не поддерживается в json.dump. Мы конечно допишем туда строки, но мы сломаем структуру файла.

# Поэтому нам надо прочитать файл, добавить туда элементы, и записать обратно в файл.

# with open("students.json", "r", encoding="utf-8") as file:
#     python_data = json.load(file)


# new_student = "Новый студент3"
# python_data.append(new_student)

# with open("students.json", "w", encoding="utf-8") as file:
#     json.dump(python_data, file, ensure_ascii=False, indent=4)


def append_json(file_name: str, *data: str, indent: int = 4, encoding: str = "utf-8") -> None:
    """
    Функция для добавления данных в JSON файл. Работает с JSON массивами.
    :param file_name: Имя файла для записи.
    :param data: Данные для добавления в файл.
    :param indent: Отступы для каждого уровня вложенности.
    :param encoding: Кодировка файла.
    """
    with open(file_name, "r", encoding=encoding) as file:
        python_data = json.load(file)

    # Если python data не является списком, то вызываем ошибку
    if not isinstance(python_data, list):
        raise TypeError("Поддерживается только добавление в JSON массивы")
    
    python_data.extend(data)

    with open(file_name, "w", encoding=encoding) as file:
        json.dump(python_data, file, ensure_ascii=False, indent=indent)


file = "students.json"
append_json(file, "Новый студент1", "Новый студент2", "Новый студент3", indent=2)

new_student = ["Новый студент4", "Новый студент5"]
append_json(file, *new_student, indent=2)
