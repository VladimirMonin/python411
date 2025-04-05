-- Lesson 36. Перешли на marvel_normal базу

SELECT *
FROM MarvelCharacters

-- Имена героев и названия цвета глаз

SELECT MarvelCharacters.name, EyeColor.color
FROM MarvelCharacters
JOIN EyeColor
ON MarvelCharacters.eye_id = EyeColor.eye_id

-- Дальше вы можете делать запросы как к одной таблице
SELECT MarvelCharacters.name, EyeColor.color
FROM MarvelCharacters
JOIN EyeColor
ON MarvelCharacters.eye_id = EyeColor.eye_id
GROUP BY EyeColor.color



SELECT MC.name, EC.color, COUNT(*) AS count
FROM MarvelCharacters MC
JOIN EyeColor EC
ON MC.eye_id = EC.eye_id
GROUP BY EC.color
ORDER BY count DESC