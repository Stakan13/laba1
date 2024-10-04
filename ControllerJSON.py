import json


class OperationJSON:

    @staticmethod
    def safe_json(data, filename: str):
        try:
            with open(filename, "w", encoding="utf-8") as json_file:
                json.dump(data, json_file, indent=4, ensure_ascii=False)
            print("Saved file: " + filename)
        except IOError as e:
            print("error when starting json file: " + str(e))

    @staticmethod
    def load_json(filename):
        try:
            with open(filename, "r", encoding="utf-8") as js:
                result = json.load(js)
                return result
        except FileNotFoundError:
            return {"cars": [], "trucks": [], "buses": [], "planes": [],
                    "helicopters": [], "submarines": []}

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
