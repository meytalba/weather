Weather Info App 

A simple web application that fetches real-time weather information for any city using the WeatherAPI and displays it using Streamlit.

Features

Fetches live weather data based on user input.
Displays:

Current temperature (°C).
Weather condition (e.g., sunny, cloudy, etc.).
Humidity level (%).

Getting Started

Prerequisites

Python 3.7 or higher.
A valid API key from WeatherAPI.

Installation

Clone this repository:

git clone https://github.com/meytalba/weather

cd weather

Install the required dependencies:
pip install -r requirements.txt

Configure your API key:

If you are running the app locally, create a .streamlit/secrets.toml file in the root directory.

Add your API key to the file:
MY_SECRET = "your_api_key_here"
Note: Ensure the .streamlit/secrets.toml file is included in your .gitignore file to keep your API key secure and prevent it from being pushed to GitHub.

If you are deploying the app using Streamlit Cloud, add the API key in the Secrets Management section of the app's settings. The key should be named MY_SECRET to match the code.

Usage

Run the Streamlit app:
streamlit run main.py

Open the app in your browser at http://localhost:8501.
Enter a city name in the text box to retrieve and display the current weather data.

Example

Input: London
Output:
Weather Information for London, United Kingdom:
Temperature: 18°C
Condition: Clear
Humidity: 65%

Project Structure

weather-info-app/
├── main.py          # Main application script
├── requirements.txt # List of dependencies
├── README.md        # Project documentation
└── .streamlit/      # Directory for secrets.toml (not included in GitHub repository)
    └── secrets.toml # Contains the API key (for local use only)
Security

The app uses st.secrets to securely manage sensitive information like the WeatherAPI key.
Ensure the .streamlit/secrets.toml file is added to .gitignore for local development.
When deploying to Streamlit Cloud, use the built-in Secrets Management feature to add your API key.
