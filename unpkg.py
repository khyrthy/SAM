import sys,os,utils,subprocess
from colorama import *
from time import *

import install
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

    DEPENDENCIES = open(destination+package.split("_")[0]+"/DEPENDENCIES")

    for line in DEPENDENCIES:
        package_name = line.replace("\n","")
        err = install.install(package_name)

        if type(err) == int and err != 0:
            print(Fore.RED + "ERROR : A dependencie cannot be resolved, try running spm update")
            return 1
