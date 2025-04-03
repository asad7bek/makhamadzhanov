from abc import ABC, abstractmethod

class GameItem(ABC):
    def __init__(self, item_name, weight, rarity):
        self.item_name = item_name
        self.weight = weight
        self.rarity = rarity

    def use(self):
        pass

    def get_description(self):
        return f'"{self.item_name}" (Редкость: {self.rarity}, Вес: {self.weight})'

class HealthPotion(GameItem):
    def __init__(self, item_name, weight, rarity, healing_amount=50):
        super().__init__(item_name, weight, rarity)
        self.healing_amount = healing_amount

    def use(self):
        print(f"Зелье здоровья {self.get_description()} использовано: + {self.healing_amount} HP")

class ManaCrystal(GameItem):
    def __init__(self, item_name, weight, rarity, mana_restore_amount=30):
        super().__init__(item_name, weight, rarity)
        self.mana_restore_amount = mana_restore_amount

    def use(self):
        print(f"Кристалл маны {self.get_description()} использован: +{self.mana_restore_amount} MP")

if __name__ == "__main__":
    # Создаем экземпляры предметов
    health_potion = HealthPotion(item_name="Большой флакон", rarity="Обычное", weight=0.5)
    mana_crystal = ManaCrystal(item_name="Синий осколок", rarity="Редкое", weight=0.3)

    # Используем предметы
    health_potion.use()
    mana_crystal.use()
