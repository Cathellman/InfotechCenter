import random
from time import sleep

print("\n***************************\n")
print("Gasoline Branch - Developer: Thellman\n")

def gasLevelGauge():
  gasLevelList = ['Empty', 'Low', 'Quarter Tank', 'Half Tank', 'Three Quarter Tank', 'Full Tank']
  return random.choice(gasLevelList)


