#!/usr/bin/env python3

# The SPM Main
# It manages every function of the SPM program

import sys, subprocess

# Import the spm modules
import makepkg
import unpkg
import remove

# We use the colorama module to print colors in the terminal
from colorama import Fore, Style

# search for verbose option

verbose = False

for option in sys.argv:
    if option == "-v" or option == "--verbose":
        verbose = True

if verbose:
    print(Fore.GREEN + "[SAM 0.3]" + Style.RESET_ALL)

# Check if necessary packages are installed
if subprocess.call(["which", "tar"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT) != 0:
    print(Fore.RED + "ERROR : Missing tar" + Style.RESET_ALL)
    sys.exit()

# The program works with a arg command
if len(sys.argv) == 1:

    print(Fore.RED + "ERROR : You didn't specify any option")
    print(Style.RESET_ALL)
    print("Usage :")
    print(" - spm [options] {args}")



else : 

    if sys.argv[1] == "help":

        print("Usage :")
        print(" - sam [options] {args}")
        print(
            "\n" + Fore.CYAN + "VALID ARGUMENTS" + Style.RESET_ALL + "\n\n" +

            Fore.MAGENTA + "-v --verbose" + Style.RESET_ALL + "                     " + "Enable verbose"
        )
        print(
            "\n" + Fore.CYAN + "COMMANDS LIST" + Style.RESET_ALL + "\n\n" +

            Fore.MAGENTA + "sam makepkg [foldername]" + Style.RESET_ALL + "         " +
            "Creates an application package from the specified folder" + "\n" +

            Fore.MAGENTA + "sam install [package file]" + Style.RESET_ALL + "       " +
            "Installs a built application package"
        )
    
    elif sys.argv[1] == "makepkg":

        if len(sys.argv) == 2:
            print(Fore.RED + "ERROR : makepkg needs a folder")
            print(Style.RESET_ALL)

        else:

            err = makepkg.makepkg(sys.argv[2])

            if type(err) == int and err != 0:

                print(Fore.RED + "SPM Exited with error code " + str(err) + Style.RESET_ALL)

            elif err == "unknown":

                print(Fore.RED + "An unknown error occurred" + Style.RESET_ALL)

            else:
                if verbose:
                    print(Fore.GREEN + "SAM ran successfully" + Style.RESET_ALL)

    elif sys.argv[1] == "install":
        
        err = None

        if len(sys.argv) == 2:
            print(Fore.RED+"ERROR : You didn't specify any package" + Style.RESET_ALL)

        else:
            for package in sys.argv[2:]:

                if package == "-v" or package == "--verbose":
                    continue

                try:
                    open(package, "r")
                except FileNotFoundError:
                    print(Fore.RED + "ERROR : " + package + " not found")
                    continue

                if package.endswith(".spk"):
                    err = unpkg.unpkg(package)
                else:
                    print(Fore.RED + "ERROR : " + package + " is not an SAM package." + Style.RESET_ALL)
                    continue

        if type(err) == int and err != 0:
            print(Fore.RED + "SAM exited with error code " + str(err) + Style.RESET_ALL)
        
        else:
            if verbose:
                print(Fore.GREEN+"SAM ran successfully"+Fore.RESET)
    
    elif sys.argv[1] == "remove":

        err = None

        if len(sys.argv) == 2:
            print(Fore.RED+"ERROR : You didn't specify any package" + Style.RESET_ALL)

        else:
            for package in sys.argv[2:]:

                if package == "-v" or package == "--verbose":
                    continue

                err = remove.remove(package)

        if type(err) == int and err != 0:
            print(Fore.RED + "SAM exited with error code " + str(err) + Style.RESET_ALL)
        
        else:
            if verbose:
                print(Fore.GREEN+"SAM ran successfully"+Fore.RESET)

    else:

        print(Fore.RED + "ERROR :", sys.argv[1], ": unknown option")
        print(Style.RESET_ALL)
        print("Usage :")
        print(" - sam [options] {args}")
