import os, json, requests, platform
installedPackeges = True
# loading json data
with open('settings.json') as f:
	data = json.load(f)

if platform.system() == "Linux":
	if os.environ.get('WAYLAND_DISPLAY'):
		data["sudo"] = True
		if os.geteuid() != 0:
			print("Sudo is needed to run OpenClick Module Edition using Wayland.")
			print("\n---Try again with sudo---")
			with open('settings.json', 'w') as outfile:
				json.dump(data, outfile,indent=4)
			quit()
		with open('settings.json', 'w') as outfile:
			json.dump(data, outfile,indent=4)

# Setting version ID
idcheck = input("Is this the latest release? (y/n): ").lower()

if idcheck == "y":
	response = requests.get("https://api.github.com/repos/SpamixOfficial/OpenClick/releases/latest")
	respdata = response.json()
	relid = respdata["id"]
	data['release']=str(relid)
elif idcheck == "n":
	response = requests.get("https://api.github.com/repos/SpamixOfficial/OpenClick/tags")
	respdata = json.loads(response.text)
	print("\nReleases:")
	for tag in respdata:
		print(tag["name"])
	idcheck2 = input("Enter the tag of the release: ")
	response = requests.get("https://api.github.com/repos/SpamixOfficial/OpenClick/releases/tags/" + idcheck2)
	if response.status_code == 404:
		print("404 Error: Non-valid tag: " + idcheck2)
		quit()
	respdata = response.json()
	relid = respdata["id"]
	data['release']=str(relid)
else:
	print("\"" + idcheck + "\" is not a valid response")
	quit


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

	data['firststartup']=True
	with open('settings.json', 'w') as outfile:
		json.dump(data, outfile,indent=4)
	print("You are ready to go!\n \nPlease make sure you have tKinter installed manually. If it isn't installed then you can read the readme for examples on how to install it!\nRead the docs over at https://github.com/SpamixOfficial/OpenClick/blob/main/README.md for more information!")


else:
	print(Back.RED + "Sorry, but either one or both of the modules wasn't found. \n Read the instructions for help on how to install them!")
	quit()
