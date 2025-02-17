import random
from datetime import datetime
from time import sleep

print("\n***************************\n")
print("Gasoline Branch - Developer: Thellman\n")

def gasLevelGauge():
    gasLevelList = ['Empty', 'Low', 'Quarter Tank', 'Half Tank', 'Three Quarter Tank', 'Full Tank']
    return random.choice(gasLevelList)

gaslevel = gasLevelGauge()
current_time = datetime.now().time()

startTime = datetime.now().minute
print(startTime)

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

gaslevelCheck()