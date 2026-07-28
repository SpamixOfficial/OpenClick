"""
OpenClick Manager (Module Edition)

Interactive menu for customizing settings.json: text color, hotkeys,
constant-click delay, and a debug toggle.
"""

import argparse
import json

from colorama import Back, Fore, init

init(autoreset=True)

SETTINGS_FILE = "settings.json"

ALL_COLORS = dict(Fore.__dict__.items())
VALID_COLORS = [
    "BLACK", "BLUE", "CYAN", "GREEN", "LIGHTBLACK_EX", "LIGHTBLUE_EX",
    "LIGHTCYAN_EX", "LIGHTGREEN_EX", "LIGHTMAGENTA_EX", "LIGHTRED_EX",
    "LIGHTWHITE_EX", "LIGHTYELLOW_EX", "MAGENTA", "RED", "WHITE", "YELLOW",
]
HOTKEY_NAMES = ["f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9"]


def load_settings():
    with open(SETTINGS_FILE) as f:
        return json.load(f)


def save_settings(data):
    with open(SETTINGS_FILE, "w") as f:
        json.dump(data, f, indent=4)


def invalid(command):
    print(Back.BLACK + Fore.LIGHTWHITE_EX + f'Invalid command: "{command}" is not a command.')


def customization_menu(data):
    while True:
        print("Customization Menu\n")
        print("\r Textcolor (--textcolor)")
        print(" \r Color Examples (--colorexamples)")
        print("\r Key (--key)")
        print("\r Constant Key (--ckey)")
        print("\r Constant Click Delay (--cdelay)")
        print("\r Explainer (--help) (This one explains all settings!)")
        print("\r Exit (--exit)")

        choice = input("$>").lower()

        if choice == "--colorexamples":
            print("Here are the colors!")
            for name in ALL_COLORS:
                print(ALL_COLORS[name] + name)
            print()

        elif choice == "--textcolor":
            for name in VALID_COLORS:
                print(name)
            chosen = input('\nChoose a color!\n$"TextColor">').upper()
            if chosen in VALID_COLORS:
                data["textcolor"] = chosen
            else:
                invalid(chosen)

        elif choice == "--key":
            for key in HOTKEY_NAMES:
                print(key)
            chosen = input('\nChoose a key!\n$"Key">').lower()
            if chosen in HOTKEY_NAMES:
                data["hotkey"] = chosen
            else:
                invalid(chosen)

        elif choice == "--ckey":
            for key in HOTKEY_NAMES:
                print(key)
            chosen = input('\nChoose a key!\n$"Key">').lower()
            if chosen in HOTKEY_NAMES:
                data["constantkey"] = chosen
            else:
                print("The key you specified either doesn't exist or it isn't supported at the time.")

        elif choice == "--cdelay":
            chosen = input('\nChoose a value!\n$"CDelay">')
            try:
                data["constantclickdelay"] = float(chosen)
            except ValueError:
                print("You must input a number.")

        elif choice == "--help":
            print("\r Textcolor (--textcolor) - The color of the text you see in the terminal.")
            print("\r Color Examples (--colorexamples) - Shows you the colors you can choose from.")
            print('\r Key (--key) - The key for the "Normal" mode.')
            print('\r Constant Key (--ckey) - The key for the "Constant" mode.')
            print('\r Constant Click Delay (--cdelay) - The delay for the "Constant" mode.')
            print("\r Explainer (--help) (This one explains all settings!)")
            print("\r Exit (--exit)")

        elif choice == "--exit":
            break

        else:
            invalid(choice)

        save_settings(data)


def debug_menu(data):
    while True:
        print("Debug Menu")
        print("\rdebugmode (--d f/t)")
        print("\rexit (--exit)")
        choice = input("$>").lower()

        if choice == "--d f":
            data["debugmode"] = False
        elif choice == "--d t":
            data["debugmode"] = True
        elif choice == "--exit":
            break
        else:
            invalid(choice)

        save_settings(data)


def main():
    parser = argparse.ArgumentParser(description="OpenClick Manager")
    parser.add_argument("--c", "--custom", dest="custom", help="Opens the customization menu", action="store_true")
    parser.add_argument("-deb", dest="debug", help="Debug", action="store_true")
    args = parser.parse_args()

    data = load_settings()

    if args.custom:
        customization_menu(data)
    elif args.debug:
        debug_menu(data)
    else:
        print("Use python manager.py -h for help.")


if __name__ == "__main__":
    main()