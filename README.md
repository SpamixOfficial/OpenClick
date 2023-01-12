## Credits
Thanks to the following persons for commiting to the project!

* spynetS (Alfred Roos, https://github.com/spynetS)


# OpenClick
Welcome to OpenClick! 
OpenClick is an open source autoclicker for Debian and Arch based systems!
Currently it does not work on windows, but a fix is on the way!

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

**For Arch Linux based distros**
  ```
  sudo pacman -S tk
  ```
  
  
# How to install
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
# How to use
Use the command 
  ```
  python3 main.py
  ```
to run the script!
Use the command 
  ```
  python3 manager.py --c
  ```
to open up the customization menu! (Tip! Use -h instead of --c to get the help menu instead!)
If you want to customize the constant click delay, then use the command 
  ```
  python3 main.py -cd [value] 
  ```
The default value is 0,5 seconds!
# Extra info
If you find any bugs, report them!
The project is written in python.
And lastly, if you find something you feel like can be improved, changed or just something you want to add, suggest it in "ideas" (https://github.com/SpamixOfficial/OpenClick/discussions/1)


# DISCLAIMER

It doesn't work on MacOS and Fedora because of issues regarding a module named pynput!


# To-do List!
- [X] Add customization
- [X] Add constant mode
- [ ] Add Windows support
- [ ] Create aur package
- [ ] (Maybe) Create deb package
- [ ] Something you can suggest in "ideas" (https://github.com/SpamixOfficial/OpenClick/discussions/1)
