

import requests
import streamlit as st

API_KEY = 'e03b584fc0724c28a9271250243112'
BASE_URL = "http://api.weatherapi.com/v1/current.json"

def get_weather_data(city_name):
    try:
        # Make API call
        url = f"{BASE_URL}?key={API_KEY}&q={city_name}"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the response JSON
        data = response.json()

        # Extract relevant weather data
        location = data['location']['name']
        country = data['location']['country']
        temperature = data['current']['temp_c']
        condition = data['current']['condition']['text']
        humidity = data['current']['humidity']

        # Display the weather data
        print(f"Weather Information for {location}, {country}:\n")
        print(f"Temperature: {temperature}°C")
        print(f"Condition: {condition}")
        print(f"Humidity: {humidity}%")
    except requests.exceptions.RequestException as e:
        print("Error fetching weather data:", e)
    except KeyError:
        print("Error: City not found or unexpected response format.")

# Main program
st.title('what is your city')
# city = st.text()
city = st.text_input("Where?", key="city")

get_weather_data(city)

import streamlit as st

