"""
Lesson 41: ORM Peewee
ORM - Object Relational Mapping (На русском - Объектно-реляционное отображение)
pip install peewee - устанавливаем библиотеку peewee

СТРУКТУРА БД:
--
-- Файл сгенерирован с помощью SQLiteStudio v3.4.16 в Вс апр 13 12:38:43 2025
--
-- Использованная кодировка текста: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Таблица: groups
DROP TABLE IF EXISTS groups;
CREATE TABLE IF NOT EXISTS groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    group_name TEXT NOT NULL UNIQUE,
    start_date TEXT DEFAULT CURRENT_TIMESTAMP,
    end_date TEXT,
    profession_id INTEGER,
    FOREIGN KEY (profession_id) REFERENCES professions(id) ON DELETE SET NULL  ON UPDATE CASCADE
);
INSERT INTO groups (id, group_name, start_date, end_date, profession_id) VALUES (1, 'python411', '2025-04-12 09:14:07', NULL, 6);
INSERT INTO groups (id, group_name, start_date, end_date, profession_id) VALUES (2, 'js412', '2025-04-12 09:14:07', NULL, 5);

-- Таблица: professions
DROP TABLE IF EXISTS professions;
CREATE TABLE IF NOT EXISTS professions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL UNIQUE,
    description TEXT
);
INSERT INTO professions (id, title, description) VALUES (3, 'Frontend-разработчик', 'Создание пользовательского интерфейса веб-приложений на JavaScript');
INSERT INTO professions (id, title, description) VALUES (4, 'Backend-разработчик', 'Разработка серверной части веб-приложений на Python');
INSERT INTO professions (id, title, description) VALUES (5, 'Frontend-разработчик_2', 'Создание пользовательского интерфейса веб-приложений на JavaScript');
INSERT INTO professions (id, title, description) VALUES (6, 'Backend-разработчик_2', 'Разработка серверной части веб-приложений на Python');

-- Таблица: student_cards
DROP TABLE IF EXISTS student_cards;
CREATE TABLE IF NOT EXISTS student_cards (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        student_id INTEGER NOT NULL UNIQUE,

        number TEXT NOT NULL UNIQUE,

        FOREIGN KEY (student_id) REFERENCES students (id) ON DELETE CASCADE ON UPDATE CASCADE

    );
INSERT INTO student_cards (id, student_id, number) VALUES (1, 1, 'PY-0001');
INSERT INTO student_cards (id, student_id, number) VALUES (2, 2, 'PY-0002');
INSERT INTO student_cards (id, student_id, number) VALUES (3, 3, 'PY-0003');
INSERT INTO student_cards (id, student_id, number) VALUES (4, 4, 'PY-0004');
INSERT INTO student_cards (id, student_id, number) VALUES (5, 5, 'PY-0005');
INSERT INTO student_cards (id, student_id, number) VALUES (6, 6, 'JS-0006');
INSERT INTO student_cards (id, student_id, number) VALUES (7, 7, 'JS-0007');
INSERT INTO student_cards (id, student_id, number) VALUES (8, 8, 'JS-0008');
INSERT INTO student_cards (id, student_id, number) VALUES (9, 9, 'JS-0009');
INSERT INTO student_cards (id, student_id, number) VALUES (10, 10, 'JS-0010');

-- Таблица: students
DROP TABLE IF EXISTS students;
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    middle_name TEXT,
    last_name TEXT NOT NULL,
    age INTEGER,
    group_id INTEGER,
    -- Указание внешнего ключа
    FOREIGN KEY (group_id) REFERENCES groups(id) ON DELETE SET NULL ON UPDATE CASCADE
);
INSERT INTO students (id, first_name, middle_name, last_name, age, group_id) VALUES (1, 'Артём', 'Питонович', 'Серпентьев', 22, 1);
INSERT INTO students (id, first_name, middle_name, last_name, age, group_id) VALUES (2, 'Ольга', 'Джанговна', 'Фласкина', 19, 1);
INSERT INTO students (id, first_name, middle_name, last_name, age, group_id) VALUES (3, 'Виктор', 'Алгоритмович', 'Рекурсивный', 24, 1);
INSERT INTO students (id, first_name, middle_name, last_name, age, group_id) VALUES (4, 'Анна', 'Датафреймовна', 'Пандасова', 21, 1);
INSERT INTO students (id, first_name, middle_name, last_name, age, group_id) VALUES (5, 'Дмитрий', 'Генадьевич', 'Индентов', 20, 1);
INSERT INTO students (id, first_name, middle_name, last_name, age, group_id) VALUES (6, 'Светлана', 'Реактовна', 'Хуковская', 23, 2);
INSERT INTO students (id, first_name, middle_name, last_name, age, group_id) VALUES (7, 'Максим', 'Промисович', 'Аякcов', 20, 2);
INSERT INTO students (id, first_name, middle_name, last_name, age, group_id) VALUES (8, 'Ксения', 'Вьюевна', 'Компонентова', 19, 2);
INSERT INTO students (id, first_name, middle_name, last_name, age, group_id) VALUES (9, 'Игорь', 'Ноудович', 'Экспрессов', 25, 2);
INSERT INTO students (id, first_name, middle_name, last_name, age, group_id) VALUES (10, 'Алина', 'Домовна', 'Вёрсточкина', 22, 2);

-- Таблица: teachers
DROP TABLE IF EXISTS teachers;
CREATE TABLE IF NOT EXISTS teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    middle_name TEXT,
    last_name TEXT NOT NULL,
    age INTEGER,
    phone TEXT NOT NULL,
    email TEXT
);
INSERT INTO teachers (id, first_name, middle_name, last_name, age, phone, email) VALUES (1, 'Иван', 'Компиляторович', 'Кодмастеров', 45, '+7 (900) 123-45-67', 'codmaster@teachmail.ru');
INSERT INTO teachers (id, first_name, middle_name, last_name, age, phone, email) VALUES (2, 'Елена', 'Алгоритмовна', 'Сортирова', 38, '+7 (900) 234-56-78', 'sort_queen@teachmail.ru');
INSERT INTO teachers (id, first_name, middle_name, last_name, age, phone, email) VALUES (3, 'Николай', 'Фреймворкович', 'Библиотечный', 42, '+7 (900) 345-67-89', 'framework_guru@teachmail.ru');
INSERT INTO teachers (id, first_name, middle_name, last_name, age, phone, email) VALUES (4, 'Татьяна', 'Баговна', 'Дебаггер', 36, '+7 (900) 456-78-90', 'bug_hunter@teachmail.ru');
INSERT INTO teachers (id, first_name, middle_name, last_name, age, phone, email) VALUES (5, 'Михаил', 'Гитович', 'Коммитов', 41, '+7 (900) 567-89-01', 'never_merge_to_master@teachmail.ru');

-- Таблица: teachers_groups
DROP TABLE IF EXISTS teachers_groups;
CREATE TABLE IF NOT EXISTS teachers_groups (
    teacher_id INTEGER,
    group_id INTEGER,
    date_start TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (teacher_id) REFERENCES teachers(id)  ON DELETE SET NULL ON UPDATE CASCADE,
    FOREIGN KEY (group_id) REFERENCES groups(id)  ON DELETE SET NULL ON UPDATE CASCADE,
    PRIMARY KEY (teacher_id, group_id) -- составной первичный ключ
);
INSERT INTO teachers_groups (teacher_id, group_id, date_start) VALUES (1, 1, '2025-04-12 09:14:07');
INSERT INTO teachers_groups (teacher_id, group_id, date_start) VALUES (2, 1, '2025-04-12 09:14:07');
INSERT INTO teachers_groups (teacher_id, group_id, date_start) VALUES (5, 1, '2025-04-12 09:14:07');
INSERT INTO teachers_groups (teacher_id, group_id, date_start) VALUES (3, 2, '2025-04-12 09:14:07');
INSERT INTO teachers_groups (teacher_id, group_id, date_start) VALUES (4, 2, '2025-04-12 09:14:07');
INSERT INTO teachers_groups (teacher_id, group_id, date_start) VALUES (5, 2, '2025-04-12 09:14:07');

-- Таблица: teachers_professions
DROP TABLE IF EXISTS teachers_professions;
CREATE TABLE IF NOT EXISTS teachers_professions (
    teacher_id INTEGER,
    profession_id INTEGER,
    notions TEXT,
    FOREIGN KEY (teacher_id) REFERENCES teachers(id)  ON DELETE SET NULL ON UPDATE CASCADE,
    FOREIGN KEY (profession_id) REFERENCES professions(id)  ON DELETE SET NULL ON UPDATE CASCADE,
    PRIMARY KEY (teacher_id, profession_id) -- составной первичный ключ
);
INSERT INTO teachers_professions (teacher_id, profession_id, notions) VALUES (1, 6, 'Эксперт по Python с опытом написания кода во сне');
INSERT INTO teachers_professions (teacher_id, profession_id, notions) VALUES (2, 6, 'Может объяснить рекурсию рекурсивно, а потом нерекурсивно');
INSERT INTO teachers_professions (teacher_id, profession_id, notions) VALUES (3, 5, 'JavaScript-гуру, по слухам однажды починил Internet Explorer');
INSERT INTO teachers_professions (teacher_id, profession_id, notions) VALUES (4, 5, 'CSS-волшебница, умеет центрировать div с первого раза');
INSERT INTO teachers_professions (teacher_id, profession_id, notions) VALUES (5, 4, 'Универсальный боец, может работать full-stack даже на калькуляторе');

-- Индекс: idx_groups_name
DROP INDEX IF EXISTS idx_groups_name;
CREATE INDEX IF NOT EXISTS idx_groups_name ON groups(group_name);

-- Индекс: idx_groups_profession
DROP INDEX IF EXISTS idx_groups_profession;
CREATE INDEX IF NOT EXISTS idx_groups_profession ON groups(profession_id);

-- Индекс: idx_students_fullname
DROP INDEX IF EXISTS idx_students_fullname;
CREATE INDEX IF NOT EXISTS idx_students_fullname ON students(first_name, middle_name, last_name);

-- Индекс: idx_students_group
DROP INDEX IF EXISTS idx_students_group;
CREATE INDEX IF NOT EXISTS idx_students_group ON students(group_id);

-- Индекс: idx_students_lastname
DROP INDEX IF EXISTS idx_students_lastname;
CREATE INDEX IF NOT EXISTS idx_students_lastname ON students(last_name);

-- Индекс: idx_teachers_email
DROP INDEX IF EXISTS idx_teachers_email;
CREATE INDEX IF NOT EXISTS idx_teachers_email ON teachers(email);

-- Индекс: idx_teachers_fullname
DROP INDEX IF EXISTS idx_teachers_fullname;
CREATE INDEX IF NOT EXISTS idx_teachers_fullname ON teachers(first_name, middle_name, last_name);

-- Индекс: idx_teachers_lastname
DROP INDEX IF EXISTS idx_teachers_lastname;
CREATE INDEX IF NOT EXISTS idx_teachers_lastname ON teachers(last_name);

-- Индекс: idx_teachers_phone
DROP INDEX IF EXISTS idx_teachers_phone;
CREATE INDEX IF NOT EXISTS idx_teachers_phone ON teachers(phone);

-- Представление: student_info
DROP VIEW IF EXISTS student_info;
CREATE VIEW IF NOT EXISTS student_info AS

SELECT

    s.first_name,

    s.middle_name,

    s.last_name,

    s.age,

    g.group_name,

    sc.number AS student_card_number



FROM

    students s

LEFT JOIN groups g ON s.group_id = g.id

LEFT JOIN student_cards sc ON s.id = sc.student_id;

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;

"""

