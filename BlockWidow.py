#Libraries HERE
import sys
from time import sleep


print('\nWelcome Branch - Developer: Thellman')

print("\nWelcome to InfoTechCenter v1.0\n")


x = 0
ellipsis = 0

while x != 20:
   x += 1
   message = ("Infotech Center System Booting" + "." * ellipsis)
   ellipsis += 1
   sys.stdout.write("\r" + message)
   sleep(.5)
   if ellipsis == 4:
       ellipsis = 0
   if x == 20:
       print("\n\nOperating System Booted Up - Retina Scanned - Access Granted\n")