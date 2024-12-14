"""
Урок 12
14.12.2024

Python функции. Аргументы и модули. Библиотеки plyer и requests. Урок: 12


1. Повторение функций:
    - DRY и SRP принципы
    - Объявление функций (def)
    - Вызов функций
    - Возврат значений (return)
    - Базовые проверки типов (isinstance)

2. Типы аргументов функций:
    - Позиционные аргументы
    - Именованные аргументы  
    - Аргументы по умолчанию
    - Обязательные и необязательные аргументы

3. Работа с внешними библиотеками:
    - Установка через pip
    - Импорт модулей
    - Библиотека plyer для уведомлений
    - Библиотека requests для HTTP запросов

4. Создание модулей:
    - Разделение кода на модули
    - Импорт собственных модулей
    - Относительные и абсолютные импорты
    - __name__ == '__main__'

5. Практика:
    - Создание функций для работы с API
    - Отправка уведомлений через plyer
    - Получение данных через requests
    - Структурирование кода в модули

    """


def is_palindrome(text: str) -> bool:
    """
    Функция проверки на палиндром

    Arguments:
        text -- строка которую нужно проверить

    Returns:
        bool -- True если строка палиндром, False если нет
    """
    ready_string = text.lower().replace(" ", "").replace(",", "").replace(".", "")
    return ready_string == ready_string[::-1]


"""
Типы аргументов функций:
4. *args и **kwargs:
    - *args (звездочка и аргументы) - это способ передачи произвольного количества позиционных аргументов в функцию.
    - **kwargs (две звездочки и аргументы) - это способ передачи произвольного количества именованных аргументов в функцию.
"""

product_list = ["хлеб", "молоко", "яйца", "сыр"]

product1, product2, *other = product_list
print(product1, product2, other)


new_product = [product_list[0], product_list[1], product_list[2], product_list[3]]

new_product = [*product_list]
print(new_product)
new_product = (*product_list, "банан")
print(new_product)


print("Hello")
print("Hello", "My name is", "Alex")


def is_palindrome2(*strings: str) -> list[bool]:
    """
    Функция проверки на палиндром
    """
    result_list = []
    for string in strings:
        ready_string = string.lower().replace(" ", "").replace(",", "").replace(".", "")
        result_list.append(ready_string == ready_string[::-1])

    return result_list


print(is_palindrome2("hello", "world", "шалаш", "а роза упала на лапу азора"))
