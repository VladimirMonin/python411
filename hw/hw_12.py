"""
Разбор HW 12 - Домашнее задание с 2 классами работы с Mistral API
"""


MISTRAL_API_KEY = 'rVpNURaWOqKRqEiaPJooogXfE8zJ5dgj'

# pip install mistralai
from mistralai import Mistral
import base64

model = "mistral-large-latest"

client = Mistral(api_key=MISTRAL_API_KEY)

chat_response = client.chat.complete(
    model = model,
    messages = [
        {
            "role": "user",
            "content": "Расскажи шутку про обезъянку и любовь французов к устрицам"
        },
    ]
)

print(chat_response.choices[0].message.content)


###############################################


def encode_image(image_path):
    """Переводит изображение в формат base64"""
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    except FileNotFoundError:
        print(f"Error: The file {image_path} was not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

# Путь к изображению
image_path = r"C:\Users\user\Pictures\2025-01-18_14-07-29.png"

# Получаем изображение в формате base64
base64_image = encode_image(image_path)


# Указываем модель для работы с изображениями
model = "pixtral-12b-2409"

# Создаем экземпляр клиента Mistral
client = Mistral(api_key=MISTRAL_API_KEY)

# Формируем сообщение для чата
messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "Детально опиши что изображено на этом изображении. Используй максимально подробные описания."
            },
            {
                "type": "image_url",
                "image_url": f"data:image/jpeg;base64,{base64_image}" 
            }
        ]
    }
]

# Делаем запрос к API Mistral
chat_response = client.chat.complete(
    model=model,
    messages=messages
)

# Печатаем ответ
print(chat_response.choices[0].message.content)
