def factorial(n): #Функция factorial вычисляет факториал числа рекурсивно.
    if n < 0:
        raise ValueError("Факториал не определен для отрицательных чисел")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

#Зад2

from functools import lru_cache

@lru_cache(maxsize=None)
def cached_factorial(n):
    if n < 0:
        raise ValueError("Факториал не определен для отрицательных чисел")
    if n == 0 or n == 1:
        return 1
    return n * cached_factorial(n - 1)

#Зад 3

def cache(func):   #@cache реализует аналогичное кэширование, но без использования встроенных функций.
    cached_results = {}

    def wrapper(n):
        if n in cached_results:
            return cached_results[n]
        result = func(n)
        cached_results[n] = result
        return result

    return wrapper

@cache
def custom_cached_factorial(n):
    if n < 0:
        raise ValueError("Факториал не определен для отрицательных чисел")
    if n == 0 or n == 1:
        return 1
    return n * custom_cached_factorial(n - 1)

#Зад 4

import time
import logging

logging.basicConfig(level=logging.INFO)

def log(func): # @log логирует информацию о вызове функции, включая имя функции, аргументы, результат и время выполнения. Он также обрабатывает ошибки и логирует их.
    def wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            result = func(*args, **kwargs)
            end_time = time.time()
            logging.info(f"Вызов функции: {func.__name__}, Аргументы: {args}, Результат: {result}, Время выполнения: {end_time - start_time:.4f} секунд")
            return result
        except Exception as e:
            end_time = time.time()
            logging.error(f"Ошибка в функции: {func.__name__}, Аргументы: {args}, Ошибка: {e}, Время выполнения: {end_time - start_time:.4f} секунд")
            raise e

    return wrapper

@log
def logged_factorial(n):
    if n < 0:
        raise ValueError("Факториал не определен для отрицательных чисел")
    if n == 0 or n == 1:
        return 1
    return n * logged_factorial(n - 1)

#Зад 5

class Player:
    def __init__(self, name):
        self.name = name
        self._health = 100
        self._level = 1
        self._experience = 0

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if value < 0:
            self._health = 0
        else:
            self._health = value

    @health.deleter
    def health(self):
        del self._health

    @property
    def level(self):
        return self._level

    @property
    def experience(self):
        return self._experience

    def gain_experience(self, amount):
        self._experience += amount
        while self._experience >= (self._level * 100):  # Пример условия повышения уровня.
            self._experience -= (self._level * 100)
            self._level += 1


# Пример класса Player.
player = Player("Hero")
print(player.health)  # Выводит: 100
player.health -= 20  # Уменьшаем здоровье на 20.
print(player.health)  # Выводит: 80
player.gain_experience(250)  # Получаем опыт.
print(player.level)  # Выводит: уровень игрока после повышения.