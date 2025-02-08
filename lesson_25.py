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
