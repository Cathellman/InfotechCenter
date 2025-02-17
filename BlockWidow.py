import random
from datetime import datetime
from time import sleep
import os
import platform

print("\n***************************\n")
print("Gasoline Branch - Developer: Thellman\n")

wait = 1

def getSystem():
    os_name = platform.system()
    if os_name == "Windows":
        return "Windows"
    elif os_name == "Darwin":
        return "macOS"
    elif os_name == "Linux":
        return "Linux"
    else:
        return "Unknown OS"

def clear():
    print('\n' * 4)

def gasLevelGauge():
    global  gasLevelList
    gasLevelList = ['empty', 'Low', 'Quarter Tank', 'Half Tank', 'Three Quarter Tank', 'Full Tank']
    return random.choice(gasLevelList)

def gasStations():
    gasStationsList = ['Shell', 'Marathon', 'SpeedWay', 'Circle K', 'Wesco', 'Meijer', 'Buc-ees', 'Cosco']
    return random.choice(gasStationsList)

def gaslevelCheck():
    milesToGasStationLow = round(random.uniform(1,25),1)
    milesToGasStationQuTank = round(random.uniform(25.1,50),1)

    clear()
    if gaslevel == 'empty':
        print("Empty. \n")
        sleep(wait)
        clear()
        print("Calling AAA")

    elif gaslevel == 'Low':
        print('Low. \n')
        sleep(wait)
        clear()
        print("The closest gas station is", gasStations(), "which is" , milesToGasStationLow, 'miles away\n')

    elif gaslevel == 'Quarter Tank':
        print('1/4. \n')
        sleep(wait)
        clear()
        print("The closest gas station is", gasStations(), "which is" , milesToGasStationQuTank, 'miles away\n')

    elif gaslevel == 'Half Tank':
        print('2/4 Tank.\n')
        sleep(wait)
        clear()

    elif gaslevel == 'Three Quarter Tank':
        print('3/4 Tank.\n')
        sleep(wait)
        clear()

    else:
        print('Full')
        sleep(wait)
        clear()


systemOS = getSystem()

gaslevel = gasLevelGauge()

startTime = datetime.now().second

gaslevelCheck()
i = 0
while True:
    sleep(0.1)
    if startTime + 3 < datetime.now().second:
        startTime = datetime.now().second
        i = i + 1
        gaslevelCheck()
        if i > 2:
            i = 0
            index = gasLevelList.index(gaslevel)
            if index == 0:
                print("Get gas now\n")
            else:
                gaslevel = gasLevelList[index - 1]