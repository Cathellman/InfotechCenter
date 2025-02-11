print('\n<--************************************-->\n')

print('Weather Branch - Developer: Thellman\n')

#Import Libraries Here!

import random
from time import sleep

# Weather Function to determine the weather

global delay
delay = 0.5

def weather():

    #Random Choice of weather condition

    weatherForecastList = ['snowing', 'blizzard', 'icy', 'rainy', 'windy', 'sunny', 'death']
    weatherCondition = random.choice(weatherForecastList)

    if weatherCondition == 'death':
        if random.randint(0,50) == 50:
           return weatherCondition
        else:
            weather()
    return weatherCondition

# VRS code to print the weather message, after choosing a random weather condition

def vehicleResponcseSystem():

    # Stores a random weather condition into the 'currentWeather' var
    # Then it gose through and cheackts to see what the random one matches , then prints message

    currentWeather = weather()

    if currentWeather == 'snowing':
        print("\nThe National Weather Service has updated our alarm by 30 minutes because of the snow\n\n Weather Condition: ", currentWeather)
        sleep(delay)
        print("\nVRS has been engaged only allowing us to drive 55MPH.")

    elif currentWeather == 'blizzard':
        print("\nThe National Weather Service has updated our alarm by 60 minutes because of the blizzard\n\n Weather Condition: ", currentWeather)
        sleep(delay)
        print("\nVRS has been engaged only allowing us to drive 10MPH.")

    elif currentWeather == 'icy':
        print("\nThe National Weather Service has updated our alarm by 30 minutes because its icy\n\n Weather Condition: ", currentWeather)
        sleep(delay)
        print("\nVRS has been engaged only allowing us to drive 30MPH.")

    elif currentWeather == 'rainy':
        print("\nThe National Weather Service has updated our alarm by 15 minutes because its rainy\n\n Weather Condition: ", currentWeather)
        sleep(delay)
        print("\nVRS has been engaged only allowing us to drive 55MPH.")

    elif currentWeather == 'windy':
        print("\nThe National Weather Service has updated our alarm by 10 minutes because its windy\n\n Weather Condition: ", currentWeather)
        sleep(delay)
        print("\nVRS has been engaged only allowing us to drive 55MPH.")

    elif currentWeather == 'sunny':
        print("\nThe National Weather Service has not updated anything, its a good day!\n\n Weather Condition: ", currentWeather)
        sleep(delay)
        print("\nVRS has been disengaged, drive safe")

    elif currentWeather == 'death':
        print("Your Dead.")
        sleep(delay)
        print("\nYouve been cooked, Dirve safe :)")

    else:
        print("Error In The Code, Not A Proper Choice!")




vehicleResponcseSystem()




