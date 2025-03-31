class Inventory:
    def __init__(self, weight_limit, slots):
        self.__items = {}
        self.__weight_limit = weight_limit
        self.__current_weight = 0
        self.__slots = slots

    def __str__(self):
        return f"Inventory (capacity: {self.__weight_limit}): {self.__items}"

    def __iter__(self):
        return iter(self.__items.items())

    def __len__(self):
        return sum(self.__items.values())

    def __getitem__(self, key):
        if key in self.__items:
            return self.__items[key]
        return 0

    def __setitem__(self, key, value):
        if key in self.__items:
            # Если предмет уже есть, просто обновляем количество
            self.__items[key] += value
        else:
            # Если предмета нет, добавляем его
            if len(self.__items) < self.__slots:
                if value <= (self.__weight_limit - self.__current_weight):
                    self.__items[key] = value
                    self.__current_weight += value
                else:
                    print("Weight limit exceeded!")
            else:
                print("No available slots!")

    def __delitem__(self, key):
        if key in self.__items:
            del self.__items[key]
            # Обновляем текущий вес (предполагаем вес 1 для каждого предмета)
            self.__current_weight -= 1
        else:
            print(f"{key} not found in inventory.")

    def __contains__(self, item):
        return item in self.__items

    def __add__(self, other):
        new_inventory = Inventory(self.__weight_limit + other.__weight_limit,
                                  self.__slots + other.__slots)

        for item, quantity in self:
            new_inventory[item] = quantity

        for item, quantity in other:
            new_inventory[item] = quantity

        return new_inventory


# Пример использования
inventory1 = Inventory(weight_limit=20, slots=5)
inventory1["stone"] = 5
inventory1["wood"] = 10

print(inventory1)

inventory2 = Inventory(weight_limit=15, slots=3)
inventory2["iron"] = 3

combined_inventory = inventory1 + inventory2
print(combined_inventory)