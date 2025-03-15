"""
Разбор HW 12 - Домашнее задание с 2 классами работы с Mistral API
"""


MISTRAL_API_KEY = 'rVpNURaWOqKRqEiaPJooogXfE8zJ5dgj'

# pip install mistralai
from unittest import result
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
    

"""
2. **ImageRequest**  
   Класс предназначен для отправки запросов, включающих изображение.

   Методы:
   - `__init__(self, api_key: str) -> None`  
     Инициализация с API-ключом.
   - `send(self, text: str, image_path: str, model: str) -> dict`  
     Отправка мультимодального запроса, объединяющего текст и изображение.  
     Задачи метода:
     - Загрузка изображения по указанному пути.
     - Преобразование изображения в формат Base64.
     - Формирование корректного JSON с текстовыми данными и данными изображения.
     - Отправка запроса к API и обработка ответа.
"""