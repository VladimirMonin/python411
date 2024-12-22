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


def append_json(
    file_name: str, *data: str, indent: int = 4, encoding: str = "utf-8"
) -> None:
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


# file = "students.json"
# append_json(file, "Новый студент1", "Новый студент2", "Новый студент3", indent=2)

# new_student = ["Новый студент4", "Новый студент5"]
# append_json(file, *new_student, indent=2)


# CSV (Comma-Separated Values)
# CSV - это текстовый формат данных, который используется для представления табличных данных.

students_list = [
    ["lastname", "firstname", "middlename"],
    ["Монин", "Владимир", "Александрович"],
    ["Артемьев", "Алексей", "Львович"],
    ["Багаутдинов", "Ринат", "Дмитриевич"],
    ["Балагуров", "Артем", "Алексеевич"],
    ["Бибиков", "Кирилл", "Сергеевич"],
    ["Крылов", "Илья", "Сергеевич"],
    ["Кряжев", "Руслан", "Анатольевич"],
    ["Кузнецов", "Иван", "Станиславович"],
    ["Лапицкая", "Наталья", "Владимировна"],
    ["Мазуренко", "Кристина", "Владимировна"],
    ["Морозов", "Илья", "Валерьевич"],
    ["Мустяцэ", "Иван", "Иванович"],
    ["Никулина", "Екатерина", "Александровна"],
]

# with open("students.csv", "w", encoding="utf-8-sig") as file:
#     writer = csv.writer(file, delimiter=";", lineterminator="\n")
#     writer.writerows(students_list)

# writerows - записывает список списков в файл
# writerow - записывает строку
# utf-8-sig - кодировка файла для успешного чтения в Excel
# delimiter=";" - разделитель полей (Для Excel)
# lineterminator="\n" - конец строки


# new_student = ["Киркоров", "Филлипп", "Бедросович"]


# with open("students.csv", "a", encoding="utf-8-sig") as file:
#     writer = csv.writer(file, delimiter=";", lineterminator="\n")
#     writer.writerow(new_student)


# with open("students.csv", "r", encoding="utf-8-sig") as file:
#     reader = csv.reader(file, delimiter=";")
#     students_list = list(reader)


print(students_list)


students_dict = [
    {"lastname": "Монин", "firstname": "Владимир", "middlename": "Александрович"},
    {"lastname": "Артемьев", "firstname": "Алексей", "middlename": "Львович"},
    {"lastname": "Багаутдинов", "firstname": "Ринат", "middlename": "Дмитриевич"},
    {"lastname": "Балагуров", "firstname": "Артем", "middlename": "Алексеевич"},
    {"lastname": "Бибиков", "firstname": "Кирилл", "middlename": "Сергеевич"},
    {"lastname": "Крылов", "firstname": "Илья", "middlename": "Сергеевич"},
    {"lastname": "Кряжев", "firstname": "Руслан", "middlename": "Анатольевич"},
    {"lastname": "Кузнецов", "firstname": "Иван", "middlename": "Станиславович"},
    {"lastname": "Лапицкая", "firstname": "Наталья", "middlename": "Владимировна"},
    {"lastname": "Мазуренко", "firstname": "Кристина", "middlename": "Владимировна"},
    {"lastname": "Морозов", "firstname": "Илья", "middlename": "Валерьевич"},
    {"lastname": "Мустяцэ", "firstname": "Иван", "middlename": "Иванович"},
    {"lastname": "Никулина", "firstname": "Екатерина", "middlename": "Александровна"},
]

# Запись списка словарей
# fieldnames - это названия для столбцов
# .writeheader() - записывает заголовки
# with open("students.csv", "w", encoding="utf-8-sig") as file:
#     writer = csv.DictWriter(
#         file, fieldnames=students_dict[0].keys(), delimiter=";", lineterminator="\n"
#     )
#     writer.writeheader()
#     writer.writerows(students_dict)


new = {"lastname": "Киркоров", "firstname": "Филлипп", "middlename": "Бедросович"}


# Код дозаписи
# with open("students.csv", "a", encoding="utf-8-sig") as file:
#     writer = csv.DictWriter(
#         file, fieldnames=students_dict[0].keys(), delimiter=";", lineterminator="\n"
#     )
#     writer.writerow(new)


# Код чтения
with open("students.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file, delimiter=";")
    students_dict = list(reader)

from pprint import pprint

pprint(students_dict, sort_dicts=False, width=100)

# pip install tabulate
from tabulate import tabulate

# Отобразим список словарей в виде таблицы
print(tabulate(students_dict, headers="keys", tablefmt="grid"))

# Отобразим список списков в виде таблицы
print(tabulate(students_list, headers="firstrow", tablefmt="grid"))


# Сначала получаем HTML таблицу из tabulate
html_table = tabulate(students_dict, headers="keys", tablefmt="html")

# Модифицируем таблицу, добавляя нужные классы Bootstrap 5
# Заменяем стандартный тег table на table с классами BS5
styled_table = html_table.replace(
    '<table>', 
    '<table class="table table-striped table-hover">'
)

html_template = f"""
<!doctype html>
<html lang="ru">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Список студентов</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
        <div class="container mt-5">
            <h1 class="mb-4">Список студентов</h1>
            {styled_table}
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
    </body>
</html>
"""


with open("students.html", "w", encoding="utf-8") as file:
    file.write(html_template)


