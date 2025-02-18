import random
from datetime import datetime
from time import sleep
import sys
import platform
import os

print("\n***************************\n")
print("Gasoline Branch - Developer: Thellman\n")

wait = 1
normal = 0.05

def typing(text, time):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(time)

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
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")



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

    
    if gaslevel == 'empty':
        typing("Empty. \n", normal)
        sleep(wait)
        typing("Calling AAA.",  normal)
        clear()

    elif gaslevel == 'Low':
        typing('Low. \n', normal)
        sleep(wait)
        typing("The closest gas station is "+ gasStations() + " which is " + str(milesToGasStationLow) + ' miles away.\n', normal)
        clear()

    elif gaslevel == 'Quarter Tank':
        typing('1/4 Tank. \n', normal)
        sleep(wait)
        typing("The closest gas station is "+ gasStations() +  " which is " + str(milesToGasStationQuTank) +  ' miles away.\n', normal)
        clear()

    elif gaslevel == 'Half Tank':
        typing('2/4 Tank.\n', normal)
        sleep(wait)
        clear()

    elif gaslevel == 'Three Quarter Tank':
        typing('3/4 Tank.\n', normal)
        sleep(wait)
        clear()

    else:
        typing('Full.\n', normal)
        sleep(wait)
        clear()


systemOS = getSystem()

gaslevel = gasLevelGauge()

startTime = datetime.now().second

gaslevelCheck()
i = 0
while True:
    sleep(0.1)
    if startTime + 5 < datetime.now().second:
        startTime = datetime.now().second
        i = i + 1
        gaslevelCheck()
        if i > 2:
            i = 0
            index = gasLevelList.index(gaslevel)
            if index == 0:
                print("\nGet gas now\n")
            else:
                gaslevel = gasLevelList[index - 1]