"""
Тема: ООП. Итераторы. Урок: 28
- Практика с итератором транскрипции

Мы будем работать с результатом работы локальной модели Wisper
Которая транскрибирует речь в текст.

На выходе мы получаем json файл формата

[
    {
        "timestamp": [
            0.0,
            4.62
        ],
        "text": " добро утра здравствуйте"
    },
    ...
]

Нашей задачей будет создать датакласс представляющий собой часть транскрибации и итератор
для перебора всех частей транскрибации.

1. Считать данные
2. Создать экземпляр датакласса с нужными данными
3. Отдать его дальше через __next__

TranscriptionChunk
text: str  Текст
int_start: int  Начало в секундах
int_end: int  Конец в секундах
str_start: str  Начало в строковом виде 00:00:00
str_end: str  Конец в строковом виде 00:00:00
"""

from dataclasses import dataclass, field
import json
from typing import Iterator, List, Dict, Optional

JSON_DATA = "lesson_27_ts.json"

@dataclass
class TranscriptionChunk:
    text: str
    float_start: float
    float_end: float
    str_start: str = field(init=False)
    str_end: str = field(init=False)

    def __post_init__(self):
        self.str_start = self._int_to_str(self.float_start)
        self.str_end = self._int_to_str(self.float_end)

    def _int_to_str(self, time: float) -> str:
        int_time = int(time)
        hours = int_time // 3600
        minutes = (int_time % 3600) // 60
        seconds = int_time % 60
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


class TranscriptionIterator:
    def __init__(self, transcription_data: List[Dict[str, List[Optional[float]]|str]]):
        self.transcription_data = transcription_data
        self.index = 0
        self.data_len = len(self.transcription_data)

    
    def __iter__(self) -> Iterator[TranscriptionChunk]:
        return self
    
    def __next__(self) -> TranscriptionChunk:
        if self.index >= self.data_len:
            raise StopIteration
        data = self.transcription_data[self.index]
        self.index += 1
        return self._chunk_serialize(data)
    
    def _chunk_serialize(self, data: Dict[str, List[Optional[float]]|str]) -> TranscriptionChunk:
        text = data['text']
        start = data['timestamp'][0]
        end = data['timestamp'][1] if data['timestamp'][1] is not None else start

        instance = TranscriptionChunk(text, start, end)
        return instance

# Тесрирование
def main():
    with open(JSON_DATA, "r", encoding="utf-8") as file:
        data = json.load(file)

    # Мы можем проитерироваться по данным
    # iterator = TranscriptionIterator(data)
    # for chunk in iterator:
    #     print(chunk)

    # Мы можем получить первые 5 кусочков
    iterator = TranscriptionIterator(data)
    for _ in range(5):
        print(next(iterator))


if __name__ == "__main__":
    main()
    pass
