"""
Тема: ООП Ч10. Знакомство с паттернами. Урок: 29
- Одиночка (Singleton)
"""

class SingleTone:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __str__(self):
        return f'Экземпляр класса SingleTone id: {id(self)}'



if __name__ == '__main__':
    first = SingleTone()
    second = SingleTone()
    print(first)
    print(second)

# Экземпляр класса SingleTone id: 1990843985808
# Экземпляр класса SingleTone id: 1990843985808