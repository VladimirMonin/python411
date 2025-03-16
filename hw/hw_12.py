"""
Разбор HW 12 - Домашнее задание с 2 классами работы с Mistral API
"""

MISTRAL_API_KEY = "rVpNURaWOqKRqEiaPJooogXfE8zJ5dgj"

# pip install mistralai
from typing import Any, List, Dict, Tuple, Optional, Union
from mistralai import Mistral
import base64
from abc import ABC, abstractmethod


class MistralRequestStrategy(ABC):
    """
    Абстрактный класс стратегии для работы с API Mistral.
    """

    @abstractmethod
    def send(self, *args: Any, **kwargs: Any) -> dict:
        pass


class TextRequest(MistralRequestStrategy):
    """
    Класс стратегия отвечает за отправку текстовых запросов к API Mistral.
    """

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.client = Mistral(api_key=self.api_key)

    def send(
        self, text: str, history: list = None, model: str = "mistral-large-latest"
    ) -> dict:
        """
        Основной метод отправки текстового запроса к API Mistral.
        """
        messages = []
        if history:
            messages.extend(
                [{"role": msg["role"], "content": msg["content"]} for msg in history]
            )

        messages.append({"role": "user", "content": text})

        response = self.client.chat.complete(model=model, messages=messages)

        result = {"role": "assistant", "content": response.choices[0].message.content}
        return result


class ImageRequest(MistralRequestStrategy):
    """
    Класс отвечает за отправку запросов, включающих изображение.
    """

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.client = Mistral(api_key=self.api_key)

    def __encode_image(self, image_path: str) -> str:
        """Переводит изображение в формат base64"""
        try:
            with open(image_path, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode("utf-8")
        except FileNotFoundError:
            print(f"Ошибка: Файл {image_path} не найден")
            return ""
        except Exception as e:
            print(f"Ошибка: {e}")
            return ""

    def send(
        self,
        text: str,
        image_path: str,
        history: list = None,
        model: str = "pixtral-12b-2409",
    ) -> dict:
        """
        Основной метод отправки мультимодального запроса, объединяющего текст и изображение.
        """
        base64_image = self.__encode_image(image_path)

        messages = []
        if history:
            messages.extend(
                [{"role": msg["role"], "content": msg["content"]} for msg in history]
            )

        messages.append(
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": text},
                    {
                        "type": "image_url",
                        "image_url": f"data:image/jpeg;base64,{base64_image}",
                    },
                ],
            }
        )

        chat_response = self.client.chat.complete(model=model, messages=messages)

        result = {
            "role": "assistant",
            "content": chat_response.choices[0].message.content,
        }
        return result


