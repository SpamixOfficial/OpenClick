import requests, json
from colorama import Fore, init 

init(autoreset=True)

# opening settings.json file
jsfile = json.load(open("settings.json"))
##

# getting new release json
response = requests.get("https://api.github.com/repos/SpamixOfficial/OpenClick/releases/latest")
respdata = response.json()
##

# getting new release info
newid = respdata["id"]

if not str(jsfile["release"]) == str(newid):
    print(Fore.YELLOW + "New release available to download! " + Fore.RED + "\nConsider updating using the \"update.py\" file since we dont support older versions of our software!")
else:
    print("Version is up to date!")