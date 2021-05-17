#!/usr/bin/env python3

# A program to run installed apps
import os, sys, utils
from colorama import *

if len(sys.argv) == 1:
    print(Fore.RED + "ERROR : Missing application argument")

else:

    ran = False

    for element in utils.read_file("installed.db", "options"):

        if element.split(" ")[0] == sys.argv[1]:
            os.system("cd ./packages/" + element.split(" ")[0] + " && ./" + utils.read_file("installed.db", "options")[element])
            ran = True


    if not ran:
        print(Fore.RED + "ERROR : Could not find package " + sys.argv[1] + Style.RESET_ALL)