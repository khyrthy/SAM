import sys,os,utils,subprocess
from colorama import *
from time import *

def unpkg(package,destination="/usr/share/spm/packages/"):
    try:
        open(package).close()
    except FileNotFoundError:
        print(Fore.RED+"ERROR : The specified package doesn't exists")
        return 1
    print(Fore.RESET)
    subprocess.call(["tar","-xvf",package])
    subprocess.call(["cp","-r",package.split("_")[0],destination+"/"+package.split("_")[0]])
    subprocess.call(["rm","-rf",package.split("_")[0]])
    subprocess.call(["mkdir",destination+package.split("_")[0]+"/Files"])
    subprocess.call(["tar","-xvf",destination+package.split("_")[0]+"/Files.tar","--directory",destination+package.split("_")[0]+"/Files"])
