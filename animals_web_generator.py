import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def extract_animal_information(animals_data):
    """
    The Function extracts information about each animal into a string:
    - name - diet - top location - type
    """
    output = ""
    for animal in animals_data:
        animal_name = animal.get("name", None)
        animal_diet = animal["characteristics"].get("diet", None)
        animal_location = animal["locations"][0]
        animal_type = animal["characteristics"].get("type", None)
        animal_selected_info = {"Name": animal_name, "Diet": animal_diet, "Location": animal_location, "Type": animal_type}

        output += '<li class="card__item">'
        for information_type, information_value in animal_selected_info.items():
            if information_value is not None:
                output += f"{information_type}: {information_value}<br/>\n"
        output += '</li>'
    return output


def add_animal_data_to_html(animals_data):
    """
    Opens html file and passes animal information as age content
    """
    with open("animals_template.html", "r") as fileobj:
        template = fileobj.read()

    new_phrase = template.replace("__REPLACE_ANIMALS_INFO__", extract_animal_information(animals_data))

    with open("animals_template.html", "w") as fileobject:
        fileobject.write(new_phrase)


def main():
    all_animals_data = load_data('animals_data.json')
    add_animal_data_to_html(all_animals_data)

if __name__ == "__main__":
    main()
