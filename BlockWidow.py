
print('\n<--************************************-->\n')


# Import Libraries Here!
import random
import sys
from time import sleep
from datetime import datetime
import platform

# ANSI escape codes for terminal colors
RESET = "\033[0m"  # Resets the color to default
BOLD = "\033[1m"  # Bold text formatting
GREEN = "\033[32m"  # Green color for success or final messages
YELLOW = "\033[33m"  # Yellow color (not used, but can be for warnings)
CYAN = "\033[36m"  # Cyan color for the booting process

# Display welcome message with cyan color for the developer's name
print(f'\n{CYAN}Welcome Branch - Developer: Thellman{RESET}')

# Display InfoTechCenter welcome message in green
print(f"{GREEN}\nWelcome to InfoTechCenter v1.0\n{RESET}")

# Initialize variables
x = 0            # Counter to track the number of iterations
ellipsis = 0      # Counter for the number of dots to display in the progress message

# Main loop to simulate the system booting process
while x != 20:
   x += 1  # Increment the counter for iterations

   # Construct the message with increasing dots and apply cyan color to the booting message
   message = f"{CYAN}Infotech Center System Booting" + "." * ellipsis
   ellipsis += 1  # Increment the number of dots to simulate progress

   # Write the message to stdout (console) without a newline, with a reset color at the end
   sys.stdout.write(f"\r{message}{RESET}")
   sleep(.3)  # Pause for 0.5 seconds to simulate a delay between updates

   # Reset the ellipsis counter after 3 dots (creates a repeating cycle of 0-3 dots)
   if ellipsis == 4:
       ellipsis = 0

   # Once the loop reaches 20 iterations, print the final boot message in bold green
   if x == 20:
       print(f"\n\n{BOLD}{GREEN}Operating System Booted Up - Retina Scanned - Access Granted\n{RESET}")

#Gas Branch Here -



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


while True:
    sleep(0.1)
    if startTime + 5 < datetime.now().second:
        vehicleResponcseSystem()
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