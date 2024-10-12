# базовый класс
class Transport:

    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

    def __getitem__(self, item):
        pass

    def make_dict(self):
        return {
            "name": self.name,
            "price": self.price,
        }


class Car(Transport):

    def __init__(self, name: str, price: int, movement_type: str):
        super().__init__(name, price)
        self.movement_type = movement_type

    def __getitem__(self, item):
        return getattr(self, item)

    def make_dict(self):
        car_dict = super().make_dict()
        car_dict["movementType"] = self.movement_type
        return car_dict


class Truck(Transport):

    def __init__(self, name: str, price: int, load_capacity: int):
        super().__init__(name, price)
        self.load_capacity = load_capacity

    def __getitem__(self, item):
        return getattr(self, item)

    def make_dict(self):
        truck_dict = super().make_dict()
        truck_dict["load_capacity"] = self.load_capacity
        return truck_dict


class Bus(Transport):

    def __init__(self, name: str, price: int, max_passengers: int):
        super().__init__(name, price)
        self.max_passengers = max_passengers

    def __getitem__(self, item):
        return getattr(self, item)

    def make_dict(self):
        bus_dict = super().make_dict()
        bus_dict["max_passengers"] = self.max_passengers
        return bus_dict


class Plane(Transport):

    def __init__(self, name: str, price: int, speed: int):
        super().__init__(name, price)
        self.speed = speed

    def __getitem__(self, item):
        return getattr(self, item)

    def make_dict(self):
        plane_dict = super().make_dict()
        plane_dict["speed"] = self.speed
        return plane_dict


class Helicopter(Transport):

    def __init__(self, name: str, price: int, rpm: int):
        super().__init__(name, price)
        self.rpm = rpm

    def __getitem__(self, item):
        return getattr(self, item)

    def make_dict(self):
        helicopter_dict = super().make_dict()
        helicopter_dict["rpm"] = self.rpm
        return helicopter_dict


class Submarine(Transport):

    def __init__(self, name: str, price: int, diving_depth: int):
        super().__init__(name, price)
        self.diving_depth = diving_depth

    def __getitem__(self, item):
        return getattr(self, item)

    def make_dict(self):
        submarine_dict = super().make_dict()
        submarine_dict["diving_depth"] = self.diving_depth
        return submarine_dict
