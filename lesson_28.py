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

    ITERATIONS_MODE = {
        "simple": "_simple_iteration",
        "text_length": "_text_lenght_iteration",
    }

    def __init__(self, transcription_data: List[Dict[str, List[Optional[float]]|str]]):
        self.transcription_data = transcription_data
        self.index = 0
        self.data_len = len(self.transcription_data)
        self._iter_method = self._simple_iteration
        self._chars= 0

    
    def __iter__(self) -> Iterator[TranscriptionChunk]:
        return self
    
    def __next__(self) -> TranscriptionChunk:
        if self._iter_method == self._simple_iteration:
            return self._simple_iteration()
        
        return self._text_lenght_iteration(self._chars)
    
    def _simple_iteration(self)-> TranscriptionChunk:
        if self.index >= self.data_len:
            raise StopIteration
        data = self.transcription_data[self.index]
        self.index += 1
        return self._chunk_serialize(data)
    
    def _text_lenght_iteration(self, chars: int) -> TranscriptionChunk:
        """
        Метод, который будет возвращать курски длинной chars символов
        А так же таймкоды (стартовый первой части и финишный последней)
        """
        data = self.transcription_data[self.index]
        start_timestamp = data['timestamp'][0]
        end_timestamp = 0
        current_chars = 0
        text = ''

        while current_chars < chars:
            text += data['text']
            current_chars += len(data['text'])
            end_timestamp = data['timestamp'][1] if data['timestamp'][1] is not None else start_timestamp
            self.index += 1
            if self.index >= self.data_len:
                break
            data = self.transcription_data[self.index]

        instance = TranscriptionChunk(text, start_timestamp, end_timestamp)
        return instance
    
    def set_iteration_mode(self, mode: str = "simple", chars: int|None = None)-> None:
        """
        Метод для установки режима итерации
        :param mode: Режим итерации
        :param chars: Количество символов для режима text_length
        :raises ValueError: Если режим не поддерживается
        """
        if mode not in self.ITERATIONS_MODE:
            raise ValueError(f"Не поддерживается режим итерации: {mode}")
        
        mode_method = getattr(self, self.ITERATIONS_MODE[mode])

        if mode == "text_length":
            if chars is None:
                raise ValueError("Длина текста не может быть None")
            self._chars = chars

        self._iter_method = mode_method


    
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
    iterator.set_iteration_mode("text_length", 200)

    for _ in range(5):
        print(next(iterator))

if __name__ == "__main__":
    main()

