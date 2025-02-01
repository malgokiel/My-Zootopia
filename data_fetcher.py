import requests
import os
from dotenv import load_dotenv

# Loading API_KEY
load_dotenv()
API_KEY = os.getenv('API_KEY')


def fetch_data(animal_to_find):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
    'name': ...,
    'taxonomy': {
        ...
    },
    'locations': [
        ...
    ],
    'characteristics': {
        ...
    }
    },
    """
    api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(animal_to_find)
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})

    animal_data_json = response.json()
    return animal_data_json