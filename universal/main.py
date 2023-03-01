# Startup Check
debugswitch = 1
import os, time, re, argparse, subprocess, threading, json, requests
parser = argparse.ArgumentParser(description="OpenClick Module Edition Help")
parser.add_argument("-cd", help="Constant Click Delay", action="store", type=float)
args = parser.parse_args()
firststartup = False
# Most important settings checking
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
	if data["sudo"] == True:
		print("Sudo is needed to run OpenClick Module Edition using Wayland.")
		print("\n---Try again with sudo---")
		quit()
## --------------------------------------------------------------- ##
# Settings Check
from pynput.keyboard import Key, Listener
from pynput.mouse import Button, Controller
from colorama import Fore, Back, init
color = Fore.RED
def ucheck():
	# opening settings.json file
	jsfile = json.load(open("settings.json"))
	##

	# getting new release json
	response = requests.get("https://api.github.com/repos/SpamixOfficial/OpenClick/releases/latest")
	respdata = response.json()
	##

	# getting new release info
	newid = respdata["id"]

	if not str(jsfile["release"]) == str(newid):
		print(Fore.YELLOW + "New release available to download! " + Fore.RED + "\nConsider updating using the \"update.py\" file since we dont support older versions of our software!")
	else:
		print("Version is up to date!")

if data["autoupdate"] == True:
	ucheck()

if True:
	# settingsread = open("settings.txt", 'r+').read()
	# colorscheck = ["BLACK", "BLUE", "CYAN", "GREEN", "LIGHTBLACK_EX", "LIGHTBLUE_EX", "LIGHTCYAN_EX", "LIGHTGREEN_EX", "LIGHTMAGENTA_EX", "LIGHTRED_EX", "LIGHTWHITE_EX", "LIGHTYELLOW_EX", "MAGENTA", "RED", "WHITE", "YELLOW"]
	# word_exp='|'.join(colorscheck)
	# fullcolorcheck = re.findall(word_exp, open("settings.txt", 'r+').read())

	with open('settings.json') as f:
		data = json.load(f)
		fullcolorcheck = (data['textcolor'])

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

contantClickDelay = args.cd
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
	print("\r" + str(fullcolorcheck) + str(hotkey))
for a in "Hello and welcome to":
	time.sleep(0.01)
	print(color + a, end="")
time.sleep(0.06)
for a in "...":
	print(color + a, end="")
	time.sleep(0.2)

os.system('cls' if os.name == 'nt' else 'clear')
for char in openlogo:
	print(color + char, end="")
	time.sleep(0.0003)

## Start of clicker code
shouldClick = False # controlls the constantclick

# this is Flag class handling constantclick delay
#class AutoDelay(Flag):
#	shortFlag="-cd"
#	longFlag="-constantClickDelay"
#	description='sets the constantclick delay (default 0.1 secounds between clicks)'
#	def onCall(self,args):
#		global contantClickDelay
#		contantClickDelay = float(args[0])

#a = FlagManager([AutoDelay()])
#a.check()


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

