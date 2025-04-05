-- Lesson 37
-- Содали новую БД students для экспериментов с созданием таблиц и CRUD
-- CRUD - Create, Read, Update, Delete 
-- AUTOINCREMENT - автоматическая генерация уникального значения для поля id

-- Создание таблицы студентов

CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    middle_name TEXT DEFAULT "Без отчества",
    last_name TEXT NOT NULL,
    age INTEGER,
    group_name TEXT NOT NULL
);

-- Добавим одного студента
INSERT INTO students (first_name, last_name, group_name)
VALUES ("Филлип", "Киркоров", "pyhton411");

-- Проверим что студент добавился
SELECT * FROM students;

-- Обновим данные Киркорова - возраст и отчество
UPDATE students
SET age = 40, middle_name = "Бедросович"
WHERE id = 1;

-- Проверим что студент добавился
SELECT * FROM students;

-- Удалим студента
DELETE FROM students
WHERE id = 1;

-- Массовое добавление студентов
INSERT INTO students (first_name, middle_name, last_name, age, group_name)
VALUES
("Анастасия", "Ивановна", "Ивлеева", 30, "python411"),
("Филлип", "Бедросович", "Киркоров", 50, "python411"),
("Владимир", "Николаевич", "Путов", 30, "python411"),
("Григорий", "Станиславович", "Шлепс", 60, "python411");


-- Проверим что студент добавился
SELECT * FROM students;

-- Удаление таблицы
DROP TABLE IF EXISTS students;


--------------------- Один ко многим ----------------------

-- Создание таблицы Групп

CREATE TABLE IF NOT EXISTS groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    group_name TEXT NOT NULL UNIQUE
);

-- Создание таблицы студентов

CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    middle_name TEXT,
    last_name TEXT NOT NULL,
    age INTEGER,
    group_id INTEGER,
    -- Указание внешнего ключа
    FOREIGN KEY (group_id) REFERENCES groups(id)
);

-- Явно включим проверку целостности ключей 
PRAGMA foreign_keys = ON;

-- Создание группы 411
INSERT INTO groups (group_name)
VALUES ("python411");



-- Массовое добавление студентов
INSERT INTO students (first_name, middle_name, last_name, age, group_id)
VALUES
("Анастасия", "Ивановна", "Ивлеева", 30, 1),
("Филлип", "Бедросович", "Киркоров", 50, 1),
("Владимир", "Николаевич", "Путов", 30, 1),
("Григорий", "Станиславович", "Шлепс", 60, 1);


-- Массовое добавление студентов
INSERT INTO students (first_name, middle_name, last_name, age, group_id)
VALUES
("Илон", Null, "Маск", 30, Null);


-- Проверим что студент добавился
SELECT * FROM students;


---- Получим студентов
-- МЫ не увидим тут Илона Маска, потому что у него group_id = NULL
-- И SQL при обычном JOIN не будет его учитывать
-- JOIN = INNER JOIN (т.е. NOT NULL с обоих сторон)
SELECT first_name, last_name, group_name
FROM students
JOIN groups ON students.group_id = groups.id;


-- Однако мы можем использовать LEFT JOIN
-- LEFT JOIN даст нам акцент на "левую" таблицу (та которая в SELECT) - это позвлит увидеть и тех студентов, у которых group_id = NULL
SELECT first_name, last_name, group_name
FROM students
LEFT JOIN groups ON students.group_id = groups.id;


-- Сделать преподов
-- Сделать Многие-ко-многим преподы и группы

-- Создать студ-билеты. 
-- Сделать Один-к-одному студ-билет и студент
-- Посмотреть проблемы (перекрестная зависимость, потребность в истории студ-билетов на студента)

-- Операции CRUD на связанных таблицах
-- Как добывать данные через многие-ко-многим