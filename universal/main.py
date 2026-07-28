"""
OpenClick Module Edition
A configurable autoclicker controlled via keyboard hotkeys.

Config file: settings.json (must exist in the same directory)
Expected keys:
    firststartup      bool   - must be true, or the program refuses to run
    sudo              bool   - if true, require root (needed for some Wayland setups)
    textcolor         str    - a colorama Fore color name, e.g. "RED"
    hotkey            str    - a pynput Key name (without "Key."), e.g. "f1"
    constantkey       str    - a pynput Key name for the toggle-autoclick key
    constantclickdelay float - seconds between clicks in constant-click mode
    debugmode         bool   - print extra diagnostic info
"""

import os
import time
import json
import argparse
import threading

from pynput.keyboard import Key, Listener
from pynput.mouse import Button, Controller
from colorama import Fore, init

SETTINGS_FILE = "settings.json"

# Maps the plain-text color name in settings.json to a colorama color code.
COLOR_MAP = {
    "BLACK": Fore.BLACK, "BLUE": Fore.BLUE, "CYAN": Fore.CYAN,
    "GREEN": Fore.GREEN, "MAGENTA": Fore.MAGENTA, "RED": Fore.RED,
    "WHITE": Fore.WHITE, "YELLOW": Fore.YELLOW,
    "LIGHTBLACK_EX": Fore.LIGHTBLACK_EX, "LIGHTBLUE_EX": Fore.LIGHTBLUE_EX,
    "LIGHTCYAN_EX": Fore.LIGHTCYAN_EX, "LIGHTGREEN_EX": Fore.LIGHTGREEN_EX,
    "LIGHTMAGENTA_EX": Fore.LIGHTMAGENTA_EX, "LIGHTRED_EX": Fore.LIGHTRED_EX,
    "LIGHTWHITE_EX": Fore.LIGHTWHITE_EX, "LIGHTYELLOW_EX": Fore.LIGHTYELLOW_EX,
}

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


def parse_args():
    """Read command-line flags. -cd overrides the click delay from settings.json."""
    parser = argparse.ArgumentParser(description="OpenClick Module Edition Help")
    parser.add_argument("-cd", help="Constant Click Delay", action="store", type=float)
    return parser.parse_args()


def load_settings():
    """Load settings.json once and return it as a dict."""
    with open(SETTINGS_FILE) as f:
        return json.load(f)


def run_startup_checks(settings):
    """
    Refuse to start unless settings.json marks first-time setup as complete,
    and (if configured) refuse to start without root privileges.
    """
    if not settings["firststartup"]:
        print("Run the installation script before running the main program!")
        raise SystemExit(1)

    if settings.get("sudo") and os.geteuid() != 0:
        print("Sudo is needed to run OpenClick Module Edition using Wayland.")
        print("\n---Try again with sudo---")
        raise SystemExit(1)


def resolve_color(name):
    """Turn the textcolor setting into a colorama code, defaulting to red if unrecognized."""
    return COLOR_MAP.get(name, Fore.RED)


def print_intro(color):
    """Animated greeting text, then clear the screen and print the ASCII logo."""
    for ch in "Hello and welcome to":
        time.sleep(0.01)
        print(color + ch, end="")
    time.sleep(0.06)
    for ch in "...":
        print(color + ch, end="")
        time.sleep(0.2)

    os.system('cls' if os.name == 'nt' else 'clear')
    for ch in OPEN_LOGO:
        print(color + ch, end="")
        time.sleep(0.0003)


class AutoClicker:
    """
    Holds all the runtime state for the clicker: the mouse controller,
    whether constant-click mode is active, and the debug toggle state.
    """

    def __init__(self, settings, click_delay):
        self.mouse = Controller()
        self.settings = settings
        self.click_delay = click_delay
        self.hotkey = "Key." + settings["hotkey"]
        self.constant_key = "Key." + settings["constantkey"]
        self.debugmode = settings["debugmode"]
        self.should_click = False       # whether constant-click mode is currently on
        self._debug_toggle_state = 1    # tracks Key.delete presses to flip debugmode

    def start_constant_click_thread(self):
        thread = threading.Thread(target=self._constant_click_loop, daemon=True)
        thread.start()

    def _constant_click_loop(self):
        """While constant-click mode is on, click repeatedly with the configured delay."""
        while self.should_click:
            self.mouse.press(Button.left)
            self.mouse.release(Button.left)
            time.sleep(self.click_delay)

    def on_press(self, key):
        """
        Handles every key press:
        - constant_key: toggles constant-click mode on/off
        - hotkey: fires a single click (repeats while held, since OS repeats key events)
        - Key.delete: toggles debug mode on/off
        """
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
        """Esc stops constant-click mode and ends the listener."""
        if key == Key.esc:
            self.should_click = False
            return False


def main():
    args = parse_args()
    settings = load_settings()

    run_startup_checks(settings)

    init(autoreset=True)
    color = resolve_color(settings["textcolor"])

    click_delay = args.cd if args.cd is not None else settings["constantclickdelay"]

    if settings["debugmode"]:
        print("Debugmode")
        print("\r" + str(settings["textcolor"]) + "Key." + settings["hotkey"])

    print_intro(color)

    clicker = AutoClicker(settings, click_delay)

    print(color + "Controls: \n" +
          clicker.hotkey + " to click (hold to click!) \n" +
          clicker.constant_key + " to click constantly (toggle on/off by clicking the key!)\n"
          "Esc to exit!")

    with Listener(on_press=clicker.on_press, on_release=clicker.on_release) as listener:
        listener.join()


if __name__ == "__main__":
    main()