import requests

SOURCES = "SOURCES"
CACHE = "cache/"
HEADERS = {'User-Agent': 'Mozilla/5.0 (Android 5.1; Tablet; rv:50.0) Gecko/50.0 Firefox/50.0'}



def update():

    # Read SOURCES
    print("Reading SOURCES...")
    
    SOURCES_File = open(SOURCES, "r")

    MIRROR_main = ""

    for line in SOURCES_File.readlines():

        if line.split("=")[0] == "main":
            
            if line.split("=")[1].endswith("\n"):

                MIRROR_main = line.split("=")[1][-1]

            else:

                MIRROR_main = line.split("=")[1]

    if MIRROR_main == "":

        print("ERROR : Invalid SOURCES file : missing main branch")
        return 1


    SOURCES_File.close()


    # Download new packages lists from the mirrors
    print("Downloading new packages lists...")

    INDEX_main = requests.get(MIRROR_main + "INDEX", headers=HEADERS)
    open(CACHE + "MAIN.index", "wb").write(INDEX_main.content)
    


