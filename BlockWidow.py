print('\n<--************************************-->\n')

print('Weather Branch - Developer: Thellman\n')

#Import Libraries Here!

import random
from time import sleep

# Weather Function to determine the weather

def weather():
    weatherForecastList = ['snowing', 'blizzard', 'icy', 'rainy', 'windy', 'sunny', 'death']
    weatherCondition = random.choice(weatherForecastList)

    if weatherCondition == 'death':
        if random.randint(0,50) == 50:
           return weatherCondition
        else:
            weather() 
    return weatherCondition



def vehicleResponcseSystem():
    currentWeather = weather()

    if currentWeather == 'snowing': 
        print("\nThe National Weather Service has updated our alarm by 30 minutes because of the snow\n\n Weather Condition: ", currentWeather)

    elif currentWeather == 'blizzard': 
        print("\nThe National Weather Service has updated our alarm by 30 minutes because of the blizzard\n\n Weather Condition: ", currentWeather)

    elif currentWeather == 'icy': 
        print("\nThe National Weather Service has updated our alarm by 30 minutes because its icy\n\n Weather Condition: ", currentWeather)

    elif currentWeather == 'rainy': 
        print("\nThe National Weather Service has updated our alarm by 30 minutes because its rainy\n\n Weather Condition: ", currentWeather)

    elif currentWeather == 'windy': 
        print("\nThe National Weather Service has updated our alarm by 30 minutes because its windy\n\n Weather Condition: ", currentWeather)

    elif currentWeather == 'sunny': 
        print("\nThe National Weather Service has not updated anything, its a good day!\n\n Weather Condition: ", currentWeather)

    elif currentWeather == 'death': 
        print("Your Dead.")

    print("\n\n")


vehicleResponcseSystem()




