import os, json, requests


#Easier way of checking if input was yes
#Instead of manually checking if user input string is "Y" etc., the programm will just check whether user input is in the array or not 
#Adding ye as an valid option due to user typos
arr = {"yes", "y", "ye", ""}

#If the user input isnt in arr, it will just count as a no 




installedPackeges = True
# loading json data
with open('settings.json') as f:
	data = json.load(f)

# Setting version ID
idcheck = input("Is this the latest release? ([Y]es/[n]o): ").lower()

if idcheck in arr:
	response = requests.get("https://api.github.com/repos/SpamixOfficial/OpenClick/releases/latest")
	respdata = response.json()
	relid = respdata["id"]
	data['release']=str(relid)
else:
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



# Module checking!


 

print("Checking for the modules on your system...")
## Checking if modules are installed and configuring settings.txt
try:
	import colorama
	print("Module \"colorama\" was found!")
	# cresult = True
except ModuleNotFoundError:
	print("The module named \"colorama\" wasn't found! Do you want to install it? ([Y]es/[n]o)") 
	#Default option for no input = Yes
	coloramainput = input().lower()
	if coloramainput in arr:
		os.system("pip install colorama")
		# cresult = True
	else:
		installedPackeges = False
		print("Then you need to install it. Read the instructions on the github page or read the README.md!")


try:
	import pynput
	print("Module \"pynput\" was found!")
	presult = True
except ModuleNotFoundError:
	print("The module named \"pynput\" wasn't found! Do you want to install it? ([Y]es/[N]o)")
	pynputinput = input().lower()
	if pynputinput in arr:
		os.system("pip install pynput")
		# presult = True
	else:
		installedPackeges = False
		print("Then you need to install it. Read the instructions on the github page or read the README.md!")


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
	try:
		print(Back.RED + "Sorry, but either one or both of the modules wasn't found. \n Read the instructions for help on how to install them!")
	except:
		print("Sorry, but either one or both of the modules wasn't found. \n Read the instructions for help on how to install them!")
	
	quit()
