# The makepkg module
# Used to generate a spk package

import os, utils, subprocess, shutil
from colorama import *


def makepkg(folder, supported_archs):

    if folder.endswith("/"):
        foldername = folder[:-1]
    else:
        foldername = folder

    print("Checking specified directory...")

    # Check if package folder exists
    try: 
        os.listdir(foldername)
    except FileNotFoundError:
        print("ERROR : The specified directory doesn't exists")
        return 1
    except NotADirectoryError:
        print("ERROR : The specified element is not a directory")
        return 1

    # Check if all the necessary files exists

    # Absolutely necessary files presence
    presence_info = False
    presence_files = False



    for f in os.listdir(foldername):

        if f == "INFO":
            presence_info = True
            print("Verified presence of necessary INFO file.")
        
        elif f == "Files.tar":
            presence_files = True
            print("Verified presence of necessary Files.tar archive.")

        
        elif f == "DEPENDENCIES":
            presence_facultative_dependencies = True
            print("Verified presence of facultative DEPENDENCIES file.")

    # Checking if everything alright
    if presence_info and presence_files == True:
        print("All necessary files are present.")

    else:
        print(Fore.RED + "ERROR : some necessary file are missing in the specified folder")
        return 1


    # Reading info file
    print("Reading info file...")
    
    INFO = utils.read_file(foldername + "/INFO", "options")

    if INFO == 1:

        print("There was an error while reading the INFO File.")
        return 1

    print("Checking necessary info...")


    info_verify = {
        "packagename": False,
        "name": False,
        "version": False,
        "description": False,
        "exec": False,
        "arch": False,
        "icon": False,
        "terminal": False,
    }

    # Check global file
    for e in INFO:
        if e == "PackageName":
            
            if not INFO[e].split(" ")[0] == INFO[e]:
                print("ERROR : (INFO File) : PackageName property must not contain spaces.")
                return 5

            else:
                info_verify["packagename"] = True

        elif e == "Name":
            info_verify["name"] = True

        elif e == "Version":
            try:
                INFO["Version"] = float(INFO["Version"])
                info_verify["version"] = True
            except ValueError:
                print("ERROR : Version format is invalid. Must be X.XX")
                return 5
        
        elif e == "Description":
            info_verify["description"] = True

        elif e == "Exec":
            info_verify["exec"] = True


        elif e == "Icon":
            info_verify["icon"] = True

        elif e == "Architecture":
            current_arch_supported = False

            for arch in supported_archs:
                if INFO["Architecture"] == arch:
                    current_arch_supported = True



            if not current_arch_supported:
                print("\nERROR : Architecture", INFO["Architecture"], "is not supported")
                return 2

            else:
                info_verify["arch"] = True

        elif e == "Terminal":

            if INFO["Terminal"].lower() == "true":
                INFO["Terminal"] = True
                info_verify["terminal"] = True

            elif INFO["Terminal"].lower() == "false":
                INFO["Terminal"] = False
                info_verify["terminal"] = True

            else:
                print("\nERROR : Property Terminal must be true or false")
                return 1

        else:
            print("\nERROR :", e, ": Unknown property")
            return 2

    # Check if every necessary property is there
    for v in info_verify:

        if info_verify[v] is not True:
            
            print("\nERROR : Property", v, "was not specified in INFO")
            return 5
        
    os.rename(foldername, INFO["PackageName"])


    # Check Files.tar
    print("Checking Files.tar")
    try:
        open(INFO["PackageName"] + "/Files.tar", "r")
    except FileNotFoundError:
        print("\nERROR : Files.tar Archive not found")
        return 1


    try:
        os.mkdir(".temp")
    except FileExistsError:
        shutil.rmtree(".temp")
        os.mkdir(".temp")

    os.system("cd .temp && tar xf ../" + INFO["PackageName"] + "/Files.tar")

    print("Checking Exec...")
    # Check if Exec is valid
    try:
        open(".temp/" + INFO["Exec"], "r").close()
    except FileNotFoundError:
        print("\nERROR : Specified Exec was not found")
        return 1



    print("Checking Icon...")
    try:
        open(".temp/" + INFO["Icon"], "r").close()
        desktop_noicon = False
    except FileNotFoundError:
        print("WARNING : Specified Icon was not found")
        desktop_noicon = True
    except KeyError:
        print("WARNING : No Icon specified")
        desktop_noicon = True

        

    print("Removing temp folder...")
    shutil.rmtree(".temp")
    
    # Print package info
    print("\n=========================\nPackage Info :\n")

    for e in INFO:

        print(e, ":", INFO[e])

    if desktop_noicon is True:
        print("The icon is missing or invalid. The package won't have any icon.")

    if input("\nContinue building package? [Y:n] : ").lower() == "y":

        pass

    else:

        print("Operation Aborted Successfully.")
        return 0

    try:
        open(INFO["PackageName"] + "_" + str(INFO["Version"]) + "_" + INFO["Architecture"] + ".spk", "r").close()

        if input("The package " + INFO["PackageName"] + "_" + str(INFO["Version"]) + "_" + INFO["Architecture"] + ".spk already exists. Do you want to overwrite it? [Y:n] : ").lower() == "y":
            os.remove(INFO["PackageName"] + "_" + str(INFO["Version"]) + "_" + INFO["Architecture"] + ".spk")

        else:
            print("Operation Aborted Successfully.")
            return 0
        
    except FileNotFoundError:
        pass
    

    print("\nStarting building the package...")

    print("Moving folder...")

    print("Building package...")

    folder_listing = ""

    # Create the filelist arg for the command
    for file in os.listdir(INFO["PackageName"]):

        folder_listing += file + " "

    packagename = INFO["PackageName"] + "_" + str(INFO["Version"]) + "_" + INFO["Architecture"] + ".spk"

    # Call the tar command to create the package
    os.system("cd " + INFO["PackageName"] + " && " + "tar -cf " +  packagename + " " + folder_listing + " && mv " + packagename + " ../")
