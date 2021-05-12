# The utils file contains common utils used by SPM to do complex actions

def read_file(filepath, mode):

    # The options mode will generate a dict with the file content
    if mode == "options":
        file = open(filepath, "r")
        options = {}

        increment = 0

        for line in file.readlines():   


            if line.split("=")[0] == line:

                if line[:1] == "#":
                    pass

                elif line == "\n":
                    pass

                else:                

                    print("\nERROR : Invalid line in file", filepath, ": line 6 (" + line + ")")
                    return 1  

            else:
                options[line.split("=")[0]] = line.split("=")[1]

                if line.split("=")[1][-1] == "\n":

                    options[line.split("=")[0]] = line.split("=")[1][:-1]

            increment += 1

            
        file.close()
        return options        
