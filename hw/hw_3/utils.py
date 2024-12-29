import json

# Функция для записи данных в JSON файл
def write_json(*data:dict, filename="data.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
