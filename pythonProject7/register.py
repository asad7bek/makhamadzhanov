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
        return self.to_signed_int(self.value)

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

        # Проверка переполнения
        if result < -2 ** 31:
            overflow_occurred = True
            result = -2 ** 31
        elif result > 2 ** 31 - 1:
            overflow_occurred = True
            result = 2 ** 31 - 1

        # Преобразуем результат в двоичное представление
        if result < 0:
            result += (1 << 32)

        self.value = [(result >> i) & 1 for i in range(self.size)][::-1]

        # Обновляем флаги
        self.flags.update(self.value)
        # Устанавливаем флаг переполнения, если это произошло
        if overflow_occurred:
            self.flags.overflow = True

    @staticmethod
    def to_signed_int(bits):
        if bits[0] == 1:  # Проверка старшего бита
            val = int(''.join(map(str, bits)), 2)
            return val - (1 << len(bits))
        return int(''.join(map(str, bits)), 2)