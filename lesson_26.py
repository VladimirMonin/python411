"""
Тема: Функции. Аннотации типов. Typing. Декораторы. Урок: 26
"""

from typing import Callable

# Декоратор
def decorator_1(func: Callable):
    def wrapper():
        print("До вызова функции")
        func()
        print("После вызова функции")
    return wrapper

def print_hello():
    print("Hello!")

def print_goodbye():
    print("Goodbye!")

print_hello_decarated = decorator_1(print_hello)
print_goodbye_decarated = decorator_1(print_goodbye)

print_hello_decarated()
print_goodbye_decarated()

def decorator_2(func: Callable[[str], str]) -> Callable[[str], str]:
    
    def wrapper(s: str) -> str:
        print("До вызова функции")
        result = func(s)
        print("После вызова функции")
        return result
    
    return wrapper

def print_hello_2(s: str) -> str:
    return f"Hello 2, {s}"

# Декорирование - учебный пример
print_hello_2_decarated = decorator_2(print_hello_2)
print(print_hello_2_decarated("Анатолий"))

# Как пишут на самом деле
@decorator_2
def print_goodbye_2(s: str) -> str:
    return f"Goodbye 2, {s}"

print(print_goodbye_2("Анатолий"))


# Этот декоратор будедет работать ТОЛЬКО с функциями которые принемают 1 аргумент.
# Если 2 - то будет падать

# @decorator_2
# def print_hello_3(name: str, age: int) -> str:
#     return f"Hello 3, {name}, {age}"

# print(print_hello_3("Анатолий", 30))
# TypeError: decorator_2.<locals>.wrapper() takes 1 positional argument but 2 were given

def decorator_3(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        print("Что-то делаем ДО вызова функции")
        result = func(*args, **kwargs)
        print("Что-то делаем ПОСЛЕ вызова функции")
        return result
    
    return wrapper

@decorator_3
def print_hello_3(name: str, age: int) -> str:
    return f"Hello 3, {name}, {age}"

print(print_hello_3("Анатолий", 30))
print(print_hello_3(name="Василий", age=40))