# 1. Установка peewee
# pip install peewee

# 2. Импортируем библиотеку peewee
import peewee as pw

# 3. Создаем подключение к базе данных SQLite
db = pw.SqliteDatabase("data/students_new.db")

# 4. Модель профессии


class Profession(pw.Model):
    title = pw.CharField(unique=True)
    description = pw.TextField(null=True)

    class Meta:
        database = db  # Указываем базу данных для этой модели
        table_name = "professions"  # Указываем имя таблицы в базе данных


# 5. Модель группы


class Group(pw.Model):
    group_name = pw.CharField(unique=True)
    start_date = pw.DateTimeField(constraints=[pw.SQL("DEFAULT CURRENT_TIMESTAMP")])
    end_date = pw.DateTimeField(null=True)
    profession = pw.ForeignKeyField(Profession, backref="groups", null=True)

    class Meta:
        database = db  # Указываем базу данных для этой модели
        table_name = "groups"  # Указываем имя таблицы в базе данных


# 6. Модель студента


class Student(pw.Model):
    first_name = pw.CharField()
    middle_name = pw.CharField(null=True)
    last_name = pw.CharField()
    age = pw.IntegerField(null=True)
    group = pw.ForeignKeyField(Group, backref="students", null=True)

    class Meta:
        database = db  # Указываем базу данных для этой модели
        table_name = "students"  # Указываем имя таблицы в базе данных


