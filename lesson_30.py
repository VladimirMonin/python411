"""
Тема: ООП Ч11. Порождающие паттерны. Практика. Урок: 30
- Строитель (Builder)
- Абстрактная фабрика (Abstract Factory)
"""


from settings import MISTRAL_API_KEY

# pip install mistralai
from mistralai import Mistral
import base64
from typing import List, Dict, Any, Optional, Union

class MistralRequestBuilder:
    """Строитель для запросов к Mistral API."""
    
    def __init__(self):
        self.api_key = MISTRAL_API_KEY
        self.client = Mistral(api_key=self.api_key)
        self.model = None
        self.messages = []
        self.inputs = []
        self.request_type = None
    
    def with_api_key(self, api_key: str):
        """Установка API ключа."""
        self.api_key = api_key
        self.client = Mistral(api_key=self.api_key)
        return self
    
    def with_model(self, model: str):
        """Установка модели."""
        self.model = model
        return self
    
    def with_text_message(self, text: str, role: str = "user"):
        """Добавление текстового сообщения."""
        self.messages.append({"role": role, "content": text})
        return self
    
    def with_image_message(self, text: str, image_path: str, role: str = "user"):
        """Добавление сообщения с изображением."""
        base64_image = self._encode_image(image_path)
        
        content = [
            {"type": "text", "text": text},
            {"type": "image_url", "image_url": f"data:image/jpeg;base64,{base64_image}"}
        ]
        
        self.messages.append({"role": role, "content": content})
        return self
    
    def with_moderation_input(self, text: str):
        """Добавление текста для модерации."""
        self.inputs.append(text)
        return self
    
    def as_text_generation(self):
        """Указание типа запроса как генерация текста."""
        self.request_type = "text_generation"
        return self
    
    def as_vision(self):
        """Указание типа запроса как модель видения."""
        self.request_type = "vision"
        return self
    
    def as_moderation(self):
        """Указание типа запроса как модерация."""
        self.request_type = "moderation"
        return self
    
    def build(self):
        """Создание объекта запроса."""
        if not self.api_key:
            raise ValueError("API key is required")
        
        if not self.model:
            raise ValueError("Model is required")
        
        if not self.request_type:
            raise ValueError("Request type is required")
        
        if self.request_type in ["text_generation", "vision"] and not self.messages:
            raise ValueError("Messages are required for text generation or vision")
        
        if self.request_type == "moderation" and not self.inputs:
            raise ValueError("Inputs are required for moderation")
        
        return MistralRequest(
            client=self.client,
            model=self.model,
            messages=self.messages,
            inputs=self.inputs,
            request_type=self.request_type
        )
    
    def _encode_image(self, image_path: str) -> str:
        """Кодирование изображения в base64."""
        try:
            with open(image_path, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode('utf-8')
        except FileNotFoundError:
            raise ValueError(f"Image file not found: {image_path}")
        except Exception as e:
            raise ValueError(f"Error encoding image: {e}")


class MistralRequest:
    """Класс для выполнения запросов к Mistral API."""
    
    def __init__(self, client, model, messages, inputs, request_type):
        self.client = client
        self.model = model
        self.messages = messages
        self.inputs = inputs
        self.request_type = request_type
    
    def execute(self):
        """Выполнение запроса."""
        if self.request_type == "text_generation":
            response = self.client.chat.complete(
                model=self.model,
                messages=self.messages
            )
            return response.choices[0].message.content
            
        elif self.request_type == "vision":
            response = self.client.chat.complete(
                model=self.model,
                messages=self.messages
            )
            return response.choices[0].message.content
            
        elif self.request_type == "moderation":
            response = self.client.classifiers.moderate(
                model=self.model,
                inputs=self.inputs
            )
            return response
        
        else:
            raise ValueError(f"Unsupported request type: {self.request_type}")



# Пример 1: Генерация текста
text_response = (MistralRequestBuilder()
    .with_model("mistral-large-latest")
    .with_text_message("Правда ли, что франзцузы едят лягушек?")
    .as_text_generation()
    .build()
    .execute())

print("Text response:", text_response)

# Пример 2: Модель видения
vision_response = (MistralRequestBuilder()
    .with_model("pixtral-12b-2409")
    .with_image_message("Детально опиши изображение", r"C:\Users\user\Pictures\photo_2024-08-05_23-15-36.jpg")
    .as_vision()
    .build()
    .execute())

print("Vision response:", vision_response)

# Пример 3: Модерация
moderation_response = (MistralRequestBuilder()
    .with_model("mistral-moderation-latest")
    .with_moderation_input("Я просто ненавижу ваш ресторан. Повара на кол. А потом сжечь!")
    .as_moderation()
    .build()
    .execute())

print("Moderation response:", moderation_response)