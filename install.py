import os, json
installedPackeges = True
# Module checking!

print("Checking for the modules on your system...")
## Checking if modules are installed and configuring settings.txt
try:
	import colorama
	print("Module \"colorama\" was found!")
	# cresult = True
except ModuleNotFoundError:
	print("The module named \"colorama\" wasn't found! Do you want to install it? ([Y]es/[N]o)")
	coloramainput = input().upper()
	if coloramainput == "Y" or coloramainput == "YES":
		os.system("pip install colorama")
		# cresult = True
	elif coloramainput == "N" or coloramainput == "NO":
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
	print("The module named \"pynput\" wasn't found! Do you want to install it? ([Y]es/[N]o)")
	pynputinput = input().upper()
	if pynputinput == "Y" or pynputinput == "YES":
		os.system("pip install pynput")
		# presult = True
	elif pynputinput == "N" or pynputinput == "NO":
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
	print("The module named \"flagser\" wasn't found! Do you want to install it? ([Y]es/[N]o)")
	pynputinput = input().upper()
	if pynputinput == "Y" or pynputinput == "YES":
		os.system("pip install flagser")
		# presult = True
	elif pynputinput == "N" or pynputinput == "NO":
		installedPackeges = False
		print("Then you need to install it. Read the instructions on the github page or read the README.md!")
	else:
		print("That wasn't a N or an Y.")
		quit()

if installedPackeges:
	#f = open('./settings.txt','r')
	#a = ['firststartup=false']
	#lst = []
	#for line in f:
	#    for word in a:
	#        if word in line:
	#            line = line.replace(word,'')
	#    lst.append(line)
	#f.close()
	#f = open('./settings.txt','w')
	#for line in lst:
	#    f.write(line)
	#f.write("firststartup=true")
	#f.close()
	with open('settings.json') as f:
		data = json.load(f)

	data['firststartup']=True
	with open('settings.json', 'w') as outfile:
		json.dump(data, outfile,indent=4)
	print("You are ready to go! \nPlease make sure you have tKinter installed manually. If it isn't installed then your can read the readme for examples on how to install it!\nRead the docs over at https://github.com/SpamixOfficial/OpenClick/blob/main/README.md for more information!")


else:
	print(Back.RED + "Sorry, but either one or both of the modules wasn't found. \n Read the instructions for help on how to install them!")
	quit()
