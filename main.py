# Startup Check

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
# Settings Check
import os, time, re
from pynput.keyboard import Key, Listener
from pynput.mouse import Button, Controller
from colorama import Fore, Back, init
color = Fore.RED

if True:
	settingsread = open("settings.txt", 'r+').read()
	colorscheck = ["BLACK", "BLUE", "CYAN", "GREEN", "LIGHTBLACK_EX", "LIGHTBLUE_EX", "LIGHTCYAN_EX", "LIGHTGREEN_EX", "LIGHTMAGENTA_EX", "LIGHTRED_EX", "LIGHTWHITE_EX", "LIGHTYELLOW_EX", "MAGENTA", "RED", "WHITE", "YELLOW"]
	word_exp='|'.join(colorscheck)
	fullcolorcheck = re.findall(word_exp, open("settings.txt", 'r+').read())

	if "BLACK" in fullcolorcheck:
		color = Fore.BLACK
	elif "BLUE" in fullcolorcheck:
		color = Fore.BLUE
	elif "CYAN" in fullcolorcheck:
		color = Fore.CYAN
	elif "GREEN" in fullcolorcheck:
		color = Fore.GREEN
	elif "LIGHTBLACK_EX" in fullcolorcheck:
		color = Fore.LIGHTBLACK_EX
	elif "LIGHTBLUE_EX" in fullcolorcheck:
		color = Fore.LIGHTBLUE_EX
	elif "LIGHTCYAN_EX" in fullcolorcheck:
		color = Fore.LIGHTCYAN_EX
	elif "LIGHTGREEN_EX" in fullcolorcheck:
		color = Fore.LIGHTGREEN_EX
	elif "LIGHTMAGENTA_EX" in fullcolorcheck:
		color = Fore.LIGTMAGENTA_EX
	elif "LIGHTRED_EX" in fullcolorcheck:
		color = Fore.LIGHTRED_EX
	elif "LIGHTWHITE_EX" in fullcolorcheck:
		color = Fore.LIGHTWHITE_EX
	elif "LIGHTYELLOW_EX" in fullcolorcheck:
		color = Fore.LIGHTYELLOW_EX
	elif "MAGENTA" in fullcolorcheck:
		color = Fore.MAGENTA
	elif "RED" in fullcolorcheck:
		color = Fore.RED
	elif "WHITE" in fullcolorcheck:
		color = Fore.WHITE
	elif "YELLOW" in fullcolorcheck:
		color = Fore.YELLOW
## --------------------------------------------------------------- ##
# Start of program

init(autoreset=True)
if firststartup == False:
	print("Run the installation script before running the main program!")
	quit()

mouse = Controller()



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
print(fullcolorcheck)

for a in "Hello and welcome to":
	time.sleep(0.1)
	print(color + a, end="")
time.sleep(0.6)
for a in "...":
	print(color + a, end="")
	time.sleep(1)

os.system("clear")
for char in openlogo:
	print(color + char, end="")
	time.sleep(0.003)

## Start of clicker code
print(color + "Controls: \nF1 to click \nEsc to exit the script!")
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