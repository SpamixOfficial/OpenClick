import argparse
from colorama import Fore, Back, init
init(autoreset=True)
colors = dict(Fore.__dict__.items())
nocolors = ["BLACK", "BLUE", "CYAN", "GREEN", "LIGHTBLACK_EX", "LIGHTBLUE_EX", "LIGHTCYAN_EX", "LIGHTGREEN_EX",
"LIGHTMAGENTA_EX", "LIGHTRED_EX", "LIGHTWHITE_EX", "LIGHTYELLOW_EX", "MAGENTA", "RED", "RESET", "WHITE", "YELLOW"]
hotkeynames = [
    'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9'
    ]
parser = argparse.ArgumentParser(description='OpenClick Manager')
parser.add_argument("--c", "--custom", help="Opens the customization menu", action="store_true")
parser.add_argument("-deb", help="Debug", action="store_true")
args = parser.parse_args()

import json
# load the json file and store it as data
with open('settings.json') as f:
	data = json.load(f)

if args.c == True:
	while True:
		print("Customization Menu")
		print("\r")
		print("	\r Textcolor (--textcolor)")
		print(" \r Color Examples (--colorexamples)")
		print("	\r Key (--key)")
		print("	\r Constant Key (--ckey)")
		print("\r Exit (--exit)")

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
				print(Back.BLACK + Fore.LIGHTWHITE_EX + "Invalid command: \"" + menuinput + "\" is not a command.")

		elif menuinput == "--exit":
			break
		# saves the settings
		with open('settings.json', 'w') as outfile:
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
		with open('settings.json', 'w') as outfile:
				json.dump(data, outfile,indent=4)
else:
	print("Use python manager.py -h for help.")

