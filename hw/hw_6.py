"""
Разбор HW_6

В данном задании вам предстоит создать классы для работы с различными типами файлов: JSON, TXT и CSV. Вы также создадите абстрактный класс, который будет предписывать методы для чтения, записи и добавления данных в файлы. Ваша задача — реализовать наследование и полиморфизм в Python с использованием библиотеки ABC.
"""

from abc import ABC, abstractmethod
import json
import csv

class AbstractFile(ABC):
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass

    @abstractmethod
    def append(self):
        pass


# TxtFile
class TxtFile(AbstractFile):
    """
    Класс для работы с текстовыми файлами.
    Один экземпляр - один файл.
    """
    
    def read(self) -> list[str]:
        """
        Метод для чтения текстового документа.
        :return: list[str]
        """
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return file.readlines()
            
        # except FileNotFoundError:
            # print("Файл не найден")
            # return []
        
        except FileNotFoundError as exc:
            raise FileNotFoundError(f"Файл {self.file_path} не найден") from exc
            # Мы могли бы создать пустой файл.

    def write(self, *lines: str)-> None:
        """
        Метод для записи текстового документа.
        :param *lines:

        """
       
        with open(self.file_path, "w", encoding="utf-8") as file:
            for line in lines:
                file.write(line + "\n")
    
      

    def append(self, *lines: str)-> None:
        """
        Метод для дозаписи текстового документа.
        :param *lines:
        """
     
        with open(self.file_path, "a", encoding="utf-8") as file:
            for line in lines:
                file.write(line + "\n")
    
     


# JsonFile
class JsonFile(AbstractFile):
    """
    Класс для работы с json файлами.
    Один экземпляр - один файл.
    """

    def read(self) -> list[dict]:
        """
        Метод для чтения json документа.
        :return: list[dict]
        """
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return json.load(file)

        except FileNotFoundError as exc:
            raise FileNotFoundError(f"Файл {self.file_path} не найден") from exc
        
        except json.JSONDecodeError as exc:
            raise ValueError(f"Файл {self.file_path} вероятно не валиден") from exc
        
        except Exception as exc:
            raise exc
        

    def write(self, *data: dict) -> None:
        """
        Метод для записи json документа.
        :param *data:
        """
        
        try:
            with open(self.file_path, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)

        except FileNotFoundError as exc:
            raise FileNotFoundError(f"Файл {self.file_path} не найден") from exc
        
    def append(self, *data: dict) -> None:
        """
        Метод для дозаписи json документа.
        """
        # 1. Прочитать файл
        old_file = self.read()
        # 2. Добавить данные
        old_file.extend(data)
        # 3. Записать файл
        self.write(*old_file)
        

# CsvFile
class CsvFile(AbstractFile):
    """
    Класс для работы с csv файлами.
    Один экземпляр - один файл.
    """
    def read(self) -> list[dict]:
        """
        Метод для чтения csv документа.
        :return: list[dict]
        """
        try:
            with open(self.file_path, "r", encoding="utf-8-sig") as file:
                reader = csv.DictReader(file, delimiter=";")
                return list(reader)
            
        except FileNotFoundError as exc:
            raise FileNotFoundError(f"Файл {self.file_path} не найден") from exc
        
        except Exception as exc:
            raise exc
        
    def write(self, *data: dict) -> None:
        """
        Метод для записи csv документа.
        :param *data:
        """
        try:
            with open(self.file_path, "w", encoding="utf-8-sig", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=data[0].keys(), delimiter=";")
                writer.writeheader()
                writer.writerows(data)

        # Ошибка когда файл занят другой программой
        except PermissionError as exc:
            raise PermissionError(
                f"Файл {self.file_path} занят другим процессом"
            ) from exc
        
    
    def append(self, *data: dict) -> None:
        """
        Метод для дозаписи csv документа.
        """
        try:
            with open(self.file_path, "a", encoding="utf-8-sig", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=data[0].keys(), delimiter=";")
                writer.writerows(data)
        
        except PermissionError as exc:
            raise PermissionError(
                f"Файл {self.file_path} занят другим процессом"
            ) from exc


if __name__ == "__main__":
    # TxtFile
    txt_file = TxtFile("data.txt")
    txt_file.write("Hello, world!", "This is a test.", "Another line.")
    txt_file.append("And another line.")
    print(txt_file.read())

    # JsonFile
    json_file = JsonFile("data.json")
    

    data = [
        {"name": "John", "age": 30, "city": "New York"},
        {"name": "Jane", "age": 25, "city": "London"},
        {"name": "Bob", "age": 40, "city": "Paris"},
    ]
    json_file.write(*data)


    new_data = [
        {"name": "Alice", "age": 28, "city": "Berlin"},
        {"name": "Mike", "age": 35, "city": "Tokyo"},
    ]

    json_file.append(*new_data)

    print(json_file.read())

    # CsvFile
    csv_file = CsvFile("data.csv")
    
    csv_file.write(*data)
    csv_file.append(*new_data)
    print(csv_file.read())




