from flask import Flask, render_template
from data_fetcher import fetch_data

selected_animal = input("Enter a name of an animal: ")

# App configuration
app = Flask(__name__)

def extract_animal_information(animals_data):
    """
    The Function extracts information about each animal into a string:
    - name - diet - top location - type
    """
    all_animals_info = []
    for animal in animals_data:
        animal_name = animal.get("name", None)
        animal_diet = animal["characteristics"].get("diet", None)
        animal_location = animal["locations"][0]
        animal_type = animal["characteristics"].get("type", None)
        animal_selected_info = {"name": animal_name,
                                "diet": animal_diet,
                                "location": animal_location,
                                "type": animal_type}

        all_animals_info.append(animal_selected_info)
    return all_animals_info


@app.route("/", methods=["GET"])
def animals_template():
    """
    Passes a list of animal dictionaries
    and renders a template
    """
    global selected_animal
    all_animals_data = fetch_data(selected_animal)
    animals = extract_animal_information(all_animals_data)
    return render_template("animals_template.html", animals=animals, selected_animal=selected_animal)


if __name__ == "__main__":
    app.run(debug=False)
