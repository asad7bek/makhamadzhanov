import random

class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

    def __str__(self):
        return f"{self.name} (Ценность: {self.value})"


class Cheast:
    def __init__(self, description: object) -> object:
        self.__contents = []
        self.__is_open = False
        self.__description = description

    def get_item(self, item):
        """Добавляет предмет в сундук."""
        self.__contents.append(item)

    def get_item(self):
        """Получает случайный предмет из сундука. Возвращает None, если пуст или закрыт."""
        if self.__is_open and self.__contents:
            random_index = random.randint(0, len(self.__contents) - 1)
            Item = self.__contents.pop(random_index)
            return Item
        else:
            return None

    def open_cheast(self):
        """Открывает сундук."""
        if not self.__is_open:
            self.__is_open = True
            print(f"Сундук открыт! {self.__description}")
            return True
        else:
            print("Сундук уже открыт.")
            return False

    def close_cheast(self):
        """Закрывает сундук."""
        self.__is_open = False
        print("Сундук закрыт.")

    def show_content(self):
        """Отображает содержимое сундука."""
        if self.__is_open:
            if not self.__contents:
                print("Сундук пуст.")
            else:
                print("Содержимое сундука:")
                for item in self.__contents:
                    print(f"- {item}")

    def add(self, param: object) -> object:
        pass
