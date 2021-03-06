import sys,os,utils,subprocess
from colorama import *
from time import *

cache = "/var/cache/sam"
apps = "/usr/share/applications"


def unpkg(package,destination="/usr/share/sam/packages/"):

  # Check if root
  if os.getuid() != 0:
      # Program is not runned as root
      print(Fore.RED + "ERROR : Install command must be runned as root" + Style.RESET_ALL)
      return 1

  print(Fore.CYAN + "\n-> Extracting package..." + Style.RESET_ALL)
  os.system("cp " + package + " " + cache + "/ && cd " + cache + " && tar xvf " + package + " && rm " + package)

  

  print(Fore.CYAN + "\n-> Reading INFO...")
  INFO = utils.read_file(cache + "/INFO", "options")

  print(Fore.CYAN + "\n-> Verifying package architecture...")
  if not INFO["Architecture"] == utils.read_file("/usr/share/sam/config", "options")["Architecture"]:
    print(Fore.RED + "ERROR : Unknown architecture " + INFO["Architecture"] + ". Must be " + utils.read_file("/usr/share/sam/config", "options")["Architecture"] + Style.RESET_ALL)
    return 2

  print(Fore.CYAN + "\n-> Checking wether package is in the db")
  for element in utils.read_file("/usr/share/sam/installed.db", "options"):
    if element.split(" ")[0] == INFO["PackageName"]:
      if element.split(" ")[1] == INFO["Version"]:
        print(Fore.GREEN + INFO["PackageName"] + " is already at the latest version (" + INFO["Version"] + ")" + Style.RESET_ALL)
        return 0

  print(Fore.CYAN + "\n---- PACKAGE INFORMATION ----" + Style.RESET_ALL)
  for property in INFO:
    print(Fore.CYAN + property + Style.RESET_ALL + " : " + INFO[property])

  if input(Fore.CYAN + "Continue Installation? [Y:n] : " + Style.RESET_ALL).lower() == "y":
    pass
  else:
    print(Fore.CYAN + "Abort." + Style.RESET_ALL)
    return 0

  print(Fore.CYAN + "\n-> Creating install directory..." + Style.RESET_ALL)
  os.system("mkdir " + destination + INFO["PackageName"])

  print(Fore.CYAN + "\n-> Extracting Files.tar in destination folder..." + Style.RESET_ALL)
  os.system("cp -r " + cache + "/Files.tar " + destination + INFO["PackageName"] + " && cd " + destination + INFO["PackageName"] + " && tar xvf Files.tar && rm Files.tar")

  
  print(Fore.CYAN + "`\n-> Creating desktop entry..." + Style.RESET_ALL)
  desktop_entry = open(apps + "/" + INFO["PackageName"] + ".desktop", "w")

  # Write informations to the desktop entry
  desktop_entry.write("[Desktop Entry]" + "\n")
  desktop_entry.write("Name=" + INFO["Name"] + "\n")
  desktop_entry.write("Comment=" + INFO["Description"] + "\n")
  desktop_entry.write("Type=Application" + "\n")
  desktop_entry.write("Exec=sam-run " + INFO["PackageName"] + "\n")
  desktop_entry.write("Terminal=" + str(INFO["Terminal"]).lower() + "\n")
  desktop_entry.write("Icon=" + os.path.abspath(destination) + "/" + INFO["PackageName"] + "/" + INFO["Icon"] + "\n")

  desktop_entry.close()

  os.system("chmod +x " + apps + "/" + INFO["PackageName"] + ".desktop")

  print(Fore.CYAN + "\n-> Clearing Cache..." + Style.RESET_ALL)
  os.system("rm -rf " + cache + "/*")

  print(Fore.CYAN + "\n-> Updating database..." + Style.RESET_ALL)
  database = open("/usr/share/sam/installed.db", "w")
  database.write(INFO["PackageName"] + " " + INFO["Version"] + "=" + INFO["Exec"] + "\n")

  print(Fore.GREEN + "\nSuccessfully Installed " + INFO["Name"] + " " + INFO["Version"] + Style.RESET_ALL)
  return 0
