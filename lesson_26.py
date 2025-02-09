"""
Тема: Функции. Аннотации типов. Typing. Декораторы. Урок: 26
"""

"""
ПРОСТАЯ АННОТАЦИЯ ТИПОВ

:int - Целое число (integer)
:float - Число с плавающей точкой (float)
:str - Строка (string)
:bool - Булево значение (boolean)
:list - Список (list)
:tuple - Кортеж (tuple)
:dict - Словарь (dictionary)
:None - Пустое значение (None)
:set - Множество (set)

Простая аннотация коллекций

:list[int] - Список целых чисел (list of integers)
:list[str] - Список строк (list of strings)
:list[dict] - Список словарей (list of dictionaries)
:set[int] - Множество целых чисел (set of integers)
set|list - Пайплайн - ИЛИ
"""

"""
РАСШИРЕННЫЕ АННОТАЦИИ ТИПОВ

from typing import List, Tuple, Set, Dict, Callable, Iterable, Iterator, Any, Union, Optional

Callable - вызываемый объект
Any - любой (вы незнаете, или там много типов)
Iterable - итерируемый объект
Iterator - итератор
Union - логическое или
Optional - что то одно. Или тип данных или None


Dict[str, List[Union[int, str]]] - Словарь с ключами типа str и значениями типа списка, содержащего целые числа или строки
pip install mypy
"""
from typing import List, Tuple, Set, Dict, Callable, Iterable, Iterator, Any, Union, Optional

list_num = ['1', 2, 3, 4, 5]


def func(num: List[int])->None:
    print(num)

func(list_num)

class MyClass:
    pass

cl: MyClass = MyClass()

def alpha_func(func: Callable[[List[int]], None]):
    pass