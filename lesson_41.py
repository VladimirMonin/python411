"""
Lesson 41: ORM Peewee
ORM - Object Relational Mapping (На русском - Объектно-реляционное отображение)
pip install peewee - устанавливаем библиотеку peewee

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

    def __str__(self):
        return f"Имя: {self.first_name}, Фамилия: {self.last_name}, Возраст: {self.age}, Группа: {self.group.group_name}"

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


"""
Создание __str__ Для моделей - чтобы упростить себе жизнь и не писать каждый раз print(student.first_name, student.middle_name, student.last_name, student.age, student.group.group_name)

Обновление и у даление данных объектов
Обновление и у даление связанных данных объектов

Использование backref для обратной связи между моделями

Связка многие-ко-многим

Миграции????
"""