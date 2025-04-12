-- Профессии
CREATE TABLE
    IF NOT EXISTS professions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL UNIQUE,
        description TEXT
    );

-- Группы
CREATE TABLE
    IF NOT EXISTS groups (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        group_name TEXT NOT NULL UNIQUE,
        start_date TEXT DEFAULT CURRENT_TIMESTAMP,
        end_date TEXT,
        profession_id INTEGER,
        FOREIGN KEY (profession_id) REFERENCES professions (id) ON DELETE SET NULL ON UPDATE CASCADE
    );

-- Cтуденты
CREATE TABLE
    IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        middle_name TEXT,
        last_name TEXT NOT NULL,
        age INTEGER,
        group_id INTEGER,
        -- Указание внешнего ключа
        FOREIGN KEY (group_id) REFERENCES groups (id) ON DELETE SET NULL ON UPDATE CASCADE

    );

-- Таблица студ. билетов - пример связи Один-к-одному
CREATE TABLE
    IF NOT EXISTS student_cards (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER NOT NULL UNIQUE,
        number TEXT NOT NULL UNIQUE,
        FOREIGN KEY (student_id) REFERENCES students (id) ON DELETE CASCADE ON UPDATE CASCADE
    )

-- Таблица преподавателей
CREATE TABLE
    IF NOT EXISTS teachers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        middle_name TEXT,
        last_name TEXT NOT NULL,
        age INTEGER,
        phone TEXT NOT NULL,
        email TEXT
    )
    -- Таблица ПреподавателиГруппы - для связи Многие-ко-многим
CREATE TABLE
    IF NOT EXISTS teachers_groups (
        teacher_id INTEGER,
        group_id INTEGER,
        date_start TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (teacher_id) REFERENCES teachers (id) ON DELETE SET NULL ON UPDATE CASCADE,
        FOREIGN KEY (group_id) REFERENCES groups (id) ON DELETE SET NULL ON UPDATE CASCADE,
        PRIMARY KEY (teacher_id, group_id) -- составной первичный ключ
    );

-- Таблица ПреподавателиПрофессии
CREATE TABLE
    IF NOT EXISTS teachers_professions (
        teacher_id INTEGER,
        profession_id INTEGER,
        notions TEXT,
        FOREIGN KEY (teacher_id) REFERENCES teachers (id) ON DELETE SET NULL ON UPDATE CASCADE,
        FOREIGN KEY (profession_id) REFERENCES professions (id) ON DELETE SET NULL ON UPDATE CASCADE,
        PRIMARY KEY (teacher_id, profession_id) -- составной первичный ключ
    );

-- Транзакция - возможность сделать серию операций SQL неделимыми, атомарными. Провести серию оперций как одну. С возможностью всегда вернуться к исходному состоянию, если что-то пошло не так.
--BEGIN TRANSACTION -- откроет транзакцию
--ROLLBACK -- откат назад
-- COMMIT TRANSACTION -- сохранит
BEGIN TRANSACTION;

-- 1. Внесем 2 профессии
INSERT INTO
    professions (title, description)
VALUES
    (
        'Frontend-разработчик_2',
        'Создание пользовательского интерфейса веб-приложений на JavaScript'
    ),
    (
        'Backend-разработчик_2',
        'Разработка серверной части веб-приложений на Python'
    );

COMMIT TRANSACTION;
-- ROLLBACK;

-- Большая и важная транзакция по созданию виртуального кампуса "Кодеры Шутники"
BEGIN TRANSACTION;

-- Шаг 1: Создаем две эпичные группы
-- Мы использовали более элегантный подход с UNION ALL, который объединяет два запроса SELECT. Каждый запрос возвращает по одной строке, и после объединения мы получаем две строки, которые затем вставляются в таблицу.

INSERT INTO groups (group_name, profession_id)
SELECT 'python411', id FROM professions WHERE title = 'Backend-разработчик_2'
UNION ALL
SELECT 'js412', id FROM professions WHERE title = 'Frontend-разработчик_2';

-- Шаг 2: Добавляем в группу python411 пять будущих гениев бэкенда
INSERT INTO students (first_name, middle_name, last_name, age, group_id)
VALUES
    ('Артём', 'Питонович', 'Серпентьев', 22, (SELECT id FROM groups WHERE group_name = 'python411')),
    ('Ольга', 'Джанговна', 'Фласкина', 19, (SELECT id FROM groups WHERE group_name = 'python411')),
    ('Виктор', 'Алгоритмович', 'Рекурсивный', 24, (SELECT id FROM groups WHERE group_name = 'python411')),
    ('Анна', 'Датафреймовна', 'Пандасова', 21, (SELECT id FROM groups WHERE group_name = 'python411')),
    ('Дмитрий', 'Генадьевич', 'Индентов', 20, (SELECT id FROM groups WHERE group_name = 'python411'));

