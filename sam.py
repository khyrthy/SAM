#!/usr/bin/env python3

# The SPM Main
# It manages every function of the SPM program

import sys, subprocess

# Import the spm modules
import makepkg
import unpkg
import remove
import utils

# We use the colorama module to print colors in the terminal
from colorama import Fore, Style

# search for verbose option

verbose = False

# the list of supported archs
supported_archs = ["x86", "x86-64", "arm64", "aarch64", "armv6", "armv7", "armv8", "arm64", "aarch64"]

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
            "Installs a built application package" + "\n" +

            Fore.MAGENTA + "sam remove [package]" + Style.RESET_ALL + "             " +
            "Removes an installed package" + "\n" +

            Fore.MAGENTA + "sam list" + Style.RESET_ALL + "                         " + 
            "Lists all the installed packages"
        )
    
    elif sys.argv[1] == "makepkg":

        if len(sys.argv) == 2:
            print(Fore.RED + "ERROR : makepkg needs a folder")
            print(Style.RESET_ALL)

        else:

            err = makepkg.makepkg(sys.argv[2], supported_archs)

            if type(err) == int and err != 0:
                if verbose:
                    print(Fore.RED + "SPM Exited with error code " + str(err) + Style.RESET_ALL)

            elif err == "unknown":
                if verbose:
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
            if verbose:
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
            if verbose:
                print(Fore.RED + "SAM exited with error code " + str(err) + Style.RESET_ALL)
        
        else:
            if verbose:
                print(Fore.GREEN+"SAM ran successfully"+Fore.RESET)

    elif sys.argv[1] == "list":

        err = None


        if not len(sys.argv) == 2 and not verbose:

            print(Fore.RED + "ERROR : list doesn't take any argument" + Style.RESET_ALL)
            err = 1
        
        elif verbose and not len(sys.argv) == 3:

            print(Fore.RED + "ERROR : list doesn't take any argument" + Style.RESET_ALL)
            err = 1

        else:

            if not open("/usr/share/sam/installed.db","r").readlines() == []:
                print(Fore.CYAN + "---- INSTALLED PACKAGES ----" + Style.RESET_ALL)

                for element in utils.read_file("/usr/share/sam/installed.db", "options"):
                    print(element)

            else:

                print(Fore.CYAN + "No package installed." + Style.RESET_ALL)

        if type(err) == int and err != 0:
            if verbose:
                print(Fore.RED + "SAM exited with error code " + str(err) + Style.RESET_ALL)
        
        else:
            if verbose:
                print(Fore.GREEN+"SAM ran successfully"+Fore.RESET)

    else:

        print(Fore.RED + "ERROR :", sys.argv[1], ": unknown option")
        print(Style.RESET_ALL)
        print("Usage :")
        print(" - sam [options] {args}")
