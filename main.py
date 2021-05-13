#!/usr/bin/env python3

# The SPM Main
# It manages every function of the SPM program

import sys, subprocess
import unpkg

# Import the spm modules
import makepkg, update

# We use the colorama module to print colors in the terminal
from colorama import Fore, Style

print(Fore.GREEN + "[SPM 0.1]" + Style.RESET_ALL)

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
        print(" - spm [options] {args}")
        print(
            "\n" + Fore.CYAN + "COMMANDS LIST" + Style.RESET_ALL + "\n\n" +

            Fore.MAGENTA + "spm makepkg [foldername]" + Style.RESET_ALL + "\n" +
            "Creates a spm package from the specified folder" + "\n"
        )
    
    if sys.argv[1] == "makepkg":

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

                print(Fore.GREEN + "SPM ran successfully" + Style.RESET_ALL)

    elif sys.argv[1] == "update":

        if not len(sys.argv) == 2:
            print(Fore.RED + "ERROR : Update doesn't needs any argument.")
            print(Style.RESET_ALL)

        else:

            err = update.update()


            if type(err) == int and err != 0:

                print(Fore.RED + "SPM exited with error code " + str(err) + Style.RESET_ALL)

            else:

                print(Fore.GREEN + "SPM ran successfully" + Style.RESET_ALL)

    elif sys.argv[1] == "unpkg":
        
        if len(sys.argv) == 2:
            print(Fore.RED+"ERROR : Please specify a package")

        elif len(sys.argv) == 3:
            unpkg.unpkg(sys.argv[2])
        
        elif len(sys.argv) == 4:
            unpkg.unpkg(sys.argv[2],sys.argv[3])
    
    else:

        print(Fore.RED + "ERROR :", sys.argv[1], ": unknown option")
        print(Style.RESET_ALL)
        print("Usage :")
        print(" - spm [options] {args}")