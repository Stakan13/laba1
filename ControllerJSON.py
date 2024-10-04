import json


class OperationJSON:
    @staticmethod
    def safe_json(data, filename):
        try:
            with open(filename, "w") as json_file:
                json.dump(data, json_file, indent=4)
            print("Saved file: " + filename)
        except IOError as e:
            print("error when starting json file: " + str(e))

    @staticmethod
    def read_json(filename):
        try:
            with open(filename, "r") as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            print("That file not file")
