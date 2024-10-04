# базовый класс
class Transport:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def make_dict(self):
        return {
            "name": self.name,
            "price": self.price,
        }


class Car(Transport):

    def __init__(self, name, price, movementType):
        super().__init__(name, price)
        self.movementType = movementType

    def make_dict(self):
        car_dict = super().make_dict()
        car_dict["movementType"] = self.movementType
        return car_dict


class Truck(Transport):

    def __init__(self, name, price, loadCapacity):
        super().__init__(name, price)
        self.loadCapacity = loadCapacity

    def make_dict(self):
        truck_dict = super().make_dict()
        truck_dict["loadCapacity"] = self.loadCapacity
        return truck_dict


class Bus(Transport):

    def __init__(self, name, price, maxPassengers):
        super().__init__(name, price)
        self.maxPassengers = maxPassengers

    def make_dict(self):
        truck_dict = super().make_dict()
        truck_dict["maxPassengers"] = self.maxPassengers
        return truck_dict


class Plane(Transport):

    def __init__(self, name, price, speed):
        super().__init__(name, price)
        self.speed = speed

    def make_dict(self):
        truck_dict = super().make_dict()
        truck_dict["speed"] = self.speed
        return truck_dict


class Helicopter(Transport):

    def __init__(self, name, price, rpm):
        super().__init__(name, price)
        self.rpm = rpm

    def make_dict(self):
        truck_dict = super().make_dict()
        truck_dict["rpm"] = self.rpm
        return truck_dict


class Submarine(Transport):

    def __init__(self, name, price, divingDepth):
        super().__init__(name, price)
        self.divingDepth = divingDepth

    def make_dict(self):
        truck_dict = super().make_dict()
        truck_dict["divingDepth"] = self.divingDepth
        return truck_dict
