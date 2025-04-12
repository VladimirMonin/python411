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


-- Таблица преподавателей
CREATE TABLE IF NOT EXISTS teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    middle_name TEXT,
    last_name TEXT NOT NULL,
    age INTEGER,
    phone TEXT NOT NULL,
    email TEXT
)

-- Таблица ПреподавателиГруппы - для связи Многие-ко-многим

CREATE TABLE IF NOT EXISTS teachers_groups (
    teacher_id INTEGER,
    group_id INTEGER,
    date_start TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- тайметка в формате 2025-04-06 12:00:00
    FOREIGN KEY (teacher_id) REFERENCES teachers(id),
    FOREIGN KEY (group_id) REFERENCES groups(id),
    -- UNIQUE (teacher_id, group_id), -- уникальная пара
    PRIMARY KEY (teacher_id, group_id) -- составной первичный ключ
);

-- TIMESTAMP DEFAULT CURRENT_TIMESTAMP - это поле будет автоматически заполняться текущей датой и временем при добавлении записи
-- 

-- Добавим еще 2 группы
INSERT INTO groups (group_name)
VALUES ("python412"), ("python413");


-- Добавим преподавателей
INSERT INTO teachers (first_name, last_name, phone)
VALUES
("Сергей", "Бурунов", "+7(999)999-99-99"),
("Станислав", "Петров", "+7(888)888-88-88"),
("Григорий", "Безруков", "+7(777)777-77-77"),
("Тарзан", "Тарзанович", "+7(666)666-66-66");

-- Сделать связку преподавателей и групп
INSERT INTO teachers_groups (teacher_id, group_id)
VALUES
(1, 1),
(1, 2);


-- Найти ID Петрова, и найти ID группы python412 и назначить его преподавателем в эту группу

INSERT INTO teachers_groups (teacher_id, group_id)
VALUES
((SELECT id FROM teachers WHERE last_name = "Петров"),
(SELECT id FROM groups WHERE group_name = "python412"));


-- Выборка всех групп и преподавателей
-- Тут 3 запроса. По сути мы просто выбираем, какая таблица будет "Левая" - FROM
-- А какие будем присоединять через JOIN

-- Основная таблица - teachers_groups
SELECT tch.first_name, tch.last_name, g.group_name
FROM teachers_groups tg
JOIN teachers tch ON tg.teacher_id = tch.id
JOIN groups g ON tg.group_id = g.id;

-- Основная таблица - teachers
SELECT tch.first_name, tch.last_name, g.group_name
FROM teachers tch
JOIN teachers_groups tg ON tch.id = tg.teacher_id
JOIN groups g ON tg.group_id = g.id;

-- Основная таблица - groups
SELECT tch.first_name, tch.last_name, g.group_name
FROM groups g
JOIN teachers_groups tg ON g.id = tg.group_id
JOIN teachers tch ON tg.teacher_id = tch.id;



-- Получить всех преподавателей группы python412
SELECT tch.first_name AS f_name, tch.last_name AS l_name
FROM teachers tch
JOIN teachers_groups tg ON tch.id = tg.teacher_id
JOIN groups g ON tg.group_id = g.id
WHERE g.group_name = "python412";


SELECT tch.first_name, tch.last_name, GROUP_CONCAT(g.group_name) AS groups, COUNT(g.group_name) AS count_groups
FROM teachers tch
JOIN teachers_groups tg ON tch.id = tg.teacher_id
JOIN groups g ON tg.group_id = g.id
GROUP BY tch.id;

-- Создать студ-билеты. 
-- Сделать Один-к-одному студ-билет и студент
-- Посмотреть проблемы (перекрестная зависимость, потребность в истории студ-билетов на студента)

-- Операции CRUD на связанных таблицах
-- Как добывать данные через многие-ко-многим