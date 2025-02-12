import requests
import os
import sys
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

    try:
        response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
        if response.status_code == 200:
            animal_data_json = response.json()
            return animal_data_json
        else:
            print("\n\n******* There has been an error: ", response.status_code, "*******\n\n")
            return response.status_code
    except requests.exceptions.ConnectionError:
        print(
            "We were not able to connect to api-ninjas. "
            "Please check your Internet connection or try again later.")
        sys.exit()

