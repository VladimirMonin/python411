"""
Тема: Функции. Области видимости. Замыкания. Декоратор. Урок: 25
- Области видимости
Buit-in - встроенная
Global - глобальная
Local - локальная
Nonlocal - нелокальная
"""

# Buit-in - встроенная
# print()
# len()
# sum()
# bool()

# Global - глобальная - область видимости файла
a = 5


# Local - область видимости внутри функций \ методов
def func():
    a = 10
    print(a)

def func2():
    a = 15
    print(a)

def func3():
    print(a)

def func4(a: int) -> None:
    """
    Печатает число
    :param a: число для печати
    """
    print(a)

def func6():
    global a, b
    a = 20
    b = 22
    print(f'{a=} внутри ')

# print = "печенька"
# print("!") # 'str' object is not callable

# Проверим a
print(f'{a=}')

# Вызов 2 функций
func()
func2()

# Проверим a
print(f'{a=}')

# Вызов функции 6
func6()

# Проверим a
print(f'{a=}')

# Проверим b
print(f'{b=}')

def func7():
    a = 7
    print(f'Функция 7 {a=}')

    def built7():
        # В зависимости от наличия строки, а в func7 будет / не будет перписываться
        nonlocal a 
        a = 77
        print(f'Встроенная функция 7 {a=}')

    built7()
    print(f'Функция 7 после вызова built7 {a=}')

# Вызов функции 7
func7()
# Функция 7 a=7
# Встроенная функция 7 a=77
# Функция 7 после вызова built7 a=77


def fucn8(a):
    # a - хранится тут
    def inner8():
        # a - используется тут
        print(a)
    return inner8

banan = print
banan("Привет!")

# Вызов функции 8
foo = fucn8("пирожок")
foo()
