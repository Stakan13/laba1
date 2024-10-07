import json


class OperationJSON:

    @staticmethod
    def safe_json(data, filename: str):
        try:
            with open(filename, "w", encoding="utf-8") as json_file:  # сохранение в файл
                json.dump(data, json_file, indent=4, ensure_ascii=False, default=lambda o: o.__dict__)
            print("Saved file: " + filename)
        except IOError as e:  # обработка ошибки при открытии фойла
            print("error when starting json file: " + str(e))

    @staticmethod
    def load_json(filename):
        try:
            with open(filename, "r", encoding="utf-8") as js:  # чтение из json
                result = json.load(js)
                return result
        except (FileNotFoundError, json.decoder.JSONDecodeError):  # если файла нет или
            # он пуст заполняем его пустым словарем
            return {"cars": [], "trucks": [], "buses": [], "planes": [],
                    "helicopters": [], "submarines": []}

    # добавление инфы в словарь
    @staticmethod
    def add_car(data, car):
        data["cars"].append(car)

    @staticmethod
    def add_truck(data, truck):
        data["trucks"].append(truck)

    @staticmethod
    def add_bus(data, bus):
        data["buses"].append(bus)

    @staticmethod
    def add_plane(data, plane):
        data["planes"].append(plane)

    @staticmethod
    def add_helicopter(data, helicopter):
        data["helicopters"].append(helicopter)

    @staticmethod
    def add_submarine(data, submarine):
        data["submarines"].append(submarine)
