class FlagsRegister:
    def __init__(self):
        self.zero = False
        self.negative = False
        self.overflow = False
        self.carry = False

    def update(self, value: list):
        """Обновляет флаги после операции."""
        self.zero = all(bit == 0 for bit in value)
        self.negative = value[0] == 1  # Старший бит = 1 -> отрицательное число

    def __str__(self):
        return f"Flags: Z={self.zero}, N={self.negative}, O={self.overflow}, C={self.carry}"
