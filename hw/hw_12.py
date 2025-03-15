"""
Разбор HW 12 - Домашнее задание с 2 классами работы с Mistral API
"""

MISTRAL_API_KEY = "rVpNURaWOqKRqEiaPJooogXfE8zJ5dgj"

# pip install mistralai
from typing import Any
from mistralai import Mistral
import base64


class TextRequest:
    """
    Класс отвечает за отправку текстовых запросов к API Mistral.
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


class ImageRequest:
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


class ChatFacade:
    """ "
    Фасад предоставляет единый интерфейс для пользователя и управляет взаимодействием с `TextRequest` и `ImageRequest`.
    """

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.models = {"text": ["mistral-large-latest"], "image": ["pixtral-12b-2409"]}

        self.request: TextRequest | ImageRequest = self.__set_request()
        self.model: str = self.__set_model()
        self.history = []

    def __set_request(self) -> TextRequest | ImageRequest:
        """
        Возвращает объект TextRequest или ImageRequest в зависимости от выбора пользователя.
        """
        mode = input("Выберите режим запроса (1 - текстовый, 2 - с изображением): ")

        if mode == "1":
            return TextRequest(api_key=self.api_key)
        elif mode == "2":
            return ImageRequest(api_key=self.api_key)
        else:
            raise ValueError("Неверный режим запроса")

    def __set_model(self) -> str:
        """
        Возвращает выбранную модель для запроса.
        """
        model = input(
            f"Выберите модель из списка {self.models['text' if isinstance(self.request, TextRequest) else 'image']}: "
        )
        if (
            model
            not in self.models[
                "text" if isinstance(self.request, TextRequest) else "image"
            ]
        ):
            raise ValueError("Неверная модель")
        return model

    def format_message(self, message: dict) -> str:
        """
        Форматирует сообщение для красивого вывода
        """
        emoji = "👤" if message["role"] == "user" else "🤖"
        return f"{emoji} {message['content']}\n"

    def aks_question(self, text: str, image_path: str = None) -> dict:
        """
        Основной метод для отправки запроса.
        """
        # Создаем сообщение пользователя
        user_message = {"role": "user", "content": text}

        # Получаем текущую историю в нужном формате
        current_history = [msg for _, msg in self.history]

        if image_path:
            response = self.request.send(
                text=text,
                image_path=image_path,
                history=current_history,
                model=self.model,
            )
        else:
            response = self.request.send(
                text=text, history=current_history, model=self.model
            )

        # Обновляем историю
        self.history.append((text, user_message))
        self.history.append((text, response))
        return response

    def __call__(self):
        """
        Запуск фасада.
        """
        print("🤖 Здравствуйте! Я готов помочь вам. Для выхода введите 'exit'")

        while True:
            text = input("\n👤 Введите текст запроса: ")
            if text.lower() == "exit":
                print("🤖 До свидания!")
                break

            image_path = None
            if isinstance(self.request, ImageRequest):
                image_path = input("👤 Введите путь к изображению: ")

            response = self.aks_question(
                text=text, image_path=image_path if image_path else None
            )

            # Красиво выводим последний ответ
            print(self.format_message(response))


# Запуск фасада
chat_facade = ChatFacade(api_key=MISTRAL_API_KEY)
chat_facade()