class MistralRequestContext:
    """
    Контекст для работы со стратегиями запросов к Mistral API.
    Реализует классическую версию паттерна Стратегия.
    """
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.models = {"text": ["mistral-large-latest"], "image": ["pixtral-12b-2409"]}
        self.strategy: MistralRequestStrategy = None
        self.model: str = None
        self.history: List[Tuple[str, Dict]] = []
        
    def set_strategy(self, strategy_type: str) -> None:
        """
        Устанавливает стратегию в зависимости от типа запроса.
        
        Args:
            strategy_type: "text" или "image"
        """
        if strategy_type == "text":
            self.strategy = TextRequest(api_key=self.api_key)
        elif strategy_type == "image":
            self.strategy = ImageRequest(api_key=self.api_key)
        else:
            raise ValueError(f"Неизвестный тип стратегии: {strategy_type}")
    
    def set_model(self, model: str) -> None:
        """
        Устанавливает модель для текущей стратегии.
        
        Args:
            model: название модели Mistral
        """
        strategy_type = "text" if isinstance(self.strategy, TextRequest) else "image"
        if model not in self.models[strategy_type]:
            raise ValueError(f"Модель {model} не доступна для стратегии {strategy_type}")
        self.model = model
    
    def get_available_models(self) -> List[str]:
        """
        Возвращает список доступных моделей для текущей стратегии.
        """
        if not self.strategy:
            return []
        strategy_type = "text" if isinstance(self.strategy, TextRequest) else "image"
        return self.models[strategy_type]
    
    def execute_request(self, text: str, image_path: Optional[str] = None) -> Dict:
        """
        Выполняет запрос с использованием текущей стратегии.
        
        Args:
            text: текст запроса
            image_path: путь к изображению (только для ImageRequest)
            
        Returns:
            Словарь с ответом от API
        """
        if not self.strategy:
            raise ValueError("Стратегия не установлена")
            
        # Создаем сообщение пользователя
        user_message = {"role": "user", "content": text}
        
        # Получаем текущую историю в нужном формате
        current_history = [msg for _, msg in self.history]
        
        # Отправляем запрос с использованием соответствующей стратегии
        if isinstance(self.strategy, ImageRequest) and image_path:
            response = self.strategy.send(
                text=text,
                image_path=image_path,
                history=current_history,
                model=self.model
            )
        elif isinstance(self.strategy, TextRequest):
            response = self.strategy.send(
                text=text,
                history=current_history,
                model=self.model
            )
        else:
            raise ValueError("Несоответствие стратегии и параметров запроса")
            
        # Обновляем историю
        self.history.append((text, user_message))
        self.history.append((text, response))
        
        return response
    
    def clear_history(self) -> None:
        """Очищает историю сообщений"""
        self.history = []


class ChatFacade:
    """
    Фасад предоставляет единый интерфейс для пользователя и координирует
    работу с контекстом запросов Mistral.
    """

    def __init__(self, api_key: str) -> None:
        self.context = MistralRequestContext(api_key=api_key)
        
    def format_message(self, message: dict) -> str:
        """
        Форматирует сообщение для красивого вывода
        """
        emoji = "👤" if message["role"] == "user" else "🤖"
        return f"{emoji} {message['content']}\n"

    def __call__(self):
        """
        Запуск фасада.
        """
        print("🤖 Здравствуйте! Я готов помочь вам. Для выхода введите 'exit'")
        
        # Настраиваем стратегию и модель перед началом беседы
        self._setup_strategy_and_model()

        while True:
            text = input("\n👤 Введите текст запроса: ")
            if text.lower() == "exit":
                print("🤖 До свидания!")
                break
                
            if text.lower() == "change":
                self._setup_strategy_and_model()
                continue

            image_path = None
            if isinstance(self.context.strategy, ImageRequest):
                image_path = input("👤 Введите путь к изображению: ")

            try:
                response = self.context.execute_request(
                    text=text, 
                    image_path=image_path
                )
                # Красиво выводим ответ
                print(self.format_message(response))
            except Exception as e:
                print(f"🚫 Произошла ошибка: {e}")
    
    def _setup_strategy_and_model(self):
        """Настройка стратегии и модели через взаимодействие с пользователем"""
        mode = input("Выберите режим запроса (1 - текстовый, 2 - с изображением): ")
        
        strategy_type = "text" if mode == "1" else "image" if mode == "2" else None
        if not strategy_type:
            print("⚠️ Неверный выбор. Установлен текстовый режим по умолчанию.")
            strategy_type = "text"
            
        # Устанавливаем стратегию
        self.context.set_strategy(strategy_type)
        
        # Получаем и показываем доступные модели
        available_models = self.context.get_available_models()
        model_prompt = f"Выберите модель из списка {available_models}: "
        model = input(model_prompt)
        
        try:
            self.context.set_model(model)
        except ValueError:
            default_model = available_models[0]
            print(f"⚠️ Выбрана модель по умолчанию: {default_model}")
            self.context.set_model(default_model)


# Запуск фасада
chat_facade = ChatFacade(api_key=MISTRAL_API_KEY)
chat_facade()