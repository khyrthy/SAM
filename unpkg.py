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

  DEPENDENCIES = open(destination+package.split("_")[0]+"/DEPENDENCIES","r")

  if os.path.exists("/usr/bin/apt"):
    system_package_manager = "apt"

  elif os.path.exists("/usr/bin/pacman"):
    system_package_manager = "pacman"

  print(system_package_manager)
  lines = DEPENDENCIES.readlines()
  for line in lines:
    print("Reading line of DEPENDENCIES")
    if line != "":
      print("Installing dependencie...")
      if system_package_manager == "apt":
        subprocess.call([system_package_manager,"install",line.replace("\n","")])
      elif system_package_manager == "pacman":
        subprocess.call([system_package_manager,"-S",line.replace("\n","")])