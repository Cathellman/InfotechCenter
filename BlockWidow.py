print('\n<--************************************-->\n')

print('Weather Branch - Developer: Thellman\n')

#Import Libraries Here!

import random
from time import sleep

# Weather Function to determine the weather

def weather():
    weatherForecastList = ['snowing', 'blizzard', 'icy', 'rainy', 'windy', 'sunny', 'death']
    weatherCondition = random.choice(weatherForecastList)
    return weatherCondition

print(weather())