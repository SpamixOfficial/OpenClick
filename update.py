import requests, json, os, zipfile, glob, getpass, subprocess

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

# filename and dir setting
downdir = "/tmp/"
downname = "openclick-" + tag + "-release.zip"
finalfile = os.path.join(downdir, downname)
##

if not str(newid) == str(locdata):
    print("Newest release: " + str(newid) + "\nYour release: " + str(locdata))
    updateinp = input("\nDo you want to update? y/n: ").lower()   

    if updateinp == "y":
        # downloading and renaming zip file
        with open(finalfile, 'wb') as fd:
            fd.write(download.content)
        # outputing into directory and removing zip file
        with zipfile.ZipFile(finalfile, 'r') as dezip:
            dezip.extractall(path="/tmp/openclick")
        os.remove(finalfile)

        # scanning folder name inside directory
        dowrelname = os.listdir("/tmp/openclick")
        dowdirname = " ".join(str(x) for x in dowrelname)
        print(dowdirname)

        # run installation script
        installp = subprocess.run("/tmp/openclick/" + dowdirname + "/install.sh")

        if installp.returncode != 0:
            print("Installation failed. \nRemoving temporary files and exiting.")
            # remove all files if installation script fails
            dowdirfiles = glob.glob("/tmp/openclick/" + dowdirname + "/*")
            for f in dowdirfiles:
                os.remove(f)
            os.rmdir("/tmp/openclick/" + dowdirname)
            os.rmdir("/tmp/openclick")
            quit()
        
        # remove directory when done
        dowdirfiles = glob.glob("/tmp/openclick/" + dowdirname + "/*")
        for f in dowdirfiles:
            os.remove(f)
        os.rmdir("/tmp/openclick/" + dowdirname)
        os.rmdir("/tmp/openclick")
