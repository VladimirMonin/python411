"""
Lesson 19
18.01.2025

Тема: ООП Ч4. Наследование. Abstractmethod. Super. Переопределение и расширение. Урок: 19
- Базовый пример на следования
- __str__ - метод, который возвращает строку с описанием объекта
- Переопределение метода voice в наследнике
- Проверка доступа защищенных и приватных атрибутов в наследнике (защищенные доступны, приватные нет)
- super и запуск инициализатора родителя
- Отвлеклись на Дебаггер
- ABC - abstract base class - базовый абстрактный класс, который может иметь абстрактные методы
- @abstractmethod - обязывает наследников реализовать метод с этим названием (совпадение только по имени метода)
"""

from abc import ABC, abstractmethod


class AbstractDocument(ABC):
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
    
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def append(self):
        pass
    
    @abstractmethod
    def write(self):
        pass


class MarkdownDocument(AbstractDocument):
    def __init__(self, file_path: str) -> None:
        super().__init__(file_path)

    def open(self):
        pass
    def read(self):
        pass
    def append(self):
        pass
    def write(self):
        pass


md_file = MarkdownDocument("file.md")
# TypeError: Can't instantiate abstract class MarkdownDocument without an implementation for abstract methods 'append', 'open', 'read', 'write'