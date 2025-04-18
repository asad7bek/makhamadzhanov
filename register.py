from flags_register import FlagsRegister # <-- Вот эта строка!

class Register:
    def __init__(self, name, size=32):
        self.value = [0] * size
        self.name = name
        self.size = size
        self.flags = FlagsRegister()

    def load(self, value: int):
        """Загружает число в регистр (диапазон: -2**31 до 2**31-1)."""
        if not -2**31 <= value <= 2**31 - 1:
            raise ValueError("Число не в диапазоне!")

        if value >= 0:
            binary = bin(value)[2:].zfill(self.size)
            self.value = [int(bit) for bit in binary]
        else:
            positive_value = abs(value)
            binary = bin(positive_value)[2:].zfill(self.size)
            inverted = ['1' if bit == '0' else '0' for bit in binary]

            carry = 1
            temp_binary = []
            for i in range(self.size - 1, -1, -1):
                bit = int(inverted[i])
                sum_bits = bit + carry
                temp_binary.insert(0, sum_bits % 2)
                carry = sum_bits // 2

            self.value = temp_binary

    def to_int(self):
        """Переводит биты регистра в число (доп. код)."""
        if self.value[0] == 0:  # Положительное число
            binary_string = "".join(map(str, self.value))
            return int(binary_string, 2)
        else:  # Отрицательное число (доп. код)
            inverted = ['1' if bit == 0 else '0' for bit in self.value]

            borrow = 1
            temp_binary = []
            for i in range(self.size - 1, -1, -1):
                bit = int(inverted[i])
                diff = bit - borrow
                if diff < 0:
                    temp_binary.insert(0, diff + 2)
                    borrow = 1
                else:
                    temp_binary.insert(0, diff)
                    borrow = 0

            binary_string = "".join(map(str, temp_binary))
            return - (int(binary_string, 2) + 1)

    def add(self, other):
        """Складывает регистры и обновляет флаги."""
        result_bits = []
        carry = 0
        overflow = False

        for i in range(self.size - 1, -1, -1):
            bit1 = self.value[i]
            bit2 = other.value[i]
            sum_bits = bit1 + bit2 + carry

            result_bits.insert(0, sum_bits % 2)
            carry = sum_bits // 2

        operand1_sign = self.value[0]
        operand2_sign = other.value[0]
        result_sign = result_bits[0]

        if operand1_sign == operand2_sign and operand1_sign != result_sign:
            overflow = True

        result_int = self.bits_to_int(result_bits)
        if result_int > 2**31 - 1 or result_int < -2**31:
            overflow = True

        final_result_bits = result_bits
        self.value = final_result_bits

        self.flags.overflow = overflow
        self.flags.carry = carry != 0
        self.flags.update(final_result_bits)

    def sub(self, other):
        """Вычитает регистры (через сложение с доп. кодом)."""
        inverted_other = ['1' if bit == 0 else '0' for bit in other.value]

        carry = 1
        twos_complement = []
        for i in range(self.size - 1, -1, -1):
            bit = int(inverted_other[i])
            sum_bits = bit + carry
            twos_complement.insert(0, sum_bits % 2)
            carry = sum_bits // 2

        temp_register = Register("temp")
        temp_register.value = twos_complement
        self.add(temp_register)

    def bits_to_int(self, bits):
        """Преобразует список битов в число (для проверки overflow)."""
        if bits[0] == 0:
            binary_string = "".join(map(str, bits))
            return int(binary_string, 2)
        else:
            inverted = ['1' if bit == 0 else '0' for bit in bits]

            borrow = 1
            temp_binary = []
            for i in range(self.size - 1, -1, -1):
                bit = int(inverted[i])
                diff = bit - borrow
                if diff < 0:
                    temp_binary.insert(0, diff + 2)
                    borrow = 1
                else:
                    temp_binary.insert(0, diff)
                    borrow = 0

            binary_string = "".join(map(str, temp_binary))
            return - (int(binary_string, 2) + 1)

    def __str__(self):
        return f"Register {self.name}: value={self.to_int()} ({self.value}), {self.flags}"