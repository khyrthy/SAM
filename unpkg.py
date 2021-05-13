import sys,os,utils,subprocess
from colorama import *

def unpkg(package,destination="/usr/share/spm/packages/"):
    try:
        open(package).close()
    except FileNotFoundError:
        print(Fore.RED+"ERROR : The specified package doesn't exists")
        return 1
    print(Fore.RESET)
    subprocess.call(["tar","-xvf",package])
    subprocess.call(["cp","-r",package.split("_")[0],destination])
    subprocess.call(["rm","-rf",package.split("_")[0]])
