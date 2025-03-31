class Vehicle:
    def __init__(self, max_speed, fuel_type):
        self.max_speed = max_speed
        self.fuel_type = fuel_type

    def start_engine(self):
        print("Engine started.")

class CargoTransport(Vehicle):
    def __init__(self, max_speed, fuel_type, cargo_capacity):
        super().__init__(max_speed, fuel_type)  # Вызов конструктора родительского класса
        self.cargo_capacity = cargo_capacity

    def load_cargo(self, weight):
        if weight <= self.cargo_capacity:
            print(f"Loaded {weight} kg of cargo.")
        else:
            print("Cargo exceeds capacity!")

class PassengerTransport(Vehicle):
    def __init__(self, max_speed, fuel_type, passenger_capacity):
        super().__init__(max_speed, fuel_type)
        self.passenger_capacity = passenger_capacity

    def board_passengers(self, count):
        if count <= self.passenger_capacity:
            print(f"Boarded {count} passengers.")
        else:
            print("Too many passengers!")

# Пример использования
cargo_transport = CargoTransport(max_speed=120, fuel_type='diesel', cargo_capacity=1000)
cargo_transport.start_engine()
cargo_transport.load_cargo(800)

passenger_transport = PassengerTransport(max_speed=150, fuel_type='petrol', passenger_capacity=5)
passenger_transport.start_engine()
passenger_transport.board_passengers(3)