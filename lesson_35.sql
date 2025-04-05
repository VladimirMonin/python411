-- Lesson 35 - Group By
-- Получаем уникальные значения столбца EYE из таблицы MarvelCharacters
SELECT DISTINCT EYE
FROM MarvelCharacters;


-- Тут выборка похожая. Но на самом деле она выполняется в 6-10 раз дольше. При этом формируются группы, с которыми мы можем работать.
SELECT EYE
FROM MarvelCharacters
GROUP BY EYE;


-- Группируем по глазам, считаем сколько всего в каждой группе
SELECT EYE, COUNT(*) AS Count
FROM MarvelCharacters
GROUP BY EYE;


-- Перед группировкой уберем всех героев с неизвестным цветом глаз
-- Очень большая разница в скорости работы запроса
-- Если есть возможность что-то убрать ДО группировки, лучше это сделать ДО
SELECT EYE, COUNT(*) AS Count
FROM MarvelCharacters
-- WHERE EYE IS NOT NULL
GROUP BY EYE
HAVING Count > 10 AND EYE IS NOT NULL;

-- HAVING - это WHERE для группировок


SELECT EYE, COUNT(*) AS Count
FROM MarvelCharacters
WHERE EYE IS NOT NULL
GROUP BY EYE
HAVING Count > 10
ORDER BY Count DESC
LIMIT 5;

--TODO - Сделайте подобный запрос по цветам волос

SELECT HAIR, COUNT(*) AS Count
FROM MarvelCharacters
WHERE HAIR IS NOT NULL
GROUP BY HAIR
HAVING Count > 10
ORDER BY Count DESC
-- LIMIT 5;

-- Группировка по HAIR и EYE чтобы понять наиболее популярные комбинации
SELECT HAIR, EYE, COUNT(*) AS Count, ROUND(AVG(YEAR)) AS AvgYear
FROM MarvelCharacters
WHERE HAIR IS NOT NULL AND EYE IS NOT NULL
GROUP BY HAIR, EYE
HAVING Count > 10
ORDER BY Count DESC


SELECT HAIR, COUNT(*) AS Count, Name AS MostPopularCharacter, APPEARANCES
FROM 
    (SELECT * FROM MarvelCharacters
    ORDER BY APPEARANCES DESC)
WHERE HAIR IS NOT NULL
GROUP BY HAIR
HAVING Count > 10
ORDER BY Count DESC

-- Взять предыдущий запрос и сортировать по YEAR 
-- в блоке FROM MarvelCharacters
-- и Выдать имя и количество появлений ранний героя в каждой группе

SELECT HAIR, EYE, COUNT(*) AS Count, Name, YEAR
FROM
    (SELECT * FROM MarvelCharacters
    WHERE YEAR IS NOT NULL
    ORDER BY YEAR)
WHERE HAIR IS NOT NULL AND EYE IS NOT NULL
GROUP BY HAIR, EYE
HAVING Count > 10
ORDER BY HAIR, YEAR

-- CTE - Common Table Expression
-- Временная таблица, которая существует только в рамках одного запроса
-- WITH - ключевое слово для создания CTE

-- Этот же запрос на CTE

WITH MarvelCharactersSorted AS
    (SELECT * FROM MarvelCharacters
    WHERE YEAR IS NOT NULL
    ORDER BY YEAR)

SELECT HAIR, EYE, COUNT(*) AS Count, Name, YEAR
FROM MarvelCharactersSorted
WHERE HAIR IS NOT NULL AND EYE IS NOT NULL
GROUP BY HAIR, EYE
HAVING Count > 10
ORDER BY HAIR, YEAR


-- Основная проблема здесь — некорректное использование GROUP BY в сочетании с особенностями SQLite. Когда мы группируем только по hair и eye, но при этом выбираем также Name и year, которые не включены в группировку, SQLite (в отличие от более строгих MySQL или PostgreSQL) не выдаёт ошибку, а просто берёт какое-то одно произвольное значение из группы для этих столбцов.

--Вот в чём подвох: SQLite не гарантирует, что это будет одно и то же значение при каждом выполнении запроса или при небольших изменениях в синтаксисе!


-- Сделаем группировку по полу
SELECT SEX, COUNT(*) AS Count, MAX(APPEARANCES) AS MaxAppearances, MIN(APPEARANCES) AS MinAppearances, ROUND(AVG(APPEARANCES)) AS AvgAppearances
FROM MarvelCharacters
GROUP BY SEX

--------------

-- Перечень агрегатных функций SQLite
-- MIN, MAX, AVG, SUM, COUNT, GROUP_CONCAT, 

SELECT name, MAX(APPEARANCES) AS MaxAppearances
FROM MarvelCharacters

SELECT COUNT(*)
FROM MarvelCharacters

SELECT COUNT(DISTINCT(EYE))
FROM MarvelCharacters

-- Пример с GROUP_CONCAT
SELECT HAIR, EYE, GROUP_CONCAT(Name) AS Names
FROM MarvelCharacters
GROUP BY HAIR, EYE
HAVING COUNT(*) > 10


-- Персонажи появлявшиеся в комиксах в 1960-х голубой цвет глаз, блондины, имена даем через запятую
SELECT HAIR, EYE, GROUP_CONCAT(Name) AS Names
FROM MarvelCharacters
WHERE YEAR BETWEEN 1960 AND 1969 AND EYE = 'Blye EYE' AND HAIR = 'Blond Hair'
GROUP BY HAIR, EYE;


-- Выборка имен похожих на man +  Группировка по цвету глаз + Вывод имен через CONCAT
SELECT EYE, GROUP_CONCAT(Name) AS Names
FROM MarvelCharacters
WHERE Name LIKE '%spider%'
GROUP BY EYE;


-- Группировка по году
SELECT YEAR, COUNT(*) AS Count
FROM MarvelCharacters
GROUP BY YEAR
ORDER BY YEAR DESC;

-- А если мы хотим сделать декады?
SELECT YEAR / 10 * 10 AS Decade, COUNT(*) AS Count
FROM MarvelCharacters
GROUP BY Decade
ORDER BY Decade DESC;

-- 1945 / 10 = 194 При деленеии дробная часть отсекается
-- 194 * 10 = 1940

SELECT YEAR / 10 * 10 AS Decade, COUNT(*) AS TotalChar, MAX(APPEARANCES) AS MaxAppearances

FROM MarvelCharacters
GROUP BY Decade
ORDER BY Decade DESC;
