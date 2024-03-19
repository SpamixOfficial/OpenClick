#!/usr/bin/env python3
import requests, argparse, os, time, re, threading, json, zipfile, glob, getpass, subprocess, shutil, random

settingsfile = "/etc/openclick/settings.json"

# Startup Check
firststartup = False
if True:
	#settingsread = open("settings.txt", 'r+').read()
	#rawstartcheck = ["firststartup=true", "firststartup=false"]
	#word_exp='|'.join(rawstartcheck)
	#fullstartupcheck = re.findall(word_exp, open("settings.txt", 'r+').read())
	with open(settingsfile) as f:
		data = json.load(f)
		autoup = (data['autoupdate'])

	fullstartupcheck = (data['firststartup'])

	if fullstartupcheck == True:
		firststartup = True
	elif fullstartupcheck == False:
		firststartup = False
		print("Run the installation script before running the main program!")
		quit()

##############

from colorama import Fore, Back, init
from pynput.keyboard import Key, Listener
from pynput.mouse import Button, Controller

global shouldClick	
init(autoreset=True)
colors = dict(Fore.__dict__.items())
nocolors = ["BLACK", "BLUE", "CYAN", "GREEN", "LIGHTBLACK_EX", "LIGHTBLUE_EX", "LIGHTCYAN_EX", "LIGHTGREEN_EX",
"LIGHTMAGENTA_EX", "LIGHTRED_EX", "LIGHTWHITE_EX", "LIGHTYELLOW_EX", "MAGENTA", "RED", "RESET", "WHITE", "YELLOW"]
hotkeynames = [
	'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9'
	]
parser = argparse.ArgumentParser(description='OpenClick Full Edition Help')
parser.add_argument("--c", "--custom", help="Opens the customization menu", action="store_true")
parser.add_argument("--deb", help="Debug", action="store_true")
parser.add_argument("-cd", help="Constant Click Delay", action="store", type=float)
parser.add_argument("-u", help="Handle update settings (auto=True/False, update)", nargs='?', const='update')
parser.add_argument("-mb", help="Choose mouse button (left, right, middle)", nargs="?", const="left")
args = parser.parse_args()

import json
# load the json file and store it as data
with open(settingsfile) as f:
	data = json.load(f)

# Manually update argument
match args.u:
	case 'auto=True':
		data['autoupdate']=True
		with open(settingsfile, 'w') as outfile:
			json.dump(data, outfile,indent=4)
		print("Successfully updated settings.")
		quit
	case 'auto=False':
		data['autoupdate']=False
		with open(settingsfile, 'w') as outfile:
			json.dump(data, outfile,indent=4)
		print("Successfully updated settings.")
		quit
	case 'update':
		# opening settings.json file
		jsfile = open("settings.json")
		##

		# getting new release json
		response = requests.get("https://api.github.com/repos/SpamixOfficial/OpenClick/releases/latest")
		respdata = response.json()
		##

		# getting new release info
		newid = respdata["id"]
		tag = respdata["tag_name"]
		##

		# local data
		jsdata = json.load(jsfile)

		locdata = jsdata["release"]
		##

		# url stuff
		downurl = respdata["zipball_url"]

		download = requests.get(downurl)
		##

		# filename and dir setting
		downdir = "/tmp/"
		downname = "openclick-" + tag + "-release.zip"
		finalfile = os.path.join(downdir, downname)
		##
		print("Newest release: " + str(newid) + "\nLocal release: " + str(locdata))
		updateinp = input("\nDo you want to update? y/n: ").lower()   

		if updateinp == "y":
			# downloading and renaming zip file
			with open(finalfile, 'wb') as fd:
				print("Downloading...")
				fd.write(download.content)
			# outputing into directory and removing zip file
			with zipfile.ZipFile(finalfile, 'r') as dezip:
				print("Extracting into folder...")
				dezip.extractall(path="/tmp/openclick")
			os.remove(finalfile)

			# scanning folder name inside directory
			dowrelname = os.listdir("/tmp/openclick")
			dowdirname = " ".join(str(x) for x in dowrelname)
			print(dowdirname)

			# run installation script
			print("Installing...")
			installp = subprocess.run("/tmp/openclick/" + dowdirname + "/install.sh")

			if installp.returncode != 0:
				print("Installation failed. \nRemoving temporary files and exiting.")
				# remove all files if installation script fails
				shutil.rmtree("/tmp/openclick")
				quit()
			print("Update was successful! Removing update files...")
			# remove directory when done
			shutil.rmtree("/tmp/openclick")
			print("Exiting...")
			quit()
		else:
			quit()			
		#########################################)
	# Automatically update

