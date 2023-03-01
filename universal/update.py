import requests, json, os, zipfile, glob, getpass, shutil

# opening settings.json file
jsfile = open("settings.json")
##

# getting new release json
response = requests.get("https://api.github.com/repos/SpamixOfficial/OpenClick/releases/latest")
respdata = response.json()
##

# getting new release info
newid = respdata["id"]
tag = respdata["tag_name"]
##

# local data
jsdata = json.load(jsfile)

locdata = jsdata["release"]
##

# url stuff
downurl = respdata["zipball_url"]

download = requests.get(downurl)
##

def install():
    global source
    try:
        shutil.move("tmp/universal", source, copy_function = shutil.copytree)
        return 0
    except:
        return 1

# filename and dir setting
downname = "openclick-" + tag + "-release.zip"
##
print("Newest release: " + str(newid) + "\nLocal release: " + str(locdata))
updateinp = input("\nDo you want to update? y/n: ").lower()   

if updateinp == "y":
    # downloading and renaming zip file
    with open(downname, 'wb') as fd:
        print("Downloading...")
        fd.write(download.content)
    # outputing into directory and removing zip file
    with zipfile.ZipFile(downname, 'r') as dezip:
        print("Extracting into folder...")
        dezip.extractall(path="tmp")
    os.remove(downname)

    # scanning folder name inside directory
    dowrelname = os.listdir("tmp")
    dowdirname = " ".join(str(x) for x in dowrelname)
    print(dowdirname)

    # run installation script
    print("Installing...")
    bdest = "old"
    source = os.getcwd()
    # Backup files if something goes wrong
    if os.path.isdir(bdest) == True:
        shutil.move(source, bdest, copy_function = shutil.copytree)
    else:
        os.mkdir(bdest)
        shutil.move(source, bdest, copy_function = shutil.copytree)
    installp = install()

    if installp != 0:
        print("Installation failed. \nRemoving temporary files and exiting.")
        # remove all files if installation script fails
        sutil.rmtree("tmp")
        quit()
    print("Update was successful! Removing update files...")
    # remove directory when done
    shutil.rmtree("tmp")
    print("Exiting...")
    quit()
else:
    quit()	
