import subprocess

import unpkg

from colorama import *
def install(package_name):

    package_source = None
    packages_list = open("cache/MAIN.index","r")

    for line in packages_list:
        listed_package_name = line.split("=")[0]
        listed_package_source = line.split("=")[1]

        if package_name == listed_package_name:
            package_source = listed_package_source

    if package_source is None:
        print(Fore.RED+"The specified package doesn't exists . Try running spm update"+Fore.RESET)
        return 1

    subprocess.call(["wget",package_source.replace("\n","")])
    filename = package_source.replace("\n","").split("/")[-1]

    err = unpkg.unpkg(filename)

    if type(err) == int and err != 0:
        return 1