if autoup == True:
	# opening settings.json file
	jsfile = open("settings.json")
	##

	# getting new release json
	response = requests.get("https://api.github.com/repos/SpamixOfficial/OpenClick/releases/latest")
	respdata = response.json()
	##

	# getting new release info
	newid = respdata["id"]
	tag = respdata["tag_name"]
	##

	# local data
	jsdata = json.load(jsfile)

	locdata = jsdata["release"]
	##

	# url stuff
	downurl = respdata["zipball_url"]

	download = requests.get(downurl)
	##

	# filename and dir setting
	downdir = "/tmp/"
	downname = "openclick-" + tag + "-release.zip"
	finalfile = os.path.join(downdir, downname)
	##
	if not str(newid) == str(locdata):
		print("Newest release: " + str(newid) + "\nLocal release: " + str(locdata))
		updateinp = input("\nDo you want to update? y/n: ").lower()   

		if updateinp == "y":
			# downloading and renaming zip file
			with open(finalfile, 'wb') as fd:
				print("Downloading...")
				fd.write(download.content)
			# outputing into directory and removing zip file
			with zipfile.ZipFile(finalfile, 'r') as dezip:
				print("Extracting into folder...")
				dezip.extractall(path="/tmp/openclick")
			os.remove(finalfile)

			# scanning folder name inside directory
			dowrelname = os.listdir("/tmp/openclick")
			dowdirname = " ".join(str(x) for x in dowrelname)
			print(dowdirname)

			# run installation script
			print("Installing...")
			installp = subprocess.run("/tmp/openclick/" + dowdirname + "/install.sh")

			if installp.returncode != 0:
				print("Installation failed. \nRemoving temporary files and exiting.")
				# remove all files if installation script fails
				shutil.rmtree("/tmp/openclick")
				quit()
			print("Update was successful! Removing update files...")
			# remove directory when done
			shutil.rmtree("/tmp/openclick")
			print("Exiting...")
			quit()
		else:
			print("You can update any time by using \"openclick -u\".")
	else:
		print("Already newest release.")
else:
	print("Autoupdates are turned off.")

########################################


if args.c == True:
	while True:
		menu_str = """
Customization Menu
\r
\r Textcolor (--textcolor)
\r Color Examples (--colorexamples)
\r Key (--key)
\r Constant Key (--ckey)
\r Random Delay (--rdelay)
\r Constant Click Delay (--cdelay)
\r Explainer (--help) (This one explains all settings!)
\r Exit (--exit)
"""
		print(menu_str)

		menuinput = input("$>").lower()

		if menuinput == "--colorexamples":
			print("Here are the colors!")
			for color in colors.keys():
				print(colors[color] + f"{color}")

			print("\n")

		elif menuinput == "--textcolor":

			for color in nocolors:
				print(color)

			print("\nChoose a color!")
			choose_color = input("$\"TextColor\">").upper()
			# check if the chosen color is in the color list and if so set the textcolor to that value
			if choose_color in nocolors:
				data['textcolor']=choose_color
			else:
				print(Back.BLACK + Fore.LIGHTWHITE_EX + "Invalid command: \"" + choose_color + "\" is not a valid color.")
		elif menuinput == "--key":
			for key in hotkeynames:
				print(key)
			print("\n Choose a key!")
			choose_key = input("$\"Key\">").lower()

			if choose_key in hotkeynames: # checks if the choosen key is in the key list
				data['hotkey']=choose_key
			else:
				print(Back.BLACK + Fore.LIGHTWHITE_EX + "Invalid command: \"" + menuinput + "\" is not a command.")
		elif menuinput == "--ckey":
			for key in hotkeynames:
				print(key)
			print("\n Choose a key!")
			choose_key = input("$\"Key\">").lower()

			if choose_key in hotkeynames: # checks if the choosen key is in the key list
				data['constantkey']=choose_key
			else:
				print("The key you specified either doesn't exist or it isn't supported at the time.")
		
		
		elif menuinput == "--rdelay":
			data['randomdelay'] = True

		elif menuinput == "--cdelay":
			print("\nChoose a value!")
			choose_key = input("$\"CDelay\">")
		
			try:
				cdelay = float(choose_key)
				data['constantclickdelay'] = float(choose_key)
				data['randomdelay'] = False
			except ValueError:
				print("You must input a number.")

		elif menuinput == "--help":
			print(menu_str)

		elif menuinput == "--exit":
			break

		else:
			print(Back.BLACK + Fore.LIGHTWHITE_EX + "Invalid command: \"" + menuinput + "\" is not a command.")
		
		# saves the settings
		with open(settingsfile, 'w') as outfile:
				json.dump(data, outfile,indent=4)

