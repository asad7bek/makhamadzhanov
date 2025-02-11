import random

class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def get_name(self):
        return self.name

    def get_name(self):
        return self.name

    def __str__(self):
        return f"{self.name} (ценность: {self.value})"

class cheast:
    def __init__(self, description):
        self. contents = []
        self.__is_open = false
        self.__description = description #описание для сундука
    def add_item(self, item):
        """Добавлять предмет в сундук."""
        self._contents.append (Item)


    def get_item(self):#англисча йозиш
     """Получает случайный предмет из сундука. И возврашает None, если пуст или закрыт."""
     if self.__is_open and self.__contents:
          случайный_индекс = random.randint(0, len(self.__contents) - 1)
          предмет = self.__contents.pop(случайный_индекс)
          return предмет
     else:
          return None

    def open_cheast (self):
        """Открывает сундук."""
        if not self.__is_open:
            self.__is_open = True
            print("Сундук уже открыт! {self.description}")
            return True
        else:
         print("Сундук уже открыт.")
         return False

    def close_cheast(self):
        """Закрывет сундук."""
        self.__is_open = False
        print("Сундук закрыт.")
    def shov_content(self):
        """Отображает содержимое сундука."""
        if self.__is_open:
            if not self.contents:
                print("Сундук пуск.")
            else:
                print("Содержимое сундука:")
                for item in self.contents:
                    print(f"-{item}")
        else:
            print("Сундука закрыт. Откройте его, чтобы увидеть содержимое. ")
    def is_open(self):
        return self.__is_open
    def get_description(self):
        return self.__description
