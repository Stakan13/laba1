from Transport import Car, Truck, Bus, Helicopter, Plane, Submarine

def get_positive_num(messege: str) -> int:
    while True:
        try:
            price = int(input(messege))
            if price <= 0:
                raise ValueError
            return price
        except ValueError:
            print("Please enter right value")

def print_data():
    pass

def main():
    print("choose operation \n"
          "1. print data from JSON\n"
          "2. print data from XML\n"
          "3. add car\n"
          "4. add truck\n"
          "5. add submarine\n"
          "6. add bus\n"
          "7. add helicopter\n"
          "8. add plane\n"
          "9. save to XML\n"
          "10. save to JSON\n"
          "11. exit")

    while True:
        choice = int(input("Enter your choice: "))

        if choice == 3:
            name = input("Enter car name: ")
            price = get_positive_num("Enter car price: ")
            movement_type = input("Enter car movement type: ")
            car = Car(name, price, movement_type)

        elif choice == 4:
            name = input("Enter truck name: ")
            price = get_positive_num("Enter truck price: ")
            load_capacity = get_positive_num("Enter truck load capacity: ")
            truck = Truck(name, price, load_capacity)

        elif choice == 5:
            name = input("Enter submarine name: ")
            price = get_positive_num("Enter submarine price: ")
            max_depth = get_positive_num("Enter submarine max depth: ")
            submarine = Submarine(name, price, max_depth)

        elif choice == 6:
            name = input("Enter bus name: ")
            price = get_positive_num("Enter bus price: ")
            max_passengers = get_positive_num("Enter bus max passengers: ")
            bus = Bus(name, price, max_passengers)

        elif choice == 7:
            name = input("Enter helicopter name: ")
            price = get_positive_num("Enter helicopter price: ")
            rpm = get_positive_num("Enter helicopter rpm: ")
            heli = Helicopter(name, price, rpm)

        elif choice == 8:
            name = input("Enter plane name: ")
            price = get_positive_num("Enter plane price: ")
            speed = get_positive_num("Enter plane speed: ")
            plane = Plane(name, price, speed)


if __name__ == "__main__":
    main()