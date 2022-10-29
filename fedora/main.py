import os
#Sudo checking!
# Settings checking!
firststartup = False
if True:
	checkstartup = "firststartup=true"
	checkstartup2 = "firststartup=false"
	settingsfile = open("settings.txt", 'r+')
	readfilesize = 'settings.txt'
	if checkstartup in settingsfile:
		firststartup = True
	elif checkstartup2 in settingsfile:
		firststartup = False

	settingsfile.close()

## --------------------------------------------------------------- ##
# Start of program

if firststartup == False:
	print("Run the installation script before running the main program!")
	quit()

import time
from getkey import getkey, keys
import pyautogui
from colorama import Fore, Back, init
init(autoreset=True)
os.system("clear")



openlogo = """ 
  /$$$$$$                                 /$$$$$$  /$$ /$$           /$$      
 /$$__  $$                               /$$__  $$| $$|__/          | $$      
| $$  \ $$  /$$$$$$   /$$$$$$  /$$$$$$$ | $$  \__/| $$ /$$  /$$$$$$$| $$   /$$
| $$  | $$ /$$__  $$ /$$__  $$| $$__  $$| $$      | $$| $$ /$$_____/| $$  /$$/
| $$  | $$| $$  \ $$| $$$$$$$$| $$  \ $$| $$      | $$| $$| $$      | $$$$$$/ 
| $$  | $$| $$  | $$| $$_____/| $$  | $$| $$    $$| $$| $$| $$      | $$_  $$ 
|  $$$$$$/| $$$$$$$/|  $$$$$$$| $$  | $$|  $$$$$$/| $$| $$|  $$$$$$$| $$ \  $$
 \______/ | $$____/  \_______/|__/  |__/ \______/ |__/|__/ \_______/|__/  \__/
          | $$                                                                
          | $$                                                                
          |__/                                                                

                                                                              
							SpamixOfficial 2022                                                          
"""


for a in "Hello and welcome to":
	time.sleep(0.1)
	print(Fore.RED + a, end="")
time.sleep(0.6)
for a in "...":
	print(Fore.RED + a, end="")
	time.sleep(1)

os.system("clear")
for char in openlogo:
	print(Fore.RED + char, end="")
	time.sleep(0.003)

## Start of clicker code
print("Controls: \nF1 to click \nEsc to exit the script!")

while True:
	key = getkey()
	print(key)
	if key == keys.F1:
	    pyautogui.click(button='left')
	if key == keys.DELETE:
		print("work :D")
	if key == keys.ESC:
	    break