from utils import write_json

# Сделаем 1 словарь и список и нескольких

person = {
    "name": "John",
    "age": 30,
    "city": "New York",
}

pesons = [
    {"name": "John", "age": 30, "city": "New York"},
    {"name": "Jane", "age": 25, "city": "London"},
    {"name": "Bob", "age": 40, "city": "Paris"},
]

# Протестируем функцию. Как пишется один словарь в виде args и список в виде *args

write_json(person)
# write_json(*pesons)
