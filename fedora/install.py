import os
cresult = False
presult = False
# Module checking!

print("Checking for the modules on your system...")
## Checking if modules are installed and configuring settings.txt

print("The module named \"colorama\" wasn't found! Do you want to install it? (y/n)")
print("\nWARNING! THIS MODULE NEEDS TO BE INSTALLED AS ROOT BECAUSE OF PERMISSION ERRORS")
coloramainput = input().upper()
if coloramainput == "Y":
	os.system("sudo pip install colorama")
	cresult = True
elif coloramainput == "N":
	print("Then you need to install it. Read the instructions on the github page or read the README.md!")
else:
	print("That wasn't a N or an Y.")
	quit()

print("The module named \"keyboard\" wasn't found! Do you want to install it? (y/n)")
print("\nWARNING! THIS MODULE NEEDS TO BE INSTALLED AS ROOT BECAUSE OF PERMISSION ERRORS")
keyboardinput = input().upper()
if keyboardinput == "Y":
	os.system("sudo pip install keyboard")
	presult = True
elif keyboardinput == "N":
	print("Then you need to install it. Read the instructions on the github page or read the README.md!")
else:
	print("That wasn't a N or an Y.")
	quit()


print("The module named \"mouse\" wasn't found! Do you want to install it? (y/n)")
print("\nWARNING! THIS MODULE NEEDS TO BE INSTALLED AS ROOT BECAUSE OF PERMISSION ERRORS")
mouseinput = input().upper()
if mouseinput == "Y":
	os.system("sudo pip install mouse")
	mresult = True
elif mouseinput == "N":
	print("Then you need to install it. Read the instructions on the github page or read the README.md!")
else:
	print("That wasn't a N or an Y.")
	quit()

if presult == True and cresult == True and mresult == True:	
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
	print(Back.RED + "Sorry, but the either one or both of the modules wasn't found. \n Read the instructions for help on how to install them!")
	quit()