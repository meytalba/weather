

import requests
import streamlit as st

API_KEY = st.secrets["MY_SECRET"]
BASE_URL = "http://api.weatherapi.com/v1/current.json"

secret =st.secrets["MY_SECRET"]
st.text(f"my secret is {secret}, keep it for yourself")

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
        st.write(f"Weather Information for {location}, {country}:")
        st.write(f"Temperature: {temperature}°C")
        st.write(f"Condition: {condition}")
        st.write(f"Humidity: {humidity}%")
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching weather data: {e}")
    except KeyError:
        st.error("Error: City not found or unexpected response format.")

# Main program
st.title('Weather Information')
city = st.text_input("Enter your city:", key="city")

if city:  # Check if the user has entered a city
    get_weather_data(city)
