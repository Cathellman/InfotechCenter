print('\n<--************************************-->\n')

print('Weather Branch - Developer: Thellman\n')

# Import Libraries Here!
import random
from time import sleep

# Weather Function to determine the weather
global delay
delay = 0.5


def weather():
    # Random Choice of weather condition
    weatherForecastList = ['snowing', 'blizzard', 'icy', 'rainy', 'windy', 'sunny']
    weatherCondition = random.choice(weatherForecastList)
    return weatherCondition


# Weather conditions and their associated messages and speeds
weather_dict = {
    'snowing': {
        'alert_time': 30,
        'speed': 55,
        'message': "The National Weather Service has updated our alarm by 30 minutes because of the snow."
    },
    'blizzard': {
        'alert_time': 60,
        'speed': 10,
        'message': "The National Weather Service has updated our alarm by 60 minutes because of the blizzard."
    },
    'icy': {
        'alert_time': 30,
        'speed': 30,
        'message': "The National Weather Service has updated our alarm by 30 minutes because it's icy."
    },
    'rainy': {
        'alert_time': 15,
        'speed': 55,
        'message': "The National Weather Service has updated our alarm by 15 minutes because it's rainy."
    },
    'windy': {
        'alert_time': 10,
        'speed': 55,
        'message': "The National Weather Service has updated our alarm by 10 minutes because it's windy."
    },
    'sunny': {
        'alert_time': 0,
        'speed': 0,
        'message': "The National Weather Service has not updated anything, it's a good day!"
    }
}


# VRS code to print the weather message, after choosing a random weather condition
def vehicleResponcseSystem():
    # Stores a random weather condition into the 'currentWeather' var
    # Then it goes through and checks to see what the random one matches, then prints message
    currentWeather = weather()

    # Get the weather data from the dictionary
    weather_data = weather_dict.get(currentWeather)

    # Print the weather data
    print(f"\n{weather_data['message']}\n\n Weather Condition: {currentWeather}")
    sleep(delay)

    if currentWeather != 'sunny':
        print(f"\nVRS has been engaged only allowing us to drive {weather_data['speed']} MPH.")
    else:
        print("\nVRS has been disengaged, drive safe!")


vehicleResponcseSystem()
