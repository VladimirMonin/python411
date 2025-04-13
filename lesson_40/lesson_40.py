"""
Lesson 40: Встроенная в Python библиотека sqlite3

- Импорт
- Основные сущности
- Объект connection - соединение с БД
- Объект cursor - курсор
"""
import sqlite3

DDL_SCRIPT = './lesson_40/lesson_40.sql'
DATA_BASE = './data/students.db'


# Создание подключения к базе данных
connection = sqlite3.connect(DATA_BASE)

# Создание курсора
cursor = connection.cursor()

# Прочитаем файл lesson_40.sql и выполним серию запросов
# Открываем файл и читаем его содержимое
# with open(DDL_SCRIPT, 'r', encoding='utf-8') as file:
#     sql_script = file.read()

# Выполняем Весь скрипт SQL
# cursor.executescript(sql_script)

# executescript - выполняет несколько SQL-команд в одном вызове
# execute - выполняет одну SQL-команду
# executemany - выполняет одну SQL-команду несколько раз с разными параметрами
# fetchone() — принеси-ка мне одну запись - кортеж
# fetchall() — давай всё и сразу! список кортежей
# fetchmany(size) — принеси-ка мне несколько записей
# description - описание столбцов
# rowcount - количество строк, затронутых последним запросом
# lastrowid - ид последней вставленной строки
# close - закрывает соединение с БД

# Пример запроса на выборку данных о студентах
SELECT_QUERY_1 = "SELECT * FROM students"
SELECT_QUERY_2 = """
SELECT st.first_name, st.last_name, st.age, gr.group_name
FROM students st
LEFT JOIN groups gr ON st.group_id = gr.id
"""

GROUP_NAME = "js412"

SELECT_QUERY_3 = f"""
SELECT st.first_name, st.middle_name, st.last_name, st.age, gr.group_name
FROM students st
LEFT JOIN groups gr ON st.group_id = gr.id
WHERE group_name = '{GROUP_NAME}'
"""

# Заставляем работать курсор
# all_students = cursor.execute(SELECT_QUERY_3).fetchmany(2) 
# print(type(all_students))
# print(all_students)

# Пример параметризованного запроса
GROUP_NAME = "python411"

SELECT_QUERY_PARAM_1 = """
SELECT st.first_name, st.middle_name, st.last_name, st.age, gr.group_name
FROM students st
LEFT JOIN groups gr ON st.group_id = gr.id
WHERE group_name = ?
"""

# Заставляем работать курсор
# all_students = cursor.execute(SELECT_QUERY_PARAM_1, (GROUP_NAME,)).fetchall()
# print(type(all_students))
# print(all_students)

# Добавляем первого студента через обычный execute
first_student = ("Кодов", "Питон", "Змеевич", 22, 1)
print(f"Добавляем первого студента: {first_student}")

INSERT_QUERY_PARAM_1 = """
INSERT INTO students (first_name, middle_name, last_name, age, group_id)
VALUES (?, ?, ?, ?, ?)
"""

# Заставляем работать курсор
cursor.execute(INSERT_QUERY_PARAM_1, first_student)


# Сохраняем изменения
connection.commit()

# Закрываем соединение с БД
connection.close()


# Для функций
# Создаем объект connection 1 раз снаружи функции ГЛОБАЛЬНО НА ФАЙЛ
# Внутрь передаем connection, и данные
# Внутри функции описан параметризованный запрос к БД
# Функция выполняет запрос, если надо делает commit и закрывает соединение

###############
DATA_BASE = './data/students.db'
connection = sqlite3.connect(DATA_BASE)

def add_student(connection: sqlite3.Connection, student: tuple):
    """
    Добавляет студента в БД
    :param connection: соединение с БД
    :param student: кортеж со значениями студента
    """
    # Создаем курсор
    cursor = connection.cursor()

    INSERT_QUERY_PARAM_1 = """
    INSERT INTO students (first_name, middle_name, last_name, age, group_id)
    VALUES (?, ?, ?, ?, ?)
    """

    # Выполняем запрос на добавление студента
    cursor.execute(INSERT_QUERY_PARAM_1, student)

    # Сохраняем изменения
    connection.commit()

    

# Тестируем функцию
# Добавляем первого студента через функцию
first_student = ("Кодов", "Питон", "Змеевич", 22, 1)
print(f"Добавляем первого студента: {first_student}")
add_student(connection, first_student)