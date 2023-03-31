## Credits
Thanks to the following persons for commiting to the project!

* spynetS (Alfred Roos, https://github.com/spynetS)

# OpenClick
[![GitHub license](https://img.shields.io/github/license/SpamixOfficial/Openclick.svg)](https://github.com/SpamixOfficial/Openclick/blob/master/LICENSE)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/SpamixOfficial/Openclick/graphs/commit-activity)
[![GitHub release](https://img.shields.io/github/release/SpamixOfficial/Openclick.svg)](https://GitHub.com/SpamixOfficial/Openclick/releases/)

Welcome to OpenClick! 

OpenClick is an open source autoclicker for Debian and Arch based systems!
Currently the only way you can run this autoclicker on Windows is by running the Module Edition (I'm going to fix this).

# LOOK HERE WAYLAND USERS!
The only way to run OpenClick on Wayland is by using Sudo. I've implemented a "feature" that checks for Wayland, and notifies you if you need to use sudo.

There are also a limited amount of application that can use openclick on wayland. **The only applications that can use Openclick on Wayland is the applications running xwayland**

# The 2 different editions (READ ME!)
There are 2 different editions/versions of this software. 

Either you use the "Module" Edition, which consists of the install.py, the main.py and the manager.py file, or you run the "Full Edition". The "Module" Edition is cross-platform, since it works on Linux and Windows!

The "Full" Edition is the 2 files (main.py and manager.py) made into one file that's also installed as a command on your system. The "Full" Edition isn't cross-platform, it does not work on windows. 

A fix is coming!

There are guides for both editions.


# Intro
So, what is an autoclicker?
An autoclicker is an application or an automatisation that clicks automatically.
Many users would probably say - "but what about xdotool?".
Of course you could use xdotool, but then you would not have any control over when it should click, and when it should not! This is basically an easy to use autoclicker and tool written in python!

Have fun :D


# Before you start...
Make sure you have python installed! Most linux distros comes with python out of the box, but check so its installed just in case it isn't!
Also make sure you have "pip" installed! Most linux distros comes with pip out of the box, but once again, check so its installed just in case it isn't!

## !IMPORTANT!
And lastly, make sure you have tKinter installed. It comes prebundled with python, though sometimes the module named "pynput" needs a manual installation of tKinter to work!
Here is how to install it. If you can't find your distro's way to install it here, then search the internet.

**For Debian/Ubuntu based distros**
  ```
  sudo apt-get install python-tk
  ```
**For Arch Linux based distros**
  ```
  sudo pacman -S tk
  ```

# How to install

**For Fedora based distros**
  ```
  sudo dnf install python3-tkinter
  ```

## Fedora

On some distros the python3-devel package is not installed by default, and this package is needed for many python modules, which causes the installation to fail if the python3-devel package isn't installed. This issue can be resolved though by installing the python3-devel package.

**devel package**
```
sudo dnf install python3-devel
```

# How to install Module Edition
**Make sure you are in the right directory!**

## How to install
**(Wayland users use sudo)**

Step 1:
  Run the installation script!
  ```
  python3 install.py
  ```
Step 2:
  When you've gotten the message:
  > You are ready to go!
  
  you can run the main.py file using:
  ```
  python3 main.py
  ```
  You are done!
## How to use
**(Wayland users use sudo)**

Use the command 
  ```
  python3 main.py
  ```
while in the correct folder to run the script!
Use the command 
  ```
  python3 manager.py --c
  ```
while in the correct folder to open up the customization menu! (Tip! Use -h instead of --c to get the help menu instead!)
If you want to customize the constant click delay, then use the command 
  ```
  python3 main.py -cd [value] 
  ```
The default value is 0,5 seconds!


# How to install Full Edition
## How to install

**Make sure you are in the right directory!**

**You will need sudo access for this**

Step 1:
  Install jq using your package manager.

  For Ubuntu/Debian based distros.
  ```
  sudo apt-get install jq
  ```
  For Arch based distros:
  ```
  sudo pacman -S jq
  ```
  For Red-Hat based distros:
  ```
  sudo dnf install jq
  ```
Step 2:
  Chmod the scripts and run the installer.
  ```
  chmod +x install.sh && chmod +x uninstall.sh && ./install.sh
  ```
Step 3:
  When you get the message;
  > Installation Success!
  
  you can run the software using the command:
  ```
  openclick
  ```
  You are done!
## How to use
Use this command to run the software.
  ```
  openclick
  ```

Use this command to open up the customization menu.
  ```
  openclick --c
  ```
(Tip! Use -h instead of --c to get the help menu instead!)
If you want to customize the constant click delay, then use the command 
  ```
  openclick -cd [value] 
  ```
The default value is 0,5 seconds!

If you want to update manually:
```
openclick -u
```
If you want to turn off auto updates:
```
openclick -u auto=False
```
If you want to turn on auto updates:
```
openclick -u auto=True
```

## IMPORTANT
I would advise you to turn auto updates off if you dont have a stable internet connection.

# Extra info
If you find any bugs, report them!
The project is written in python.
And lastly, if you find something you feel like can be improved, changed or just something you want to add, suggest it in "ideas" (https://github.com/SpamixOfficial/OpenClick/discussions/1)


# DISCLAIMER

It doesn't work on MacOS and Fedora because of issues regarding a module named pynput!


# To-do List!
- [X] Add customization
- [X] Add constant mode
- [X] Partial Add Windows support
- [X] Add auto updates
- [X] Add auto updates for all editions
- [ ] Add Windows support
- [ ] Create aur package
- [ ] (Maybe) Create deb package
- [ ] Something you can suggest in "ideas" (https://github.com/SpamixOfficial/OpenClick/discussions/1)

[![ForTheBadge built-with-swag](http://ForTheBadge.com/images/badges/built-with-swag.svg)](https://GitHub.com/SpamixOfficial/)
