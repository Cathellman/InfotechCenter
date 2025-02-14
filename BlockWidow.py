
print('\n<--************************************-->\n')


#Import Libraries Here!

import random
import sys
from time import sleep


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