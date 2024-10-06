from Transport import Car, Truck, Bus, Helicopter, Plane, Submarine
from ControllerJSON import OperationJSON


def get_positive_num(message: str) -> int:
    while True:
        try:
            price = int(input(message))
            if price <= 0:
                raise ValueError
            return price
        except ValueError:
            print("Please enter right value")


def print_data(data):
    print("\nData from JSON")

    print("\nCars")
    for car in data["cars"]:
        print(f"Name: {car['name']}, Price: {car['price']}, Movement type: {car['movement_type']}")

    print("\nTrucks")
    for truck in data["trucks"]:
        print(f"Name: {truck['name']}, Price: {truck['price']}, Load capacity: {truck['load_capacity']}")

    print("\nBuses")
    for bus in data["buses"]:
        print(f"Name: {bus['name']}, Price: {bus['price']}, Max passengers: {bus['max_passenger']}")

    print("\nPlanes")
    for plane in data["planes"]:
        print(f"Name: {plane['name']}, Price: {plane['price']}, Max passengers: {plane['speed']}")

    print("\nHelicopters")
    for helicopter in data["helicopters"]:
        print(f"Name: {helicopter['name']}, Price: {helicopter['price']}, Max passengers: {helicopter['rpm']}")

    print("\nSubmarines")
    for submarine in data["submarines"]:
        print(f"Name: {submarine['name']}, Price: {submarine['price']}, Max passengers: {submarine['diving_depth']}")


def main():
    data = OperationJSON.load_json("result.json")

    while True:
        print("choose operation \n"
              "1. print data from JSON\n"
              "2. add car\n"
              "3. add truck\n"
              "4. add submarine\n"
              "5. add bus\n"
              "6. add helicopter\n"
              "7. add plane\n"
              "8. save to JSON\n"
              "9. exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print_data(data)

        elif choice == 2:
            name = input("Enter car name: ")
            price = get_positive_num("Enter car price: ")
            movement_type = input("Enter car movement type: ")
            car = Car(name, price, movement_type)
            OperationJSON.add_car(data, car)

        elif choice == 3:
            name = input("Enter truck name: ")
            price = get_positive_num("Enter truck price: ")
            load_capacity = get_positive_num("Enter truck load capacity: ")
            truck = Truck(name, price, load_capacity)
            OperationJSON.add_truck(data, truck)

        elif choice == 4:
            name = input("Enter submarine name: ")
            price = get_positive_num("Enter submarine price: ")
            max_depth = get_positive_num("Enter submarine max depth: ")
            submarine = Submarine(name, price, max_depth)
            OperationJSON.add_submarine(data, submarine)

        elif choice == 5:
            name = input("Enter bus name: ")
            price = get_positive_num("Enter bus price: ")
            max_passengers = get_positive_num("Enter bus max passengers: ")
            bus = Bus(name, price, max_passengers)
            OperationJSON.add_bus(data, bus)

        elif choice == 6:
            name = input("Enter helicopter name: ")
            price = get_positive_num("Enter helicopter price: ")
            rpm = get_positive_num("Enter helicopter rpm: ")
            heli = Helicopter(name, price, rpm)
            OperationJSON.add_helicopter(data, heli)

        elif choice == 7:
            name = input("Enter plane name: ")
            price = get_positive_num("Enter plane price: ")
            speed = get_positive_num("Enter plane speed: ")
            plane = Plane(name, price, speed)
            OperationJSON.add_plane(data, plane)

        elif choice == 8:
            OperationJSON.safe_json(data, "result.json")

        else:
            break


if __name__ == "__main__":
    main()
