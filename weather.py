from dotenv import load_dotenv
from pprint import pprint
import requests  # used to send HTTP requests
import os

load_dotenv()  # this function loads the variables from the .env  file into the environment


def get_current_weather(city="Durban"):
    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={
        os.getenv("API_KEY")}&q={city}&units=metric'

    # converts the response from the server (assumed to be in a JSON format) into a Python dictionary or list, depending on the structure of the JSON data.
    weather_data = requests.get(request_url).json()

    return weather_data


# to make a module, have to do this. This is so the module can be imported into other modules/python files.
if __name__ == "__main__":
    print('\n*** Get the Current Weather Conditions *** \n')

    city = input("\nPlease enter a city name: ")  # this just in the terminal

# check for empty string or just spaces
    # converts a value to its Boolean equivalent. Non empty strings retyrn True. Empty strings (or strings that become empty after .strip()) return False.
    if not bool(city.strip()):
        # not inverts the Bool value. So if True (ie: empty space), it defaults to the value of "Kansas City".
        city = "Kansas City"

    weather_data = get_current_weather(city)

    print("\n")  # this displays the weather data in the terminal
    pprint(weather_data)
