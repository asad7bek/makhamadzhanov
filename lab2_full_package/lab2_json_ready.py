# ЗАДАЧА 1
import json

data = {
    "people": [
        {"name": "Иван", "city": "Москва", "age": 17},
        {"name": "Миша", "city": "Санкт-Петербург", "age": 18},
        {"name": "Егор", "city": "Москва", "age": 16}
    ]
}

with open("people.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

# Открытие и вывод
with open("people.json", "r", encoding="utf-8") as f:
    people = json.load(f)["people"]

names = [p["name"] for p in people if p["city"] == "Москва"]
average_age = sum(p["age"] for p in people if p["city"] == "Москва") / len(names)

print("Имена из Москвы:", names)
print("Средний возраст:", average_age)


# ЗАДАЧА 2
my_info = {
    "Фамилия": "Сандул",
    "Имя": "Миша",
    "Отчество": "Анатолевич",
    "Телефон": "89991234567",
    "Год рождения": 2007,
    "Город рождения": "Село уголовое",
    "Место учебы": "БГПУ"
}

with open("my_info.json", "w", encoding="utf-8") as f:
    json.dump(my_info, f, ensure_ascii=False, indent=4)


# ЗАДАЧА 3
with open("my_info.json", "r", encoding="utf-8") as f:
    data = json.load(f)

key = input("Введите ключ, который хотите изменить: ")
if key in data:
    value = input("Введите новое значение: ")
    data[key] = value

    with open("my_info.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
else:
    print("Ключ не найден!")


# ЗАДАЧА 4
with open("geocoder.json", "r", encoding="utf-8") as f:
    data = json.load(f)

country = data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["metaDataProperty"]["GeocoderMetaData"]["AddressDetails"]["Country"]["CountryName"]
coordinates = data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"].split()

longitude = coordinates[0]
latitude = coordinates[1]

print("Страна:", country)
print("Долгота:", longitude)
print("Широта:", latitude)


# ЗАДАЧА 5
with open("geocoder.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Замена данных на БГПУ
bgpu_info = {
    "CountryName": "Россия",
    "Point": {"pos": "55.9549 54.7388"}
}

data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["metaDataProperty"]["GeocoderMetaData"]["AddressDetails"]["Country"]["CountryName"] = bgpu_info["CountryName"]
data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"] = bgpu_info["Point"]["pos"]

with open("geocoder.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
