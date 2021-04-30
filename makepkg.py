# The makepkg module
# Used to generate a spm package

import os

def makepkg(foldername):

    print("Checking specified directory...")

    # Check if package folder exists
    try: 
        os.listdir(foldername)
    except FileNotFoundError:
        return 1
    except NotADirectoryError:
        return 2

    # Check if all the necessary files exists

    # Absolutely necessary files presence
    presence_info = False
    presence_files = False

    # Facultative files
    

    for f in os.listdir(foldername):

        if f == "INFO":
            presence_info = True
            print("Verified presence of necessary INFO file.")
        
        elif f == "Files.tar":
            presence_files = True
            print("Verified presence of Files.tar archive.")

        
        
    