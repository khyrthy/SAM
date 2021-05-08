# The makepkg module
# Used to generate a spm package

import os, utils

def makepkg(foldername):

    print("Checking specified directory...")

    # Check if package folder exists
    try: 
        os.listdir(foldername)
    except FileNotFoundError:
        print("ERROR : The specified directory doesn't exists")
        return 1
    except NotADirectoryError:
        print("ERROR : The specified element is not a directory")
        return 2

    # Check if all the necessary files exists

    # Absolutely necessary files presence
    presence_info = False
    presence_files = False

    # Facultative files
    presence_facultative_dependencies = False
    presence_facultative_preinst = False
    presence_facultative_postinst = False
    presence_facultative_predel = False
    presence_facultative_postdel = False


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
        return 3


    # Reading info file
    print("Reading info file...")
    
    INFO = utils.read_file(foldername + "/INFO", "options")

    if INFO == 1:

        print("There was an error while reading the INFO File.")
        return 4

    print("Checking necessary info...")


    info_verify = {
        "packagename": False,
        "name": False,
        "version": False,
        "description": False,
        "exec": False,
        "desktop": False,

        "icon": False
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

        elif e == "Desktop":
            info_verify["desktop"] = True

        elif e == "Icon":
            info_verify["icon"] = True

        else:
            print("\nERROR :", e, ": Unknown property")

    # Check if every necessary property is there
    for v in info_verify:

        if v == "icon":
            pass

        elif info_verify[v] is not True:
            
            print("\nERROR : Property", v, "was not specified in INFO")
            return 5
        
    # Check if Desktop property is valid
    if INFO["Desktop"] == "True":

        INFO["Desktop"] = True

        if not info_verify["icon"]:

            print("\nERROR : No icon specified while package is a desktop app")
            return 5
    
    elif INFO["Desktop"] == "False":

        INFO["Desktop"] = False

    else:
        print("\nERROR : Desktop property must be \"True\" or \"False\"")
        return 5

    
    # Print package info
    print("\n=========================\nPackage Info :\n")

    for e in INFO:

        print(e, ":", INFO[e])

    if input("\nContinue building package? [Y/n] : ").lower() == "y":

        pass

    else:

        print("Operation Aborted Successfully.")
        return None