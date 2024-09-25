from abc import ABC, abstractmethod
import xml.etree.ElementTree as ET


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


class Car(Transport):

    def __init__(self):
        super().__init__()
        self.name = input("Enter car name: ")

        while True:
            try:  # проверка правильности ввода данных
                self.price = float(input("Enter price of transport:"))
                if self.price <= 0:
                    raise ValueError  # бросаем ошибку если что то не так
                break
            except ValueError:
                print("Invalid input for price")  # сообщение об ошибке

        self.movementType = input("Enter movement type of transport:")

    def info(self):
        print(f"Moving {self.name}(brrrrrr)")
        print(f"Price of {self.name}: {self.price}")
        print(f"Movement type is {self.movementType}")

    def to_json(self, filename):  # метод для парсинга json в текстовый файл
        return {
            "type": "car",
            "name": self.name,
            "price": self.price,
            "movementType": self.movementType
        }

    def to_xml(self, filename):  # метод для парсинго xml в текстовый файл
        root = ET.Element("car")
        name = ET.SubElement(root, "name")
        name.text = self.name
        price = ET.SubElement(root, "price")
        price.text = str(self.price)
        movement = ET.SubElement(root, "movementType")
        movement.text = self.movementType

        return root


class Truck(Transport):

    def __init__(self):
        super().__init__()
        self.name = input("Enter truck name: ")

        while True:
            try:  # проверка правильности ввода данных
                self.price = float(input("Enter price of truck:"))
                if self.price <= 0:
                    raise ValueError  # бросаем ошибку если что то не так
                break
            except ValueError:
                print("Invalid input for price")  # сообщение об ошибке

        self.movementType = input("Enter movement type of truck:")

    def info(self):
        print(f"Moving {self.name}(brrrrrr)")
        print(f"Price of {self.name}: {self.price}")
        print(f"Movement type is {self.movementType}")

    def to_json(self, filename):  # метод для парсинга json в текстовый файл
        return {
            "type": "truck",
            "name": self.name,
            "price": self.price,
            "movementType": self.movementType
        }

    def to_xml(self, filename):  # метод для парсинго xml в текстовый файл
        root = ET.Element("truck")
        name = ET.SubElement(root, "name")
        name.text = self.name
        price = ET.SubElement(root, "price")
        price.text = str(self.price)
        movement = ET.SubElement(root, "movementType")
        movement.text = self.movementType

        return root