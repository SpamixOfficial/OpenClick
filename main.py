# Startup Check
debugswitch = 1
import os, time, re
import threading
from flagser import *

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
    'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9'
    ]
	word_exp='|'.join(keycheck)
	fullkeycheck = re.findall(word_exp, open("settings.txt", 'r+').read())

	if "f1" in fullkeycheck:
		hotkey = Key.f1
	elif "f2" in fullkeycheck:
		hotkey = Key.f2
	elif "f3" in fullkeycheck:
		hotkey = Key.f3
	elif "f4" in fullkeycheck:
		hotkey = Key.f4
	elif "f5" in fullkeycheck:
		hotkey = Key.f5
	elif "f6" in fullkeycheck:
		hotkey = Key.f6
	elif "f7" in fullkeycheck:
		hotkey = Key.f7
	elif "f8" in fullkeycheck:
		hotkey = Key.f8
	elif "f9" in fullkeycheck:
		hotkey = Key.f9
if True:
	settingsread = open("settings.txt", 'r+').read()
	debugcheck = [
     "debugmode=true", "debugmode=false"
    ]
	word_exp='|'.join(debugcheck)
	debugcheckr = re.findall(word_exp, open("settings.txt", 'r+').read())
	if "debugmode=true" in debugcheckr:
		debugmode = True
	elif "debugmode=false" in debugcheckr:
		debugmode = False
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
if debugmode == True:
	print("Debugmode")
	print("\r" + str(fullcolorcheck) + str(fullkeycheck))
for a in "Hello and welcome to":
	time.sleep(0.01)
	print(color + a, end="")
time.sleep(0.06)
for a in "...":
	print(color + a, end="")
	time.sleep(0.2)

os.system("clear")
for char in openlogo:
	print(color + char, end="")
	time.sleep(0.0003)

## Start of clicker code
# variable to controll if the clicker should autoclick
shouldClick = False
shouldAuto = False
clickDelay = 0.2

# check for auto click flag
class Auto(Flag):
	shortFlag="-a"
	longFlag="-autoclick"
	description='adds autoclick function'
	def onCall(self,args):
		global shouldAuto
		shouldAuto = True

class AutoDelay(Flag):
	shortFlag="-ad"
	longFlag="-autoclickdelay"
	description='sets the autoclick delay (default 0.1 secounds between clicks)'
	def onCall(self,args):
		global clickDelay
		clickDelay = float(args[0])

a = FlagManager([Auto(),AutoDelay()])
a.check()


print(color + "Controls: \n" + str(hotkey) + " to click \nEsc to exit the script!")
def on_press(key):
	global Key
	global debugmode
	global debugswitch
	global shouldClick
	global shouldAuto

	if key == hotkey:
        # if autoclick flag was set we auto click
		if shouldAuto == True:
			#toggles the autoclick
			shouldClick = not shouldClick
			# start new thread to handle the autoclicking on
			autoClickThread = threading.Thread(target=autoClick)
			autoClickThread.start()

		if debugmode == True:
			print(key)
		mouse.press(Button.left)
		mouse.release(Button.left)
	if key == Key.delete:
		if debugswitch == 1:
			debugmode = True
			debugswitch = 1+1
			print(debugswitch)
		if debugswitch == 2:
			debugmode = False
			debugswitch = 2-1
			print(debugswitch)

def on_release(key):
	global shouldClick
	if key == Key.esc:
		# Stop autoclick
		shouldClick = False
		# Stop listener
		return False

# method to autoclick
def autoClick():
	global shouldClick
	while shouldClick:
		mouse.press(Button.left)
		mouse.release(Button.left)
		time.sleep(clickDelay)

# Collect events until released
with Listener(
		on_press=on_press,
		on_release=on_release) as listener:
	listener.join()

