import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def print_animal_information(animals_data):
    """
    The Function prints out information about each animal:
    - name - diet - top location - type
    """
    for animal in animals_data:
        animal_name = animal.get("name", None)
        animal_diet = animal["characteristics"].get("diet", None)
        animal_location = animal["locations"][0]
        animal_type = animal["characteristics"].get("type", None)
        animal_selected_info = {"Name": animal_name, "Diet": animal_diet, "Location": animal_location, "Type": animal_type}

        for information_type, information_value in animal_selected_info.items():
            if information_value is not None:
                print(f"{information_type}: {information_value}")
        print()


def main():
    animals_data = load_data('animals_data.json')
    print_animal_information(animals_data)


if __name__ == "__main__":
    main()