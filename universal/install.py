"""
OpenClick installer (Module Edition)

Checks whether the required modules are installed (offering to pip-install
any that are missing), detects whether root is required for Wayland, and
marks settings.json as ready to run.
"""

import json
import os
import platform
import subprocess
import sys

SETTINGS_FILE = "settings.json"

# Accepted "yes" answers - matches the project's convention of treating a
# bare Enter as a yes.
YES_INPUTS = {"yes", "y", "ye", ""}


def load_settings():
    with open(SETTINGS_FILE) as f:
        return json.load(f)


def save_settings(data):
    with open(SETTINGS_FILE, "w") as f:
        json.dump(data, f, indent=4)


def confirm(prompt):
    return input(prompt).strip().lower() in YES_INPUTS


def check_wayland_sudo(data):
    """On Linux + Wayland, OpenClick needs root. Record and enforce that now."""
    if platform.system() != "Linux":
        return
    if not os.environ.get("WAYLAND_DISPLAY"):
        return

    data["sudo"] = True
    save_settings(data)

    if os.geteuid() != 0:
        print("Sudo is needed to run OpenClick Module Edition using Wayland.")
        print("\n---Try again with sudo---")
        sys.exit(1)


def ensure_module(module_name, pip_name=None):
    """Check whether a module is importable; offer to pip install it if missing."""
    pip_name = pip_name or module_name
    try:
        __import__(module_name)
        print(f'Module "{module_name}" was found!')
        return True
    except ModuleNotFoundError:
        print(f'The module named "{module_name}" wasn\'t found! Do you want to install it? ([Y]es/[n]o)')
        if confirm(""):
            subprocess.run([sys.executable, "-m", "pip", "install", pip_name])
            return True
        print("Then you need to install it. Read the instructions on the github page or read the README.md!")
        return False


def main():
    data = load_settings()

    check_wayland_sudo(data)

    print("Checking for the modules on your system...")
    have_colorama = ensure_module("colorama")
    have_pynput = ensure_module("pynput")

    if have_colorama and have_pynput:
        data["firststartup"] = True
        save_settings(data)
        print(
            "You are ready to go!\n\n"
            "Please make sure you have tKinter installed manually. If it isn't installed then "
            "you can read the readme for examples on how to install it!\n"
            "Read the docs over at https://github.com/SpamixOfficial/OpenClick/blob/main/README.md "
            "for more information!"
        )
    else:
        print(
            "Sorry, but one or both of the required modules weren't found.\n"
            "Read the instructions for help on how to install them!"
        )
        sys.exit(1)


if __name__ == "__main__":
    main()