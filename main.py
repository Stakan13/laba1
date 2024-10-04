from Transport import Car, Truck, Bus, Helicopter, Plane, Submarine

def get_price():
    while True:
        try:
            price = int(input("Enter price: "))
            if price <= 0:
                raise ValueError
            return price
            break
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

if __name__ == "__main__":
    main()