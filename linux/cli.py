#!/usr/bin/env python3
"""
OpenClick Full Edition (installed as the `openclick` command on Linux)

Combines the autoclicker (see main.py) with the settings customization
menu (see manager.py) into a single script, reading/writing
/etc/openclick/settings.json.
"""

import argparse
import json
import os
import threading
import time

from colorama import Back, Fore, init
from pynput.keyboard import Key, Listener
from pynput.mouse import Button, Controller

SETTINGS_FILE = "/etc/openclick/settings.json"

COLOR_MAP = {
    "BLACK": Fore.BLACK, "BLUE": Fore.BLUE, "CYAN": Fore.CYAN,
    "GREEN": Fore.GREEN, "MAGENTA": Fore.MAGENTA, "RED": Fore.RED,
    "WHITE": Fore.WHITE, "YELLOW": Fore.YELLOW,
    "LIGHTBLACK_EX": Fore.LIGHTBLACK_EX, "LIGHTBLUE_EX": Fore.LIGHTBLUE_EX,
    "LIGHTCYAN_EX": Fore.LIGHTCYAN_EX, "LIGHTGREEN_EX": Fore.LIGHTGREEN_EX,
    "LIGHTMAGENTA_EX": Fore.LIGHTMAGENTA_EX, "LIGHTRED_EX": Fore.LIGHTRED_EX,
    "LIGHTWHITE_EX": Fore.LIGHTWHITE_EX, "LIGHTYELLOW_EX": Fore.LIGHTYELLOW_EX,
}
HOTKEY_NAMES = ["f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9"]

OPEN_LOGO = r"""
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

                        SpamixOfficial & Moita 2026
"""


def load_settings():
    with open(SETTINGS_FILE) as f:
        return json.load(f)


def save_settings(data):
    with open(SETTINGS_FILE, "w") as f:
        json.dump(data, f, indent=4)


def resolve_color(name):
    return COLOR_MAP.get(name, Fore.RED)


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
            for name, code in COLOR_MAP.items():
                print(code + name)
            print()

        elif choice == "--textcolor":
            for name in COLOR_MAP:
                print(name)
            chosen = input('\nChoose a color!\n$"TextColor">').upper()
            if chosen in COLOR_MAP:
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


def print_intro(color):
    for ch in "Hello and welcome to":
        time.sleep(0.01)
        print(color + ch, end="")
    time.sleep(0.06)
    for ch in "...":
        print(color + ch, end="")
        time.sleep(0.2)

    os.system("clear")
    for ch in OPEN_LOGO:
        print(color + ch, end="")
        time.sleep(0.0003)


class AutoClicker:
    def __init__(self, settings, click_delay):
        self.mouse = Controller()
        self.click_delay = click_delay
        self.hotkey = "Key." + settings["hotkey"]
        self.constant_key = "Key." + settings["constantkey"]
        self.debugmode = settings["debugmode"]
        self.should_click = False

    def start_constant_click_thread(self):
        threading.Thread(target=self._constant_click_loop, daemon=True).start()

    def _constant_click_loop(self):
        while self.should_click:
            self.mouse.press(Button.left)
            self.mouse.release(Button.left)
            time.sleep(self.click_delay)

    def on_press(self, key):
        if str(key) == self.constant_key:
            self.should_click = not self.should_click
            if self.should_click:
                self.start_constant_click_thread()

        if str(key) == self.hotkey:
            if self.debugmode:
                print(key)
            self.mouse.press(Button.left)
            self.mouse.release(Button.left)

        if key == Key.delete:
            self.debugmode = not self.debugmode
            print(self.debugmode)

    def on_release(self, key):
        if key == Key.esc:
            self.should_click = False
            return False


def run_clicker(settings, click_delay):
    color = resolve_color(settings["textcolor"])

    if settings["debugmode"]:
        print("Debugmode")
        print("\r" + settings["textcolor"] + " Key." + settings["hotkey"])

    print_intro(color)

    clicker = AutoClicker(settings, click_delay)

    print(color + "Controls: \n" +
          clicker.hotkey + " to click (hold to click!) \n" +
          clicker.constant_key + " to click constantly (toggle on/off by clicking the key!)\n"
          "Esc to exit!")

    with Listener(on_press=clicker.on_press, on_release=clicker.on_release) as listener:
        listener.join()


def main():
    parser = argparse.ArgumentParser(description="OpenClick Full Edition Help")
    parser.add_argument("--c", "--custom", dest="custom", help="Opens the customization menu", action="store_true")
    parser.add_argument("--deb", dest="debug", help="Debug", action="store_true")
    parser.add_argument("-cd", help="Constant Click Delay", action="store", type=float)
    args = parser.parse_args()

    settings = load_settings()

    if not settings["firststartup"]:
        print("Run the installation script before running the main program!")
        raise SystemExit(1)

    init(autoreset=True)

    if args.custom:
        customization_menu(settings)

    if args.debug:
        debug_menu(settings)

    click_delay = args.cd if args.cd is not None else settings["constantclickdelay"]
    run_clicker(settings, click_delay)


if __name__ == "__main__":
    main()