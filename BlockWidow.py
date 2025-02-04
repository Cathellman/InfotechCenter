# Import necessary libraries
import sys
from time import sleep

# Display welcome message for the developer and InfoTechCenter
print('\nWelcome Branch - Developer: Thellman')
print("\nWelcome to InfoTechCenter v1.0\n")

# Initialize variables
x = 0            # Counter to track the number of iterations
ellipsis = 0      # Counter for the number of dots to display in the progress message

# Main loop to simulate system booting
while x != 20:
   x += 1  # Increment the counter for iterations
   message = ("Infotech Center System Booting" + "." * ellipsis)  # Construct the message with increasing dots
   ellipsis += 1  # Increment the number of dots
   sys.stdout.write("\r" + message)  # Write the message to stdout (console) without a newline
   sleep(.5)  # Pause for 0.5 seconds to simulate a delay between updates
   
   # Reset the ellipsis counter after 3 dots (creates a repeating cycle of 0-3 dots)
   if ellipsis == 4:
       ellipsis = 0

   # Once the loop reaches 20 iterations, print the final boot message
   if x == 20:
       print("\n\nOperating System Booted Up - Retina Scanned - Access Granted\n")
