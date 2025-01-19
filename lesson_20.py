"""
19.01.2025
Тема: ООП Ч5. Наследование. Множественное. Иерархическое. MRO. Урок: 20
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

    def __str__(self) -> str:
        return f"{self.__class__.__name__} - {self.file_path}"


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


class PdfDocument(AbstractDocument):
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


# abstract = AbstractDocument() # Это не работает. Мы не можем создать экземпляр абстрактного класса
md_file = MarkdownDocument("file.md")
pdf_file = PdfDocument("file.pdf")

print(md_file)
print(pdf_file)

# MarkdownDocument - file.md
# PdfDocument - file.pdf