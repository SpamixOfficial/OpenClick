# Startup Check
debugswitch = 1
import os, time, re
import threading
import json
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


firststartup = False
if True:
	#settingsread = open("settings.txt", 'r+').read()
	#rawstartcheck = ["firststartup=true", "firststartup=false"]
	#word_exp='|'.join(rawstartcheck)
	#fullstartupcheck = re.findall(word_exp, open("settings.txt", 'r+').read())
	with open('settings.json') as f:
		data = json.load(f)

	fullstartupcheck = (data['firststartup'])

	if fullstartupcheck == True:
		firststartup = True
	elif fullstartupcheck == False:
		firststartup = False
		print("Run the installation script before running the main program!")
		quit()

## --------------------------------------------------------------- ##
# Settings Check
from flagser import *
from pynput.keyboard import Key, Listener
from pynput.mouse import Button, Controller
from colorama import Fore, Back, init
color = Fore.RED



if True:
	# settingsread = open("settings.txt", 'r+').read()
	# colorscheck = ["BLACK", "BLUE", "CYAN", "GREEN", "LIGHTBLACK_EX", "LIGHTBLUE_EX", "LIGHTCYAN_EX", "LIGHTGREEN_EX", "LIGHTMAGENTA_EX", "LIGHTRED_EX", "LIGHTWHITE_EX", "LIGHTYELLOW_EX", "MAGENTA", "RED", "WHITE", "YELLOW"]
	# word_exp='|'.join(colorscheck)
	# fullcolorcheck = re.findall(word_exp, open("settings.txt", 'r+').read())

	with open('settings.json') as f:
		data = json.load(f)
		fullcolorcheck =  (data['textcolor'])

	color_map = {
    'BLACK': Fore.BLACK,
    'BLUE': Fore.BLUE,
    'CYAN': Fore.CYAN,
    'GREEN': Fore.GREEN,
    'LIGHTBLACK_EX': Fore.LIGHTBLACK_EX,
    'LIGHTBLUE_EX': Fore.LIGHTBLUE_EX,
    'LIGHTCYAN_EX': Fore.LIGHTCYAN_EX,
    'LIGHTGREEN_EX': Fore.LIGHTGREEN_EX,
    'LIGHTMAGENTA_EX': Fore.LIGHTMAGENTA_EX,
    'LIGHTRED_EX': Fore.LIGHTRED_EX,
    'LIGHTWHITE_EX': Fore.LIGHTWHITE_EX,
    'LIGHTYELLOW_EX': Fore.LIGHTYELLOW_EX,
    'MAGENTA': Fore.MAGENTA,
    'RED': Fore.RED,
    'WHITE': Fore.WHITE,
    'YELLOW': Fore.YELLOW,
}

color = color_map.get(fullcolorcheck, Fore.RESET)

hotkey = Key.f1
constantKey = Key.f2
contantClickDelay = 0.1 # the delay between clicks in constantclick

if True:
	with open('settings.json') as f:
		data = json.load(f)
		hotkey = "Key." + (data['hotkey'])

if True:
	with open('settings.json') as f:
		data = json.load(f)
		constantKey =  "Key." + (data['constantkey'])
#sets the constantclickdelay
if True:
	with open('settings.json') as f:
		data = json.load(f)
		constantClickDelay = (data['constantclickdelay'])

if True:
	with open('settings.json') as f:
		data = json.load(f)
		debugmode = (data['debugmode'])
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
shouldClick = False # controlls the constantclick

# this is Flag class handling constantclick delay
class AutoDelay(Flag):
	shortFlag="-cd"
	longFlag="-constantClickDelay"
	description='sets the constantclick delay (default 0.1 secounds between clicks)'
	def onCall(self,args):
		global contantClickDelay
		contantClickDelay = float(args[0])

a = FlagManager([AutoDelay()])
a.check()


print(color + "Controls: \n" + str(hotkey) + " to click (hold to click!) \n" + str(constantKey) + " to click constantly (toggle on/off by clicking the key!)\nEsc to exit!")

def on_press(key):
	global Key
	global debugmode
	global debugswitch
	global shouldClick

# checks if the string values if the objects are the same
# this makes so we can set the hotkey to a string instead
# of a key instance
	if str(key) == str(constantKey): # if the constant key is pressed

		shouldClick = not shouldClick #toggles the autoclick
		# start new thread to handle the autoclicking on
		autoClickThread = threading.Thread(target=autoClick)
		autoClickThread.start()

	if str(key) == str(hotkey): #check hotkey
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
		time.sleep(contantClickDelay) #add delay

# Collect events until released
with Listener(
		on_press=on_press,
		on_release=on_release) as listener:
	listener.join()