-- Шаг 3: Добавляем в группу js412 пять будущих магов фронтенда
INSERT INTO students (first_name, middle_name, last_name, age, group_id)
VALUES
    ('Светлана', 'Реактовна', 'Хуковская', 23, (SELECT id FROM groups WHERE group_name = 'js412')),
    ('Максим', 'Промисович', 'Аякcов', 20, (SELECT id FROM groups WHERE group_name = 'js412')),
    ('Ксения', 'Вьюевна', 'Компонентова', 19, (SELECT id FROM groups WHERE group_name = 'js412')),
    ('Игорь', 'Ноудович', 'Экспрессов', 25, (SELECT id FROM groups WHERE group_name = 'js412')),
    ('Алина', 'Домовна', 'Вёрсточкина', 22, (SELECT id FROM groups WHERE group_name = 'js412'));

-- Шаг 4: Выдаем всем студенческие билеты, чтобы легально посещали столовую
-- Здесь мы выбираем всех студентов из группы python411, формируем для них номера билетов с префиксом 'PY-', затем выбираем всех студентов из группы js412 и формируем для них номера с префиксом 'JS-'. А потом объединяем эти два набора данных с помощью UNION ALL и вставляем все строки одним запросом.


INSERT INTO student_cards (student_id, number)
SELECT id, 'PY-' || printf('%04d', id) FROM students WHERE group_id = (SELECT id FROM groups WHERE group_name = 'python411')
UNION ALL
SELECT id, 'JS-' || printf('%04d', id) FROM students WHERE group_id = (SELECT id FROM groups WHERE group_name = 'js412');



-- Шаг 5: Нанимаем пять преподавателей (с претензией на Нобелевскую премию по педагогике)
INSERT INTO teachers (first_name, middle_name, last_name, age, phone, email)
VALUES
    ('Иван', 'Компиляторович', 'Кодмастеров', 45, '+7 (900) 123-45-67', 'codmaster@teachmail.ru'),
    ('Елена', 'Алгоритмовна', 'Сортирова', 38, '+7 (900) 234-56-78', 'sort_queen@teachmail.ru'),
    ('Николай', 'Фреймворкович', 'Библиотечный', 42, '+7 (900) 345-67-89', 'framework_guru@teachmail.ru'),
    ('Татьяна', 'Баговна', 'Дебаггер', 36, '+7 (900) 456-78-90', 'bug_hunter@teachmail.ru'),
    ('Михаил', 'Гитович', 'Коммитов', 41, '+7 (900) 567-89-01', 'never_merge_to_master@teachmail.ru');

-- Шаг 6: Связываем преподавателей с профессиями (чтобы знали, что преподавать)
INSERT INTO teachers_professions (teacher_id, profession_id, notions)
VALUES
    (1, (SELECT id FROM professions WHERE title = 'Backend-разработчик_2'), 
     'Эксперт по Python с опытом написания кода во сне'),
    (2, (SELECT id FROM professions WHERE title = 'Backend-разработчик_2'), 
     'Может объяснить рекурсию рекурсивно, а потом нерекурсивно'),
    (3, (SELECT id FROM professions WHERE title = 'Frontend-разработчик_2'), 
     'JavaScript-гуру, по слухам однажды починил Internet Explorer'),
    (4, (SELECT id FROM professions WHERE title = 'Frontend-разработчик_2'), 
     'CSS-волшебница, умеет центрировать div с первого раза'),
    (5, (SELECT id FROM professions WHERE title LIKE 'Backend%' OR title LIKE 'Frontend%'), 
     'Универсальный боец, может работать full-stack даже на калькуляторе');

-- Шаг 7: Распределяем преподавателей по группам (пусть помучаются)
INSERT INTO teachers_groups (teacher_id, group_id)
VALUES
    -- К python группе приставляем Python-специалистов
    (1, (SELECT id FROM groups WHERE group_name = 'python411')),
    (2, (SELECT id FROM groups WHERE group_name = 'python411')),
    (5, (SELECT id FROM groups WHERE group_name = 'python411')),
    -- К JS группе приставляем фронтенд-магов
    (3, (SELECT id FROM groups WHERE group_name = 'js412')),
    (4, (SELECT id FROM groups WHERE group_name = 'js412')),
    (5, (SELECT id FROM groups WHERE group_name = 'js412'));  -- Универсал везде нужен

-- Шаг 8: Торжественно подтверждаем создание нашей виртуальной академии
COMMIT;

-- VIEW - получим данные по студентам, группам, билетам
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


SELECT * FROM student_info;

-- Если вдруг что-то пойдет не так, закомментируй COMMIT и раскомментируй строку ниже:
-- ROLLBACK;

-- Теперь можно проверить, как заполнились таблицы:
-- SELECT * FROM students;
-- SELECT * FROM student_cards;
-- SELECT * FROM teachers;
-- SELECT s.first_name, s.last_name, g.group_name FROM students s JOIN groups g ON s.group_id = g.id;
-- SELECT t.first_name, t.last_name, g.group_name FROM teachers t
--   JOIN teachers_groups tg ON t.id = tg.teacher_id
--   JOIN groups g ON tg.group_id = g.id;


-- Один-к-одному
-- Транзацкии
-- Индексы
-- Триггеры
-- Вью - представления
-- Оконные функции ????