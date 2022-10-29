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
if firststartup == False:
	print("Run the installation script before running the main program!")
	quit()
## --------------------------------------------------------------- ##
# Start of program

import os, time
from pynput.keyboard import Key, Listener
from pynput.mouse import Button, Controller
from colorama import Fore, Back, init

init(autoreset=True)

mouse = Controller()
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
def on_press(key):
    if key == Key.f1:
        mouse.press(Button.left)
        mouse.release(Button.left)
    if key == Key.delete:
    	print("work :D")

def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()