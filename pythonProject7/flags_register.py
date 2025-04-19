class FlagsRegister:
    def __init__(self):
        self.zero = False
        self.negative = False
        self.overflow = False
        self.carry = False

    def update(self, value):
        signed_result = self.to_signed_int(value)

        # Обновляем флаги
        self.zero = (signed_result == 0)
        self.negative = (value[0] == 1)  # старший бит
        self.overflow = signed_result < -2**31 or signed_result > 2**31 - 1
        self.carry = len(value) > 32  # перенос

    @staticmethod
    def to_signed_int(bits):
        if bits[0] == 1:
            val = int(''.join(map(str, bits)), 2)
            return val - (1 << len(bits))  # преобразуем в отрицательное
        return int(''.join(map(str, bits)), 2)