import requests
import json

# Define your API key and base URLs
API_KEY = 'AGbFAKx58hyjQScCXIYrxuEwJh2W2cmv'
WEATHER_BROKER_URL = 'https://weather-broker-cdn.api.bbci.co.uk/en/forecast/aggregated/'

# Weather Data Extraction
def get_weather_forecast(location_id):
    url = f'{WEATHER_BROKER_URL}{location_id}'
    params = {
        'api_key': API_KEY
    }
    response = requests.get(url, params=params)
    return response.json()

# Data Transformation
def transform_weather_data(weather_data):
    forecasts = weather_data['forecasts']
    transformed_data = {}
    for forecast in forecasts:
        issue_date = forecast['issueDate']
        weather_description = forecast['enhancedWeatherDescription']
        transformed_data[issue_date] = weather_description
    return transformed_data

# Main function to get weather forecast for a city and save JSON output to a file
def main():
    location_id = '1174872'  # Karachi's location ID
    weather_data = get_weather_forecast(location_id)
    transformed_data = transform_weather_data(weather_data)
    
    # Save the transformed data to a JSON file
    with open('karachi_weather_forecast.json', 'w') as json_file:
        json.dump(transformed_data, json_file, indent=4)
    
    print("Weather forecast data saved to karachi_weather_forecast.json")

if __name__ == '__main__':
    main()
