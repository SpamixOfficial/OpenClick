import argparse
from colorama import Fore, Back, init
init(autoreset=True)
colors = dict(Fore.__dict__.items())
nocolors = ["BLACK", "BLUE", "CYAN", "GREEN", "LIGHTBLACK_EX", "LIGHTBLUE_EX", "LIGHTCYAN_EX", "LIGHTGREEN_EX", 
"LIGHTMAGENTA_EX", "LIGHTRED_EX", "LIGHTWHITE_EX", "LIGHTYELLOW_EX", "MAGENTA", "RED", "RESET", "WHITE", "YELLOW"]
hotkeynames = [
    'alt', 'backspace', 'cmd', 'ctrl', 'delete', 'down', 'end', 'enter',
    'f1', 'f10', 'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18',
    'f19', 'f2', 'f20', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'home',
    ]
parser = argparse.ArgumentParser(description='OpenClick Manager!')
parser.add_argument("--c", "--custom", help="Opens the customization menu", action="store_true")
args = parser.parse_args()

if args.c == True:
	print("Customization Menu")
	print("\r")
	print("	\r Textcolor (--textcolor)")
	print(" \r Color Examples (--colorexamples)")
	print("	\r Key (--key)")
	print("\r Exit (--exit)")

	while True:
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
			choose_color = input("$\"TextColor\">").lower()

			if choose_color == "black":
				print("Color \"Black\" was selected!")
				with open('settings.txt', 'r', encoding='utf-8') as file:
					data = file.readlines()

				print(data)
				data[0] = "BLACK\n"

				with open('settings.txt', 'w', encoding='utf-8') as file:
					file.writelines(data)

			elif choose_color == "blue":
				print("Color \"Blue\" was selected!")
				with open('settings.txt', 'r', encoding='utf-8') as file:
					data = file.readlines()

				print(data)
				data[0] = "BLUE\n"

				with open('settings.txt', 'w', encoding='utf-8') as file:
					file.writelines(data)

			elif choose_color == "cyan":
				print("Color \"Cyan\" was selected!")
				with open('settings.txt', 'r', encoding='utf-8') as file:
					data = file.readlines()

				print(data)
				data[0] = "CYAN\n"

				with open('settings.txt', 'w', encoding='utf-8') as file:
					file.writelines(data)

			elif choose_color == "green":
				print("Color \"Green\" was selected!")
				with open('settings.txt', 'r', encoding='utf-8') as file:
					data = file.readlines()

				print(data)
				data[0] = "GREEN\n"

				with open('settings.txt', 'w', encoding='utf-8') as file:
					file.writelines(data)

			elif choose_color == "lightblack_ex":
				print("Color \"Lightblack_EX\" was selected!")
				with open('settings.txt', 'r', encoding='utf-8') as file:
					data = file.readlines()

				print(data)
				data[0] = "LIGHTBLACK\n"

				with open('settings.txt', 'w', encoding='utf-8') as file:
					file.writelines(data)

			elif choose_color == "lightblue_ex":
				print("Color \"Lightblue_EX\" was selected!")
				with open('settings.txt', 'r', encoding='utf-8') as file:
					data = file.readlines()

				print(data)
				data[0] = "LIGHTBLUE\n"

				with open('settings.txt', 'w', encoding='utf-8') as file:
					file.writelines(data)

			elif choose_color == "lightcyan_ex":
				print("Color \"Lightcyan_EX\" was selected!")
				with open('settings.txt', 'r', encoding='utf-8') as file:
					data = file.readlines()

				print(data)
				data[0] = "LIGHTCYAN\n"

				with open('settings.txt', 'w', encoding='utf-8') as file:
					file.writelines(data)

			elif choose_color == "lightgreen_ex":
				print("Color \"Lightgreen_EX\" was selected!")
				with open('settings.txt', 'r', encoding='utf-8') as file:
					data = file.readlines()

				print(data)
				data[0] = "LIGHTGREEN\n"

				with open('settings.txt', 'w', encoding='utf-8') as file:
					file.writelines(data)

			elif choose_color == "lightmagenta_ex":
				print("Color \"Lightmagenta_EX\" was selected!")
				with open('settings.txt', 'r', encoding='utf-8') as file:
					data = file.readlines()

				print(data)
				data[0] = "LIGHTMAGENTA\n"

				with open('settings.txt', 'w', encoding='utf-8') as file:
					file.writelines(data)

			elif choose_color == "lightred_ex":
				print("Color \"Lightred_EX\" was selected!")
				with open('settings.txt', 'r', encoding='utf-8') as file:
					data = file.readlines()

				print(data)
				data[0] = "LIGHTRED\n"

				with open('settings.txt', 'w', encoding='utf-8') as file:
					file.writelines(data)

			elif choose_color == "lightwhite_ex":
				print("Color \"Lightwhite_EX\" was selected!")
				with open('settings.txt', 'r', encoding='utf-8') as file:
					data = file.readlines()

				print(data)
				data[0] = "LIGHTWHITE\n"

				with open('settings.txt', 'w', encoding='utf-8') as file:
					file.writelines(data)

			elif choose_color == "lightyellow_ex":
				print("Color \"Lightyellow_EX\" was selected!")
				with open('settings.txt', 'r', encoding='utf-8') as file:
					data = file.readlines()

				print(data)
				data[0] = "LIGHTYELLOW\n"

				with open('settings.txt', 'w', encoding='utf-8') as file:
					file.writelines(data)
			elif choose_color == "--exit":
				break

			elif choose_color == "magenta":
				print("Color \"Magenta\" was selected!")
				with open('settings.txt', 'r', encoding='utf-8') as file:
					data = file.readlines()

				print(data)
				data[0] = "MAGENTA\n"

				with open('settings.txt', 'w', encoding='utf-8') as file:
					file.writelines(data)

			elif choose_color == "red":
				print("Color \"Red\" was selected!")
				with open('settings.txt', 'r', encoding='utf-8') as file:
					data = file.readlines()

				print(data)
				data[0] = "RED\n"

				with open('settings.txt', 'w', encoding='utf-8') as file:
					file.writelines(data)

			elif choose_color == "white":
				print("Color \"White\" was selected!")
				with open('settings.txt', 'r', encoding='utf-8') as file:
					data = file.readlines()

				print(data)
				data[0] = "WHITE\n"

				with open('settings.txt', 'w', encoding='utf-8') as file:
					file.writelines(data)

			elif choose_color == "yellow":
				print("Color \"Yellow\" was selected!")
				with open('settings.txt', 'r', encoding='utf-8') as file:
					data = file.readlines()

				print(data)
				data[0] = "YELLOW\n"

				with open('settings.txt', 'w', encoding='utf-8') as file:
					file.writelines(data)

		elif menuinput == "--key":
			for key in hotkeynames:
				print(key)
			print("\n Choose a key!")
			choose_key = input("$\"Key\">").lower()

			if choose_key == "f1":
				print("Key \"f1\" was selected!")
				with open('settings.txt', 'r', encoding='utf-8') as file:
					data = file.readlines()

				print(data)
				data[2] = "f1\n"

				with open('settings.txt', 'w', encoding='utf-8') as file:
					file.writelines(data)
			elif choose_key == "f2":
				print("Key \"f2\" was selected!")
				with open('settings.txt', 'r', encoding='utf-8') as file:
					data = file.readlines()

				print(data)
				data[2] = "f2\n"

				with open('settings.txt', 'w', encoding='utf-8') as file:
					file.writelines(data)
		elif menuinput == "--exit":
			break