elif args.deb == True:
	while True:
		print("Debug Menu")
		print("\rdebugmode (--d f/t)")
		print("\rexit (--exit")
		debinput = input("$>").lower()
		if debinput == "--d f":
			data['debugmode']=False
		elif debinput == "--d t":
			data['debugmode']=True
		elif debinput == "--exit":
			break
		else:
			print(Back.BLACK + Fore.LIGHTWHITE_EX + "Invalid command: \"" + debinput + "\" is not a command.")
		with open(settingsfile, 'w') as outfile:
				json.dump(data, outfile,indent=4)

	## --------------------------------------------------------------- ##
	# Settings Check
	color = Fore.RED



if True:
	# settingsread = open("settings.txt", 'r+').read()
	# colorscheck = ["BLACK", "BLUE", "CYAN", "GREEN", "LIGHTBLACK_EX", "LIGHTBLUE_EX", "LIGHTCYAN_EX", "LIGHTGREEN_EX", "LIGHTMAGENTA_EX", "LIGHTRED_EX", "LIGHTWHITE_EX", "LIGHTYELLOW_EX", "MAGENTA", "RED", "WHITE", "YELLOW"]
	# word_exp='|'.join(colorscheck)
	# fullcolorcheck = re.findall(word_exp, open("settings.txt", 'r+').read())

	with open(settingsfile) as f:
		data = json.load(f)
		fullcolorcheck =  (data['textcolor'])

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
constantClickDelay = 0.1 # the delay between clicks in constantclick


with open(settingsfile) as f:
	data = json.load(f)

	if True:
		hotkey = "Key." + (data['hotkey'])

	if True:
			constantKey =  "Key." + (data['constantkey'])

	if True:
			userandomdelay = (data['randomdelay'])


	#sets the constantclickdelay
	if True:
			constantClickDelay = (data['constantclickdelay'])

	if True:
			debugmode = (data['debugmode'])


			
## --------------------------------------------------------------- ##
# Start of program
if args.cd:
	constantClickDelay = args.cd

if not args.mb == None:
	args.mb = args.mb.lower()
	if args.mb == "left":
		mouse_button = Button.left
	elif args.mb == "right":
		mouse_button = Button.right
	elif args.mb == "middle":
		mouse_button = Button.middle
elif args.mb == None:
	mouse_button = Button.left


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


							SpamixOfficial 2023
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

os.system('cls' if os.name == 'nt' else 'clear')
for char in openlogo:
	print(color + char, end="")
	time.sleep(0.0003)



print(color + "Controls: \n" + str(hotkey) + " to click (hold to click!) \n" + str(constantKey) + " to click constantly (toggle on/off by clicking the key!)\nEsc to exit!")






## Start of clicker code
shouldClick = False # controlls the constantclick


@listener.event
def on_press(key):
	global Key
	global debugmode
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
		mouse.press(mouse_button)
		mouse.release(mouse_button)

	if str(key) == str(Key.delete):
		debugmode = not debugmode #toggles the debugmode
		
@listener.event
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
		mouse.press(mouse_button)
		mouse.release(mouse_button)

		#sleep for either random or set delay
		if userandomdelay:
			time.sleep(random.uniform(0.01, 3))
		else:
			time.sleep(constantClickDelay) #add delay

# Collect events until released
with Listener(
		on_press=on_press,
		on_release=on_release) as listener:
	listener.join()
