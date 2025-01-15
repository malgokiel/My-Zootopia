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
    formatted_animal_info = ""
    for animal in animals_data:
        animal_name = animal.get("name", None)
        animal_diet = animal["characteristics"].get("diet", None)
        animal_location = animal["locations"][0]
        animal_type = animal["characteristics"].get("type", None)
        animal_selected_info = {"Diet": animal_diet, "Location": animal_location, "Type": animal_type}

        formatted_animal_info += serialize_animal(animal_name, animal_selected_info)

    return formatted_animal_info


def serialize_animal(animal_name, animal_selected_info):
    """
    Formats a string with animal information to ensure desired html formatting
    """
    serialized_animal = ""
    serialized_animal += '<li class="card__item">'
    serialized_animal += f'<div class="card__title">{animal_name}</div>'
    serialized_animal += '<p class="card__text">'
    for information_type, information_value in animal_selected_info.items():
        if information_value is not None:
            serialized_animal += f"<strong>{information_type}:</strong> {information_value}<br/>\n"
    serialized_animal += '</p>'
    serialized_animal += '</li>'

    return serialized_animal


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
