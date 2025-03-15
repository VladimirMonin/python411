"""
Разбор HW 12 - Домашнее задание с 2 классами работы с Mistral API
"""


MISTRAL_API_KEY = 'rVpNURaWOqKRqEiaPJooogXfE8zJ5dgj'

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

    def send(self, text: str, model: str = "mistral-large-latest") -> dict:
        """
        Основной метод отправки текстового запроса к API Mistral.
        """
        response = self.client.chat.complete(
            model = model,
            messages = [
                {
                    "role": "user",
                    "content": text
                }
            ]
        )
        # Формируем ответ в виде словаря для работы с историей чата
        result = {
            "role": "assistant",
            "content": response.choices[0].message.content
        }

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
                return base64.b64encode(image_file.read()).decode('utf-8')
        except FileNotFoundError:
            print(f"Ошибка: Файл {image_path} не найден")
            return ''
        except Exception as e:
            print(f"Ошибка: {e}")
            return ''

    
    
    def send(self, text: str, image_path: str, model: str = "pixtral-12b-2409") -> dict:
        """
        Основной метод отправки мультимодального запроса, объединяющего текст и изображение.
        """
        # Получаем изображение в формате base64
        base64_image = self.__encode_image(image_path)


        # Формируем сообщение для чата
        messages = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": text
                    },
                    {
                        "type": "image_url",
                        "image_url": f"data:image/jpeg;base64,{base64_image}" 
                    }
                ]
            }
        ]
        
        chat_response = self.client.chat.complete(
            model=model,
            messages=messages
        )

        # Формируем ответ в виде словаря для работы с историей чата
        result = {
            "role": "assistant",
            "content": chat_response.choices[0].message.content
        }

        return result
    

class ChatFacade:
    """"
    Фасад предоставляет единый интерфейс для пользователя и управляет взаимодействием с `TextRequest` и `ImageRequest`.
    """
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.models = {
            "text": ["mistral-large-latest"],
            "image": ["pixtral-12b-2409"]
        }

        self.request: TextRequest|ImageRequest = self.__set_request()
        self.model: str = self.__set_model()
        self.history = []
        


    def __set_request(self) -> TextRequest|ImageRequest:
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
        model = input(f"Выберите модель из списка {self.models['text' if isinstance(self.request, TextRequest) else 'image']}: ")
        if model not in self.models['text' if isinstance(self.request, TextRequest) else 'image']:
            raise ValueError("Неверная модель")
        return model
    

    def aks_question(self, text: str, image_path: str = None) -> dict:
        """
        Основной метод для отправки запроса.
        """
        if image_path:
            response = self.request.send(text=text, image_path=image_path, model=self.model)
        else:
            response = self.request.send(text=text, model=self.model)
        
        self.history.append((text, response))
        return response
    

    def get_history(self) -> list[tuple[str, dict]]:
        """
        Возвращает историю запросов и ответов.
        """
        return self.history
    
    def __call__(self):
        """
        Запуск фасада.
        """
        while True:
            text = input("Введите текст запроса: ")
            image_path = None
            
            if isinstance(self.request, ImageRequest):
                image_path = input("Введите путь к изображению: ")
            response = self.aks_question(text=text, image_path= image_path if image_path else None)
            print(response)
            print(self.history)


# Запуск фасада
chat_facade = ChatFacade(api_key=MISTRAL_API_KEY)
chat_facade()