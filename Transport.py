from abc import ABC, abstractmethod


# интерфейс предметной области
class Transport(ABC):

    def __init__(self):
        self.name = input("Enter name: ")
        self.price = float(input("Enter price of transport: "))

    @abstractmethod  # абстрактные методы для реализации дочерних класс
    def info(self):
        pass

    @abstractmethod
    def to_json(self, filename):
        pass

    @abstractmethod
    def to_xml(self, filename):
        pass