# 7. Сделаем тестовый запуск - получим всех студентов и выведем их на экран
all_students = Student.select()


# 8. Найдем студента с именем "Ольга" и выведем его на экран
student = Student.get(Student.first_name == "Ольга")

print(student.first_name, student.group, student.group.group_name)

# 9. Всех студентов старше 20 лет
all_students = Student.select().where(Student.age > 20)

for student in all_students:
    print(student.first_name, student.age)

# 10. Накинем на прошлую выборку фильтр - имена где есть "ан"
all_students = Student.select().where(Student.first_name.contains("ан"))

for student in all_students:
    print(student.first_name, student.age)

# 11. Найдем всех студентов группы "python411"
all_students = Student.select().join(Group).where(Group.group_name == "python411")

for student in all_students:
    print(student.first_name, student.age)

# 12. Найдем всех студентов группы "python411" и старше 20 лет
all_students = Student.select().join(Group).where(
    (Student.group.group_name == "python411") & (Student.age > 20)
)

for student in all_students:
    print(student.first_name, student.age, student.group.group_name)


"""
Select - инструмент возвращающий данные из базы данных в виде коллекции объектов
Where - фильтрует данные по заданному условию
Join - объединяет таблицы по заданному условию, в отличии от Django ORM мы явно должны указать по какому полю мы соединяем таблицы

Операторы:
    | - ИЛИ
    & - И
    


~ (тильда) - это логическое НЕ (NOT). Например: ~(Student.age > 20) - найдёт всех студентов, возраст которых НЕ больше 20 лет.

.contains() - проверяет, содержит ли строка подстроку. Например: Student.first_name.contains("Алек") - найдёт всех "Александров" и "Алексеев".

.startswith() и .endswith() - проверяют начало и конец строки. Например: Student.last_name.endswith("ов") - найдёт всех с фамилиями, оканчивающимися на "ов".

.in_() - проверяет, входит ли значение в список. Например: Student.age.in_([18, 19, 20]) - найдёт студентов определённых возрастов.

.not_in() - проверяет, что значение НЕ входит в список.

.is_null(True) и .is_null(False) - проверяют, является ли поле NULL или NOT NULL. Например: Student.middle_name.is_null(True) - найдёт студентов без отчества.

.between() - проверяет, находится ли значение в диапазоне. Например: Student.age.between(18, 25) - найдёт студентов в возрасте от 18 до 25 лет.    
"""

students = Student.select().join(Group).where(
    ((Student.age > 20) & (Group.group_name == "python411")) | 
    ((Student.age < 20) & (Group.group_name == "js412"))
)


######################### СОЗДАНИЕ НОВОЙ ЗАПИСИ #########################

# 13. Петр Петрович Петров, 25 лет, группа python411

# new_student = Student.create(
#     first_name="Петр",
#     middle_name="Петрович",
#     last_name="Петров",
#     age=25,
#     group=Group.get(Group.group_name == "python411"),
# )

# 14. Добуду всех студентов и выведу их на экран
all_students = Student.select()

for student in all_students:
    print(student.id, student.first_name, student.middle_name, student.last_name, student.age, student.group.group_name)

# У студента id=12 меняю отчество на "Сидорович"

student_12 = Student.get(Student.id == 12)
student_12.middle_name = "Сидорович"
student_12.save()  # Сохраняю изменения в базе данных


# Проверим изменения
student_12 = Student.get(Student.id == 12)
print(student_12.id, student_12.first_name, student_12.middle_name, student_12.last_name, student_12.age, student_12.group.group_name)