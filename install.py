import os
installedPackeges = True
# Module checking!

print("Checking for the modules on your system...")
## Checking if modules are installed and configuring settings.txt
try:
	import colorama
	print("Module \"colorama\" was found!")
	# cresult = True
except ModuleNotFoundError:
	print("The module named \"colorama\" wasn't found! Do you want to install it? (y/n)")
	coloramainput = input().upper()
	if coloramainput == "Y":
		os.system("pip install colorama")
		# cresult = True
	elif coloramainput == "N":
		installedPackeges = False
		print("Then you need to install it. Read the instructions on the github page or read the README.md!")
	else:
		print("That wasn't a N or an Y.")
		quit()

try:
	import pynput
	print("Module \"pynput\" was found!")
	presult = True
except ModuleNotFoundError:
	print("The module named \"pynput\" wasn't found! Do you want to install it? (y/n)")
	pynputinput = input().upper()
	if pynputinput == "Y":
		os.system("pip install pynput")
		# presult = True
	elif pynputinput == "N":
		installedPackeges = False
		print("Then you need to install it. Read the instructions on the github page or read the README.md!")
	else:
		print("That wasn't a N or an Y.")
		quit()
#checking for flagser
try:
	import flagser
	print("Module \"flagser\" was found!")
	presult = True
except ModuleNotFoundError:
	print("The module named \"flagser\" wasn't found! Do you want to install it? (y/n)")
	pynputinput = input().upper()
	if pynputinput == "Y":
		os.system("pip install flagser")
		# presult = True
	elif pynputinput == "N":
		installedPackeges = False
		print("Then you need to install it. Read the instructions on the github page or read the README.md!")
	else:
		print("That wasn't a N or an Y.")
		quit()

if installedPackeges:
	f = open('./settings.txt','r')
	a = ['firststartup=false']
	lst = []
	for line in f:
	    for word in a:
	        if word in line:
	            line = line.replace(word,'')
	    lst.append(line)
	f.close()
	f = open('./settings.txt','w')
	for line in lst:
	    f.write(line)
	f.write("firststartup=true")
	f.close()
	print("You are ready to go!")


else:
	print(Back.RED + "Sorry, but either one or both of the modules wasn't found. \n Read the instructions for help on how to install them!")
	quit()
