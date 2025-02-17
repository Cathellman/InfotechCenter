import random
from datetime import datetime
from time import sleep

print("\n***************************\n")
print("Gasoline Branch - Developer: Thellman\n")

def gasLevelGauge():
    gasLevelList = ['Empty', 'Low', 'Quarter Tank', 'Half Tank', 'Three Quarter Tank', 'Full Tank']
    return random.choice(gasLevelList)

gaslevel = gasLevelGauge()

startTime = datetime.now().minute
current_time = datetime.now().minute

def gasStations():
    gasStations = ['Shell', 'Marathon', 'SpeedWay', 'Circle K', 'Wesco', 'Meijer', 'Buc-ees', 'Cosco']
    return random.choice(gasStations)

def gaslevelCheck():
    milesToGasStationLow = round(random.uniform(1,25),1)
    milesToGasStationQuTank = round(random.uniform(25.1,50),1)

    if gaslevel.lower == 'empty':
        print("Out of Gas, L bozo.\n")
        sleep(0.5)
        print("Calling AAA")
    elif gaslevel == 'Low':
        print('Low. You should get a job to get more gas, imagine\n')
        sleep(0.5)
        print("The closest gas station is", gasStations(), "which is" , milesToGasStationLow, 'miles away\n')
    elif gaslevel == 'Quarter Tank':
        print('Quarter Tank. How could you.\n')
        sleep(0.5)
        print("The closest gas station is", gasStations(), "which is" , milesToGasStationQuTank, 'miles away\n')
    elif gaslevel == 'Half Tank':
        print('Half Tank.\n')
    elif gaslevel == 'Three Quarter Tank':
        print('Three Quarter Tank.\n')
    else:
        print('Full')
        


gaslevelCheck()
i = 0
while True:
    if startTime > current_time:
        startTime = current_time
        i = i + 1
        gaslevelCheck()
        if i > 2:
            i = 0
            gaslevel = gasLevelGauge()
