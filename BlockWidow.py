import random
from time import sleep

print("\n***************************\n")
print("Gasoline Branch - Developer: Thellman\n")

def gasLevelGauge():
    gasLevelList = ['Empty', 'Low', 'Quarter Tank', 'Half Tank', 'Three Quarter Tank', 'Full Tank']
    return random.choice(gasLevelList)

def gasStations():
    gasStations = ['Shell', 'Marathon', 'SpeedWay', 'Circle K', 'Wesco', 'Meijer', 'Buc-ees', 'Cosco']
    return random.choice(gasStations)

print(gasLevelGauge())
print(gasStations())
