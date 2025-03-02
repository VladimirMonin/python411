"""
Тема: ООП Ч11. Порождающие паттерны. Практика. Урок: 30
- Строитель (Builder)
- Абстрактная фабрика (Abstract Factory)
"""


from settings import MISTRAL_API_KEY

# pip install mistralai
from mistralai import Mistral
import base64

# model = "mistral-large-latest"

# client = Mistral(api_key=MISTRAL_API_KEY)

# chat_response = client.chat.complete(
#     model = model,
#     messages = [
#         {
#             "role": "user",
#             "content": "Расскажи шутку про обезъянку и французский Mistral API"
#         },
#     ]
# )

# print(chat_response.choices[0].message.content)


###############################################


def encode_image(image_path):
    """Encode the image to base64."""
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    except FileNotFoundError:
        print(f"Error: The file {image_path} was not found.")
        return None
    except Exception as e:  # Added general exception handling
        print(f"Error: {e}")
        return None

# Path to your image
image_path = r"C:\Users\user\Pictures\2025-01-18_14-07-29.png"

# Getting the base64 string
base64_image = encode_image(image_path)


# Specify model
model = "pixtral-12b-2409"

# Initialize the Mistral client
client = Mistral(api_key=MISTRAL_API_KEY)

# Define the messages for the chat
messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "Детально опиши что изображено на этом изображении. Используй максимально подробные детали."
            },
            {
                "type": "image_url",
                "image_url": f"data:image/jpeg;base64,{base64_image}" 
            }
        ]
    }
]

# Get the chat response
chat_response = client.chat.complete(
    model=model,
    messages=messages
)

# Print the content of the response
print(chat_response.choices[0].message.content)

"""
Изображение представляет собой скриншот интерфейса музыкального плеера. Интерфейс разделен на две основные секции. Слева находится панель управления, а справа — список треков.

Панель управления состоит из шести различных кнопок, каждая из которых выполняет определенную функцию. Сверху вниз эти кнопки включают кнопку воспроизведения, кнопку приостановки, кнопку перемотки вперед, кнопку перемотки назад, кнопку повтора и кнопку выхода.

Справа от панели управления находится список треков. В списке отображаются три трека, каждый из которых имеет название и продолжительность. Название треков на русском языке, а продолжительность указана в секундах.

Фон интерфейса черный, что создает резкий контраст с белым текстом и красными кнопками. Общая компоновка интерфейса указывает на удобный для пользователя дизайн, с четко видимыми кнопками управления и списком треков.
"""