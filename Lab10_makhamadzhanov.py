from abc import ABC, abstractmethod


class Item(ABC):
    """Базовый абстрактный класс для всех предметов."""

    @abstractmethod
    def info(self):
        pass


class Material(Item):
    """Класс для материалов, используемых в крафте."""

    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def info(self):
        return f"Материал: {self._name}"


class Weapon(Item):
    """Класс для оружия, которое можно создавать и улучшать."""

    def __init__(self, name, damage, level=1):
        self._name = name
        self._damage = damage
        self._level = level

    def get_name(self):
        return self._name

    def get_damage(self):
        return self._damage

    def get_level(self):
        return self._level

    def upgrade(self, material):
        """Улучшение оружия при помощи материала."""
        if isinstance(material, Material) and material.get_name() == "Титанит":
            self._level += 1
            self._damage += 10
            return f"{self._name} улучшен до уровня {self._level}, урон: {self._damage}"
        return "Улучшение невозможно."

    def info(self):
        return f"Оружие: {self._name}, Урон: {self._damage}, Уровень: {self._level}"


class CraftingSystem:
    """Система крафта предметов."""

    @staticmethod
    def create_item(*items):
        """Создание нового предмета из материалов."""
        names = [item.get_name() for item in items]
        if set(names) == {"Палка", "Камень"}:
            return Weapon("Каменный меч", 20)
        return "Крафт не удался."

    @staticmethod
    def break_item(item):
        """Разбор предмета на материалы."""
        if isinstance(item, Weapon) and item.get_name() == "Каменный меч":
            return [Material("Палка"), Material("Камень")]
        return "Разбор невозможен."


# Тестирование
wood = Material("Палка")
stone = Material("Камень")
titanite = Material("Титанит")

sword = CraftingSystem.create_item(wood, stone)
if isinstance(sword, Weapon):
    print(sword.info())  # Оружие: Каменный меч, Урон: 20, Уровень: 1
    print(sword.upgrade(titanite))  # Каменный меч улучшен до уровня 2, урон: 30
    print(sword.info())  # Оружие: Каменный меч, Урон: 30, Уровень: 2

# Разбор меча
materials = CraftingSystem.break_item(sword)
if isinstance(materials, list):
    for material in materials:
        print(material.info())