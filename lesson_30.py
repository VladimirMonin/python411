"""
Тема: ООП Ч11. Порождающие паттерны. Практика. Урок: 30
- Строитель (Builder)
- Абстрактная фабрика (Abstract Factory)
"""

"""
Полная версия.
Абстрактная фабрика (Abstract Factory)

Структура классов
- АБСТРАКТНЫЕ ПРОДУКТЫ
  - AbstractImageAnalyzer
  - AbstractTextGenerator
  - AbstractTextFormatter
  - AbstractAudioTrascriber

- АБСТРАКТНАЯ ФАБРИКА
  - AbstractProductFactory

- Реальные продукты
  - ClaudeImageAnalyzer
  - ClaudeTextGenerator


  - OpenAiAudioTranscriber
  - OpenAiImageAnalyzer
  - OpenAiTextGenerator

  - MistralImageAnalyzer
  - MistralTextGenerator

"""

from typing import List, Optional, Self
from abc import ABC, abstractmethod


# Сделаеем только 2 абстратных продукта. Анализатор картинок и генератор текста. и Реальные. OpenAI и Mistral

# АБСТРАКТНЫЕ ПРОДУКТЫ

class AbstractImageAnalyzer(ABC):
    @abstractmethod
    def analyze_image(self, image_path: str) -> str:
        pass
        # print(f'Анализатор картинок {self.__class__.__name__}: Анализирую картинку {image_path}')

class AbstractTextGenerator(ABC):
    @abstractmethod
    def generate_text(self, prompt: str) -> str:
        pass
        # print(f'Генератор текста {self.__class__.__name__}: Генерирую текст по запросу {prompt}')

# РЕАЛЬНЫЕ ПРОДУКТЫ

class OpenAiImageAnalyzer(AbstractImageAnalyzer):
    def analyze_image(self, image_path: str) -> str:
        print(f'OpenAI: Анализирую картинку {image_path}')
        return f'Результат анализа картинки: {image_path}'

class OpenAiTextGenerator(AbstractTextGenerator):
    def generate_text(self, prompt: str) -> str:
        print(f'OpenAI: Генерирую текст по запросу {prompt}')
        return f'Результат генерации текста: {prompt}'

class MistralImageAnalyzer(AbstractImageAnalyzer):
    def analyze_image(self, image_path: str) -> str:
        print(f'Mistral: Анализирую картинку {image_path}')
        return f'Результат анализа картинки: {image_path}'

class MistralTextGenerator(AbstractTextGenerator):
    def generate_text(self, prompt: str) -> str:
        print(f'Mistral: Генерирую текст по запросу {prompt}')
        return f'Результат генерации текста: {prompt}'

# АБСТРАКТНАЯ ФАБРИКА

class AbstractProductFactory(ABC):
    @abstractmethod
    def create_image_analyzer(self) -> AbstractImageAnalyzer:
        pass

    @abstractmethod
    def create_text_generator(self) -> AbstractTextGenerator:
        pass


# РЕАЛЬНЫЕ ПРОДУКТЫ

# Фабрика OpenAI
class OpenAiFactory(AbstractProductFactory):
    def create_image_analyzer(self) -> AbstractImageAnalyzer:
        return OpenAiImageAnalyzer()
    
    def create_text_generator(self) -> AbstractTextGenerator:
        return OpenAiTextGenerator()
    
# Фабрика Mistral
class MistralFactory(AbstractProductFactory):
    def create_image_analyzer(self) -> AbstractImageAnalyzer:
        return MistralImageAnalyzer()
    
    def create_text_generator(self) -> AbstractTextGenerator:
        return MistralTextGenerator()
    

# Сделаем анализ картинок через Open AI
if __name__ == '__main__':
    openai_factory = OpenAiFactory()
    openai_image_analyzer = openai_factory.create_image_analyzer()
    
    image_path = input('Введите путь до картинки:')
    openai_image_analyzer.analyze_image(image_path)
    
