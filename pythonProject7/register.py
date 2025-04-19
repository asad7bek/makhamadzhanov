from flags_register import FlagsRegister


class Register:
    def __init__(self, name, size=32):
        self.name = name
        self.size = size
        self.value = [0] * size
        self.flags = FlagsRegister()

    def load(self, num):
        if num < -2 ** 31 or num > 2 ** 31 - 1:
            raise ValueError("Число вне диапазона")
        if num < 0:
            num = (1 << 32) + num  # Преобразуем в положительное двоичное представление
        self.value = [(num >> i) & 1 for i in range(self.size)][::-1]

    def to_int(self):
        integer_value = self.to_signed_int(self.value)
        print(f"Конвертация в int. Двоичное значение: {self.value}, Полученное целое значение: {integer_value}")
        return integer_value

    def add(self, other):
        result = self.to_int() + other.to_int()
        self._handle_result(result)

    def sub(self, other):
        result = self.to_int() - other.to_int()
        self._handle_result(result)

    def mul(self, other):
        result = self.to_int() * other.to_int()
        self._handle_result(result)

    def div(self, other):
        if other.to_int() == 0:
            raise ZeroDivisionError("Деление на ноль")
        result = self.to_int() // other.to_int()
        self._handle_result(result)

    def _handle_result(self, result):
        overflow_occurred = False

        print(f"Результат операции (до обработки): {result}")  # Вывод результата перед обработкой

        # Проверка переполнения
        if result < -2 ** 31:
            overflow_occurred = True
            result = -2 ** 31
        elif result > 2 ** 31 - 1:
            overflow_occurred = True
            result = 2 ** 31 - 1

        print(
            f"Результат после обработки: {result}, Переполнение: {overflow_occurred}")  # Вывод результата после обработки

        # Преобразуем результат в двоичное представление
        if result < 0:
            result += (1 << 32)

        self.value = [(result >> i) & 1 for i in range(self.size)][::-1]

        # Обновляем флаги
        self.flags.update(self.value)
        if overflow_occurred:
            self.flags.overflow = True

    @staticmethod
    def to_signed_int(bits):
        if bits[0] == 1:  # Проверка старшего бита
            val = int(''.join(map(str, bits)), 2)
            return val - (1 << len(bits))
        return int(''.join(map(str, bits)), 2)