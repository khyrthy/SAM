import os,utils
from colorama import *

def remove(package):

    print(Fore.CYAN + "\n-> Scanning database to find package " + package + "..." + Style.RESET_ALL)
    found = False

    for element in utils.read_file("/usr/share/sam/installed.db", "options"):
        if element.split(" ")[0] == package:
            found = True

    if not found:
        print(Fore.RED + "ERROR : Could not find " + package + " in database.")
        return 1
    
    if input(Fore.CYAN + "\nContinue removing " + package + "? [Y:n] : " + Style.RESET_ALL).lower() == "y":
        pass
    else:
        print("Abort")
        return 0

    print(Fore.CYAN + "\n-> Removing package repertory..." + Style.RESET_ALL)
    os.system("rm -rf /usr/share/sam/packages/" + package)

    print(Fore.CYAN + "\n-> Removing Desktop Entry..." + Style.RESET_ALL)
    os.system("rm /usr/share/applications/" + package + ".desktop")

    print(Fore.CYAN + "\n-> Removing package from database..." + Style.RESET_ALL)
    database = open("/usr/share/sam/installed.db", "r")
    database_content = database.readlines()
    database.close()

    iterator = 0
    for line in database_content:
        if line.startswith(package):
            del database_content[iterator]

        iterator += 1
    
    database = open("/usr/share/sam/installed.db", "w+")

    for line in database_content:
        database.write(line)

    database.close() 