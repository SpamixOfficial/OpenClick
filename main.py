# Startup Check
import os, time, re
firststartup = False
if True:
	settingsread = open("settings.txt", 'r+').read()
	rawstartcheck = ["firststartup=true", "firststartup=false"]
	word_exp='|'.join(rawstartcheck)
	fullstartupcheck = re.findall(word_exp, open("settings.txt", 'r+').read())
	if "firststartup=true" in fullstartupcheck:
		firststartup = True
	elif "firststartup=false" in fullstartupcheck:
		firststartup = False
		print("Run the installation script before running the main program!")
		quit()

## --------------------------------------------------------------- ##
# Settings Check
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

hotkey = Key.f1
if True:
	settingsread = open("settings.txt", 'r+').read()
	keycheck = [
    'alt', 'backspace', 'cmd', 'ctrl', 'delete', 'down', 'end', 'enter',
     'f1', 'f10', 'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18',
    'f19', 'f2', 'f20', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'home',
    ]
	word_exp='|'.join(keycheck)
	fullkeycheck = re.findall(word_exp, open("settings.txt", 'r+').read())

	if "f1" in fullkeycheck:
		hotkey = Key.f1
	elif "f2" in fullkeycheck:
		hotkey = Key.f2
## --------------------------------------------------------------- ##
# Start of program

init(autoreset=True)

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
print(color + "Controls: \n" + str(hotkey) + " to click \nEsc to exit the script!")
def on_press(key):
	global Key
	if key == hotkey:

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