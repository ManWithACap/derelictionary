import os, json, vars
from colors import Colors

# local variables
data = []

# used to decide which nested function to call based on the category and mode chosen
def runSearch(category, method, mode="r"):
    """
    The primary function used to choose which nested function to use based on the "mode" parameter

    Parameters:
    - category (string): the category in which to search for data.
    - method (string): the method in which to search for data.
    - mode (string): read, write, or clear data mode
    """
    
    # used to read and report data back to the user
    def rData(dataList, mthd, qry):
        """
        A nested function responsible for actually searching out data and reporting it back to the user

        Parameters:
        - dataList (list): the list of dictionaries to be read from
        - mthd (string): the method in which to search in dataList
        - qry (string): the string value to be searched
        """

        # setup toggle variable to know if something was found
        foundSomething = True

        # colors! :D
        print(f"\n{Colors.B}{Colors.U}{Colors.CYAN}FOUND:{Colors.RESET}")
        
        # using the mthd parameter variable, decide which method to use when searching
        match mthd:
            case "g":

                # setup secondary toggle variable
                matchFound = False
                
                # perform the search
                for entry in dataList:

                    try:

                        if qry.lower() == entry['galaxy'].lower():

                            try:

                                print(f"{Colors.YELLOW}{Colors.B}{entry['name']}{Colors.RESET} - {entry['system']}, {Colors.GREEN}{Colors.B}{entry['type'].upper()}{Colors.RESET}.")
                                matchFound = True

                            except KeyError:

                                if category == "STARGATES":

                                    print(f"{Colors.YELLOW}{Colors.B}{entry['id']}{Colors.RESET} - {entry['system']}, {Colors.YELLOW}OS:{Colors.RESET} {entry['output']['system']}, {Colors.YELLOW}OG:{Colors.RESET} {entry['output']['galaxy']}.")
                                    matchFound = True

                                else:

                                    print(f"{Colors.YELLOW}{Colors.B}{entry['id']}{Colors.RESET} - {entry['system']}")
                                    matchFound = True

                    except KeyError:

                        if qry.lower() == entry['name'].lower():

                            for system in entry['systems']:

                                print(f"{Colors.YELLOW}{Colors.B}{system}{Colors.RESET}")
                                matchFound = True

                # if a match is found, set the toggle variable to say that something was found
                if matchFound:

                    foundSomething = True

                else:

                    foundSomething = False

            case "s":

                # setup secondary toggle variable
                matchFound = False
                
                # perform search
                for entry in dataList:

                    try:

                        if qry.lower() == entry['system'].lower():

                            try:

                                print(f"{Colors.YELLOW}{Colors.B}{entry['name']}{Colors.RESET} - {entry['galaxy']}, {Colors.GREEN}{Colors.B}{entry['type'].upper()}{Colors.RESET}.")
                                matchFound = True

                            except KeyError:

                                if category == "STARGATES":

                                    print(f"{Colors.YELLOW}{Colors.B}{entry['id']}{Colors.RESET} - {entry['galaxy']}, {Colors.YELLOW}OS:{Colors.RESET} {entry['output']['system']}, {Colors.YELLOW}OG:{Colors.RESET} {entry['output']['galaxy']}.")
                                    matchFound = True

                                else:

                                    print(f"{Colors.YELLOW}{Colors.B}{entry['id']}{Colors.RESET} - {entry['galaxy']}")
                                    matchFound = True

                    except KeyError:

                        for system in entry['systems']:

                            if qry.lower() == system.lower():

                                print(f"{Colors.YELLOW}{Colors.B}{entry['name']}{Colors.RESET}")
                                matchFound = True

                # if something was found, set the toggle variable to say that something was found
                if matchFound:

                    foundSomething = True

                else:

                    foundSomething = False

            case "t":

                # setup secondary toggle variable
                matchFound = False
                
                # perform search
                for entry in dataList:

                    if qry.lower() == entry['type']:

                        print(f"{Colors.YELLOW}{Colors.B}{entry['name']}{Colors.RESET} - {entry['system']}, {entry['galaxy']}.")
                        matchFound = True

                # if something was found, set the toggle variable to say that something was found
                if matchFound:

                    foundSomething = True

                else:

                    foundSomething = False

            case "lp":

                # setup secondary toggle variable
                matchFound = False
                
                # perform search
                for entry in dataList:

                    if category == "SYSTEMS":

                        for system in entry['systems']:

                            if qry.lower() in system.lower():

                                print(f"{Colors.YELLOW}{Colors.B}{system}{Colors.RESET} - {entry['name']}")
                                matchFound = True

                    elif category == "OUTPOSTS":

                        if qry.lower() in entry['name'].lower():

                            print(f"{Colors.YELLOW}{Colors.B}{entry['name']}{Colors.RESET} - {entry['system']}, {entry['galaxy']}, {Colors.GREEN}{Colors.B}{entry['type'].upper()}{Colors.RESET}.")
                            matchFound = True

                    else:

                        if qry.lower() in entry['name'].lower():

                            print(f"{Colors.YELLOW}{Colors.B}{entry['name']}{Colors.RESET}")
                            matchFound = True

                # if something was found, set the toggle variable to say that something was found
                if matchFound:

                    foundSomething = True

                else:

                    foundSomething = False

            case "os":

                # setup secondary toggle variable
                matchFound = False
                
                # perform search
                for entry in dataList:

                    if qry.lower() == entry['output']['system'].lower():

                        print(f"{Colors.YELLOW}{Colors.B}{entry['id']}{Colors.RESET} - {entry['system']}, {entry['galaxy']}, {Colors.YELLOW}OG:{Colors.RESET} {entry['output']['galaxy']}")
                        matchFound = True

                # if something was found, set the toggle variable to say that something was found
                if matchFound:

                    foundSomething = True

                else:

                    foundSomething = False

            case "og":

                # setup secondary toggle variable
                matchFound = False
                
                # perform search
                for entry in dataList:

                    if qry.lower() == entry['output']['galaxy'].lower():

                        print(f"{Colors.YELLOW}{Colors.B}{entry['id']}{Colors.RESET} - {entry['system']}, {entry['galaxy']}, {Colors.YELLOW}OS:{Colors.RESET} {entry['output']['system']}")
                        matchFound = True

                # if something was found, set the toggle variable to say that something was found
                if matchFound:

                    foundSomething = True

                else:

                    foundSomething = False
        
        # if something was not found, let the user know
        if not foundSomething:

            print(f"{Colors.BLACK}{Colors.REDB}!! NONE !!{Colors.RESET}")
    
    # used to write data to the "database"
    def wData(dataList, mthd):
        """
        A nested function responsible for actually searching out data and reporting it back to the user

        Parameters:
        - dataList (list): the list of dictionaries to be read from
        - mthd (string): the method in which to search in dataList
        - qry (string): the string value to be searched
        """
        
        # colors! :D
        print(f"\n{Colors.B}{Colors.U}{Colors.CYAN}DATA INPUT REQUIRED:{Colors.RESET}")
        
        # using the mthd variable, use the correct process to write in data
        match mthd:
            
            case "o":

                # local variables
                lastIndexOf = 0
                content = ""
                firstEntry = False

                # read the current data from the file and determine if this is the first entry or not
                # accounts for a totally blank file
                with open("./data/outposts.txt", "r") as rfile:
                    
                    # read data
                    content = rfile.read()
                    
                    # if there is no [ or ] in the data then it must be a blank file or this is the first entry
                    # set toggle bool to True and set last index to be in between the brackets
                    if "[" and "]" not in content:
                        firstEntry = True
                        lastIndexOf = 1

                    # if there is already data in the file, find the last index of the } character
                    # this character signifies the end of a dictionary and will be the next starting place to write at
                    else:
                        for i in range(len(content) - 1, -1, -1):
                            if content[i] == "}":
                                lastIndexOf = i+1
                                break

                    rfile.close()

                # get the user's input for the new dictionary
                userDataInput = ""
                outpostName = input(f"{Colors.B}{Colors.RED}NAME: {Colors.RESET}")
                outpostSystem = input(f"{Colors.B}{Colors.YELLOW}SYSTEM: {Colors.RESET}")
                outpostGalaxy = input(f"{Colors.B}{Colors.GREEN}GALAXY: {Colors.RESET}")
                outpostType = input(f"{Colors.B}{Colors.BLUE}TYPE: {Colors.RESET}")
                
                # if this is the first entry, don't use a comma and a line break at the start
                # if it is not, use them
                if firstEntry:
                    userDataInput = "    {\n        " + f'"name": "{outpostName}",\n        ' + f'"system": "{outpostSystem}",\n        ' + f'"galaxy": "{outpostGalaxy}",\n        ' + f'"type": "{outpostType}"\n    ' + "}"
                elif not firstEntry:
                    userDataInput = ",\n    {\n        " + f'"name": "{outpostName}",\n        ' + f'"system": "{outpostSystem}",\n        ' + f'"galaxy": "{outpostGalaxy}",\n        ' + f'"type": "{outpostType}"\n    ' + "}"
                
                # open the file to write
                with open("./data/outposts.txt", "w") as wfile:
                    
                    # if it's the first entry, put the user's data inside the brackets
                    if firstEntry:
                        wfile.write("[\n" + userDataInput + "\n]")
                    
                    # if it is not, just insert the data
                    elif not firstEntry:
                        wfile.write(content[:lastIndexOf] + userDataInput + content[lastIndexOf:])
                    wfile.close()

                # update the database so it can be ready to read
                update()

            case "g":
                
                # local variables
                lastIndexOf = 0
                content = ""
                firstEntry = False

                # read the current data from the file and determine if this is the first entry or not
                # accounts for a totally blank file
                with open("./data/stargates.txt", "r") as rfile:
                    
                    # read data
                    content = rfile.read()
                    
                    # if there is no [ or ] in the data then it must be a blank file or this is the first entry
                    # set toggle bool to True and set last index to be in between the brackets
                    if "[" and "]" not in content:
                        firstEntry = True
                        lastIndexOf = 1

                    # if there is already data in the file, find the last index of the } character
                    # this character signifies the end of a dictionary and will be the next starting place to write at
                    else:
                        for i in range(len(content) - 1, -1, -1):
                            if content[i] == "}":
                                lastIndexOf = i+1
                                break

                    rfile.close()

                # get the user's input for the new dictionary
                userDataInput = ""
                stargateID = input(f"{Colors.B}{Colors.RED}ID: {Colors.RESET}")
                stargateSystem = input(f"{Colors.B}{Colors.YELLOW}SYSTEM: {Colors.RESET}")
                stargateGalaxy = input(f"{Colors.B}{Colors.GREEN}GALAXY: {Colors.RESET}")
                stargateOutputSystem = input(f"{Colors.B}{Colors.BLUE}OUTPUT SYSTEM: {Colors.RESET}")
                stargateOutputGalaxy = input(f"{Colors.B}{Colors.PURPLE}OUTPUT GALAXY: {Colors.RESET}")
                
                # if this is the first entry, don't use a comma and a line break at the start
                # if it is not, use them
                if firstEntry:
                    userDataInput = "    {\n        " + f'"id": "{stargateID}",\n        ' + f'"system": "{stargateSystem}",\n        ' + f'"galaxy": "{stargateGalaxy}",\n        ' + '"output": {\n            ' + f'"system": "{stargateOutputSystem}",\n            "galaxy": "{stargateOutputGalaxy}"\n        ' + "}\n    }"        
                elif not firstEntry:
                    userDataInput = ",\n    {\n        " + f'"id": "{stargateID}",\n        ' + f'"system": "{stargateSystem}",\n        ' + f'"galaxy": "{stargateGalaxy}",\n        ' + '"output": {\n            ' + f'"system": "{stargateOutputSystem}",\n            "galaxy": "{stargateOutputGalaxy}"\n        ' + "}\n    }"
                
                # open the file to write
                with open("./data/stargates.txt", "w") as wfile:
                    
                    # if it's the first entry, put the user's data inside the brackets
                    if firstEntry:
                        wfile.write("[\n" + userDataInput + "\n]")
                    
                    # if it is not, just insert the data
                    elif not firstEntry:
                        wfile.write(content[:lastIndexOf] + userDataInput + content[lastIndexOf:])
                    wfile.close()

                # update the database so it can be ready to read
                update()

            case "t":
                
                # local variables
                lastIndexOf = 0
                content = ""
                firstEntry = False

                # read the current data from the file and determine if this is the first entry or not
                # accounts for a totally blank file
                with open("./data/trading_posts.txt", "r") as rfile:
                    
                    # read data
                    content = rfile.read()
                    
                    # if there is no [ or ] in the data then it must be a blank file or this is the first entry
                    # set toggle bool to True and set last index to be in between the brackets
                    if "[" and "]" not in content:
                        firstEntry = True
                        lastIndexOf = 1

                    # if there is already data in the file, find the last index of the } character
                    # this character signifies the end of a dictionary and will be the next starting place to write at
                    else:
                        for i in range(len(content) - 1, -1, -1):
                            if content[i] == "}":
                                lastIndexOf = i+1
                                break

                    rfile.close()

                # get the user's input for the new dictionary
                userDataInput = ""
                postID = input(f"{Colors.B}{Colors.RED}ID: {Colors.RESET}")
                postSystem = input(f"{Colors.B}{Colors.YELLOW}SYSTEM: {Colors.RESET}")
                postGalaxy = input(f"{Colors.B}{Colors.GREEN}GALAXY: {Colors.RESET}")
                
                # if this is the first entry, don't use a comma and a line break at the start
                # if it is not, use them
                if firstEntry:
                    userDataInput = "    {\n        " + f'"id": "{postID}",\n        "system": "{postSystem}",\n        "galaxy": "{postGalaxy}"\n    ' + "}"
                elif not firstEntry:
                    userDataInput = ",\n    {\n        " + f'"id": "{postID}",\n        "system": "{postSystem}",\n        "galaxy": "{postGalaxy}"\n    ' + "}"

                # open the file to write
                with open("./data/trading_posts.txt", "w") as wfile:
                    
                    # if it's the first entry, put the user's data inside the brackets
                    if firstEntry:
                        wfile.write("[\n" + userDataInput + "\n]")
                    
                    # if it is not, just insert the data
                    elif not firstEntry:
                        wfile.write(content[:lastIndexOf] + userDataInput + content[lastIndexOf:])
                    wfile.close()

                # update the database so it can be ready to read
                update()

            case "s":
                
                
                # local variables
                lastIndexOf = 0
                content = ""
                firstEntry = False

                # read the current data from the file and determine if this is the first entry or not
                # accounts for a totally blank file
                with open("./data/systems.txt", "r") as rfile:
                    
                    # read data
                    content = rfile.read()
                    
                    # if there is no [ or ] in the data then it must be a blank file or this is the first entry
                    # set toggle bool to True and set last index to be in between the brackets
                    if "[" and "]" not in content:
                        firstEntry = True
                        lastIndexOf = 1

                    # if there is already data in the file, find the last index of the } character
                    # this character signifies the end of a dictionary and will be the next starting place to write at
                    else:
                        for i in range(len(content) - 1, -1, -1):
                            if content[i] == "}":
                                lastIndexOf = i+1
                                break

                    rfile.close()

                # get the user's input for the new dictionary
                userDataInput = ""
                systemName = input(f"{Colors.B}{Colors.RED}NAME: {Colors.RESET}")
                systemGalaxy = input(f"{Colors.B}{Colors.YELLOW}PARENT GALAXY: {Colors.RESET}")

                # search the database for a parent galaxy with the name provided
                try:

                    for galaxy in dataList:
                        
                        # if it does not exist, create a new galaxy and place this system inside it
                        if galaxy["name"].lower() != systemGalaxy.lower():

                            # if this is the first entry, don't use a comma and a line break at the start
                            # if it is not, use them
                            if firstEntry:
                                userDataInput = "    {\n        " + f'"name": "{systemGalaxy}",\n        "systems": [\n            "{systemName}"\n        ]\n    ' + "}"
                            elif not firstEntry:
                                userDataInput = ",\n    {\n        " + f'"name": "{systemGalaxy}",\n        "systems": [\n            "{systemName}"\n        ]\n    ' + "}"

                            # open the file to write
                            with open("./data/systems.txt", "w") as wfile:
                    
                                # if it's the first entry, put the user's data inside the brackets
                                if firstEntry:
                                    wfile.write("[\n" + userDataInput + "\n]")

                                # if it is not, just insert the data
                                elif not firstEntry:
                                    wfile.write(content[:lastIndexOf] + userDataInput + content[lastIndexOf:])
                                wfile.close()
                        
                        # if it does exist, place the system inside the entry
                        # but add it through the database instead of directly to the file
                        # use the text form of the dataList to print over the entire file
                        elif galaxy["name"].lower() == systemGalaxy.lower():
                            
                            # remove the "NONE" filler if it's there by replacing it with the new system name
                            if "NONE" in galaxy["systems"]:
                                
                                galaxy["systems"][0] = systemName
                            
                            # if it's not there, just append the new system
                            elif "NONE" not in galaxy["systems"]:
                                
                                galaxy["systems"].append(systemName)

                            # finally, make sure to rewrite the entire file so that it's included in it
                            # make sure to format the text version of the list so that it is readable upon inspection
                            import json

                            # write formatted text to file
                            with open("./data/systems.txt", "w") as wfile:
                                formattedDataList = json.dumps(dataList, indent=4)
                                wfile.write(formattedDataList)
                                wfile.close

                except Exception as exception:
                    pass
                    # print(f"EXCEPTION THROWN: {exception}")

                # update the database so it can be ready to read
                update()

            case "x":
                
                # local variables
                lastIndexOf = 0
                content = ""
                firstEntry = False

                # read the current data from the file and determine if this is the first entry or not
                # accounts for a totally blank file
                with open("./data/systems.txt", "r") as rfile:
                    
                    # read data
                    content = rfile.read()
                    
                    # if there is no [ or ] in the data then it must be a blank file or this is the first entry
                    # set toggle bool to True and set last index to be in between the brackets
                    if "[" and "]" not in content:
                        firstEntry = True
                        lastIndexOf = 1

                    # if there is already data in the file, find the last index of the } character
                    # this character signifies the end of a dictionary and will be the next starting place to write at
                    else:
                        for i in range(len(content) - 1, -1, -1):
                            if content[i] == "}":
                                lastIndexOf = i+1
                                break

                    rfile.close()

                # get the user's input for the new dictionary
                userDataInput = ""
                galaxyName = input(f"{Colors.B}{Colors.RED}NAME: {Colors.RESET}")
                galaxySystems = []

                while True:

                    # if the user knows or wants to input any systems inside the galaxy, start loop to get data
                    isParent = input(f"{Colors.B}{Colors.CYAN}Would you like to input any systems inside this galaxy? (y / n): {Colors.RESET}")

                    # if yes, start loop
                    if isParent.lower() == "y":

                        while True:
                            
                            # ask for system name and append it to the list
                            galaxySystem = input(f"{Colors.B}{Colors.YELLOW}SYSTEM NAME: {Colors.RESET}")
                            galaxySystems.append(galaxySystem)

                            # ask to add in another
                            anotherChild = input(f"{Colors.B}{Colors.CYAN}Input Another? (y / n): {Colors.RESET}")

                            # if yes, continue
                            if anotherChild.lower() == "y":
                                pass

                            # if no, break
                            elif anotherChild.lower() == "n":
                                break

                            # if wrong input, repeat and tell
                            else:
                                print(f"{Colors.BLACK}{Colors.REDB}\n!- INVALID CHOICE. PLEASE TRY AGAIN. -!{Colors.RESET}\n")

                        break

                    # if no, fill in as blank and continue
                    elif isParent.lower() == "n":
                        galaxySystems.append("NONE")
                        break

                    # if wrong input, repeat and tell
                    else:
                        print(f"{Colors.BLACK}{Colors.REDB}\n!- INVALID CHOICE. PLEASE TRY AGAIN. -!{Colors.RESET}\n")
                
                # add the systems to the userDataInput
                systemDataInput = '"systems": [\n            '
                for i in range(len(galaxySystems)):
                    
                    # if it's not the last item, use the comma
                    if i != (len(galaxySystems) - 1):
                        systemDataInput = systemDataInput + f'"{galaxySystems[i]}",\n            '

                    # if it is, don't use the comma (using it will disrupt the read function of the app)
                    # and make sure to include the last brackets
                    elif i == (len(galaxySystems) - 1):
                        systemDataInput = systemDataInput + f'"{galaxySystems[i]}"\n        ]\n    ' + "}"

                # if this is the first entry, don't use a comma and a line break at the start
                # if it is not, use them
                if firstEntry:
                    userDataInput = "    {\n        " + f'"name": "{galaxyName}",\n        ' + systemDataInput
                elif not firstEntry:
                    userDataInput = ",\n    {\n        " + f'"name": "{galaxyName}",\n        ' + systemDataInput

                # open the file to write
                with open("./data/systems.txt", "w") as wfile:
                    
                    # if it's the first entry, put the user's data inside the brackets
                    if firstEntry:
                        wfile.write("[\n" + userDataInput + "\n]")
                    
                    # if it is not, just insert the data
                    elif not firstEntry:
                        wfile.write(content[:lastIndexOf] + userDataInput + content[lastIndexOf:])
                    wfile.close()

                # update the database so it can be ready to read
                update()
    
    # currently this is only just copy & pasted code from "rData" because the code for searching data will probably be used again
    def cData(dataList, mthd, qry):
        """
        A nested function responsible for actually searching out desired data and erasing/clearing/wiping it

        Parameters:
        - dataList (list): the list of dictionaries to be read from
        - mthd (string): the method in which to search in dataList
        - qry (string): the string value to be searched
        """

        foundSomething = True
        print(Colors.CYAN + Colors.U)
        match mthd:
            case "g":
                matchFound = False
                print(f"FOUND:_______________{Colors.UOFF}")
                for entry in dataList:
                    try:
                        if qry.lower() == entry['galaxy'].lower():
                            try:
                                print(f"{Colors.YELLOW}{Colors.B}{entry['name']}{Colors.RESET} - {entry['system']}, {Colors.GREEN}{Colors.B}{entry['type'].upper()}{Colors.RESET}.")
                                matchFound = True
                            except KeyError:
                                if category == "STARGATES":
                                    print(f"{Colors.YELLOW}{Colors.B}{entry['id']}{Colors.RESET} - {entry['system']}, {Colors.YELLOW}OS:{Colors.RESET} {entry['output']['system']}, {Colors.YELLOW}OG:{Colors.RESET} {entry['output']['galaxy']}.")
                                    matchFound = True
                                else:
                                    print(f"{Colors.YELLOW}{Colors.B}{entry['id']}{Colors.RESET} - {entry['system']}")
                                    matchFound = True
                    except KeyError:
                        if qry.lower() == entry['name'].lower():
                            for system in entry['systems']:
                                print(f"{Colors.YELLOW}{Colors.B}{system}{Colors.RESET}")
                                matchFound = True
                if matchFound:
                    foundSomething = True
                else:
                    foundSomething = False
            case "s":
                matchFound = False
                print(f"FOUND:_______________{Colors.UOFF}")
                for entry in dataList:
                    try:
                        if qry.lower() == entry['system'].lower():
                            try:
                                print(f"{Colors.YELLOW}{Colors.B}{entry['name']}{Colors.RESET} - {entry['galaxy']}, {Colors.GREEN}{Colors.B}{entry['type'].upper()}{Colors.RESET}.")
                                matchFound = True
                            except KeyError:
                                if category == "STARGATES":
                                    print(f"{Colors.YELLOW}{Colors.B}{entry['id']}{Colors.RESET} - {entry['galaxy']}, {Colors.YELLOW}OS:{Colors.RESET} {entry['output']['system']}, {Colors.YELLOW}OG:{Colors.RESET} {entry['output']['galaxy']}.")
                                    matchFound = True
                                else:
                                    print(f"{Colors.YELLOW}{Colors.B}{entry['id']}{Colors.RESET} - {entry['galaxy']}")
                                    matchFound = True
                    except KeyError:
                        for system in entry['systems']:
                            if qry.lower() == system.lower():
                                print(f"{Colors.YELLOW}{Colors.B}{entry['name']}{Colors.RESET}")
                                matchFound = True
                if matchFound:
                    foundSomething = True
                else:
                    foundSomething = False
            case "t":
                matchFound = False
                print(f"FOUND:_______________{Colors.UOFF}")
                for entry in dataList:
                    if qry.lower() == entry['type']:
                        print(f"{Colors.YELLOW}{Colors.B}{entry['name']}{Colors.RESET} - {entry['system']}, {entry['galaxy']}.")
                        matchFound = True
                if matchFound:
                    foundSomething = True
                else:
                    foundSomething = False
            case "lp":
                matchFound = False
                print(f"FOUND:_______________{Colors.UOFF}")
                for entry in dataList:
                    if category == "SYSTEMS":
                        for system in entry['systems']:
                            if qry.lower() in system.lower():
                                print(f"{Colors.YELLOW}{Colors.B}{system}{Colors.RESET} - {entry['name']}")
                                matchFound = True
                    elif category == "OUTPOSTS":
                        if qry.lower() in entry['name'].lower():
                            print(f"{Colors.YELLOW}{Colors.B}{entry['name']}{Colors.RESET} - {entry['system']}, {entry['galaxy']}, {Colors.GREEN}{Colors.B}{entry['type'].upper()}{Colors.RESET}.")
                            matchFound = True
                    else:
                        if qry.lower() in entry['name'].lower():
                            print(f"{Colors.YELLOW}{Colors.B}{entry['name']}{Colors.RESET}")
                            matchFound = True
                if matchFound:
                    foundSomething = True
                else:
                    foundSomething = False
            case "os":
                matchFound = False
                print(f"FOUND:_______________{Colors.UOFF}")
                for entry in dataList:
                    if qry.lower() == entry['output']['system'].lower():
                        print(f"{Colors.YELLOW}{Colors.B}{entry['id']}{Colors.RESET} - {entry['system']}, {entry['galaxy']}, {Colors.YELLOW}OG:{Colors.RESET} {entry['output']['galaxy']}")
                        matchFound = True
                if matchFound:
                    foundSomething = True
                else:
                    foundSomething = False
            case "og":
                print(f"FOUND:_______________{Colors.UOFF}")
                for entry in dataList:
                    if qry.lower() == entry['output']['galaxy'].lower():
                        print(f"{Colors.YELLOW}{Colors.B}{entry['id']}{Colors.RESET} - {entry['system']}, {entry['galaxy']}, {Colors.YELLOW}OS:{Colors.RESET} {entry['output']['system']}")
                        matchFound = True
                if matchFound:
                    foundSomething = True
                else:
                    foundSomething = False
        if not foundSomething:
            print(f"{Colors.BLACK}{Colors.REDB}!! NONE !!{Colors.RESET}")

    # when the function is called, check what the mode is, then run the match-case statement for it's corresponding function
    # WRITING MODE 
    if mode == "w":

        # pass a different corresponding data list variable depending on the category chosen
        # fyi: vars.systems is used for both the "GALAXIES" category case AND the "SYSTEMS" category case
        # because BOTH desired search return data choices are found in the same file and therefore in the same data list
        match category:
            case "OUTPOSTS":
                wData(vars.outposts, method)

            case "STARGATES":
                wData(vars.stargates, method)

            case "TRADING POSTS":
                wData(vars.tradingPosts, method)

            case "GALAXIES":
                wData(vars.systems, method)

            case "SYSTEMS":
                wData(vars.systems, method)


        # after the function decided above is finished executing, ask if the user wishes to query another value
        while True:
            
            qagain = input(f"{Colors.CYAN}{Colors.B}Would you like to input another entry? (y / n){Colors.RESET}: ")
            
            # if yes, run the search again with the same parameters and break the loop
            # if no, just break the loop
            # if the value is invalid, let the user know and go again
            if qagain == "y":
                runSearch(category, method, mode)
                break
            elif qagain == "n":
                break
            else:
                print(f"{Colors.BLACK}{Colors.REDB}\n!- INVALID CHOICE. PLEASE TRY AGAIN. -!{Colors.RESET}\n")

    # READING MODE
    elif mode == "r":

        # ask for query to search for
        query = input(f"\n{Colors.YELLOW}{Colors.B}Input Query{Colors.RESET}: ")

        # pass a different corresponding data list variable depending on the category chosen
        # fyi: vars.systems is used for both the "GALAXIES" category case AND the "SYSTEMS" category case
        # because BOTH desired search return data choices are found in the same file and therefore in the same data list
        match category:
            case "OUTPOSTS":
                rData(vars.outposts, method, query)
            case "STARGATES":
                rData(vars.stargates, method, query)
            case "TRADING POSTS":
                rData(vars.tradingPosts, method, query)
            case "GALAXIES":
                rData(vars.systems, method, query)
            case "SYSTEMS":
                rData(vars.systems, method, query)

        # after the function decided above is finished executing, ask if the user wishes to query another value
        while True:
            
            qagain = input(f"{Colors.CYAN}{Colors.B}Would you like to query again? (y / n){Colors.RESET}: ")
            
            # if yes, run the search again with the same parameters and break the loop
            # if no, just break the loop
            # if the value is invalid, let the user know and go again
            if qagain == "y":
                runSearch(category, method, mode)
                break
            elif qagain == "n":
                break
            else:
                print(f"{Colors.BLACK}{Colors.REDB}\n!- INVALID CHOICE. PLEASE TRY AGAIN. -!{Colors.RESET}\n")

    # CLEARING MODE
    elif mode == "c":

        # function not implemented yet
        print(f"\n{Colors.BLACK}{Colors.REDB}!!* FUNCTION NOT IMPLETMENTED YET. *!!{Colors.RESET}")
    
    # if the mode is an incorrect value, throw an error
    else:
        raise ValueError("Argument value not 'r', 'w', or 'c'.")

# used to decide what the method (seen as "choice" in this function) to use when searching
# this variable is later used in the nested functions of "runSearch"
def rwcData(mode="r"):
    """
    Decides what method to use when searching data
    and calls one of the corresponding nested functions based on the mode.

    Parameters:
    - mode (string): "r" read, "w" write, "c" clear; defaulted to "r" for read
    """

    # ask the user what they would like to search/write/clear
    while True:
        
        # read mode
        if mode == "r":
            
            # ask user what to search for
            choice2 = input(f"{Colors.RED}\n(O)utposts{Colors.WHITE}, {Colors.YELLOW}Star(g)ates{Colors.WHITE}, {Colors.GREEN}(T)rading Posts{Colors.WHITE}, {Colors.BLUE}Gala(x)ies{Colors.WHITE}, or {Colors.PURPLE}(S)ystems{Colors.WHITE}?: ")

            # if the value is "exit", break the loop and go back to the main menu
            if choice2 == "exit":
                break

            # if the value is one of the valid values, proceed and call runSearch
            elif choice2 in ["o", "g", "t", "s", "x"]:
                match choice2:
                    case "o":
                        print(Colors.CYAN)
                        group = "OUTPOSTS"
                        print(f"\nYou have chosen to search for {Colors.RESET}{Colors.B}{group}{Colors.BOFF}{Colors.CYAN}.")
                        while True:
                            choice = input(f"{Colors.CYAN}Search by {Colors.RED}(g)alaxy name{Colors.CYAN}, {Colors.YELLOW}(s)ystem name{Colors.CYAN}, {Colors.GREEN}letter or phrase in name (lp){Colors.CYAN}?: {Colors.RESET}")
                            if choice not in ["g", "s", "t", "lp"]:
                                print(f"{Colors.BLACK}{Colors.REDB}\n!- INVALID CHOICE. PLEASE TRY AGAIN. -!{Colors.RESET}\n")
                            else:
                                runSearch(group, choice, mode)
                                break

                    case "g":
                        print(Colors.CYAN)
                        group = "STARGATES"
                        print(f"\nYou have chosen to search for {Colors.RESET}{Colors.B}{group}{Colors.BOFF}{Colors.CYAN}.")
                        while True:
                            choice = input(f"{Colors.CYAN}Search by {Colors.RED}(g)alaxy name{Colors.CYAN}, {Colors.YELLOW}(s)ystem name{Colors.CYAN},{Colors.PURPLE}\noutput system (os){Colors.CYAN}, or {Colors.MAGENTA}output galaxy (og){Colors.CYAN}?: {Colors.RESET}")
                            if choice not in ["g", "s", "i", "os", "og"]:
                                print(f"{Colors.BLACK}{Colors.REDB}\n!- INVALID CHOICE. PLEASE TRY AGAIN. -!{Colors.RESET}\n")
                            else:
                                runSearch(group, choice, mode)
                                break

                    case "t":
                        print(Colors.CYAN)
                        group = "TRADING POSTS"
                        print(f"\nYou have chosen to search for {Colors.RESET}{Colors.B}{group}{Colors.BOFF}{Colors.CYAN}.")
                        while True:
                            choice = input(f"{Colors.CYAN}Search by {Colors.RED}(g)alaxy name{Colors.CYAN}, {Colors.YELLOW}(s)ystem name{Colors.CYAN}: {Colors.RESET}")
                            if choice not in ["g", "s"]:
                                print(f"{Colors.BLACK}{Colors.REDB}\n!- INVALID CHOICE. PLEASE TRY AGAIN. -!{Colors.RESET}\n")
                            else:
                                runSearch(group, choice, mode)
                                break

                    case "s":
                        print(Colors.CYAN)
                        group = "SYSTEMS"
                        print(f"\nYou have chosen to search for {Colors.RESET}{Colors.B}{group}{Colors.BOFF}{Colors.CYAN}.")
                        while True:
                            choice = input(f"{Colors.CYAN}Search by {Colors.RED}(g)alaxy name{Colors.CYAN}, {Colors.YELLOW}letter or phrase in name (lp){Colors.CYAN}?: {Colors.RESET}")
                            if choice not in ["g", "lp"]:
                                print(f"{Colors.BLACK}{Colors.REDB}\n!- INVALID CHOICE. PLEASE TRY AGAIN. -!{Colors.RESET}\n")
                            else:
                                runSearch(group, choice, mode)
                                break

                    case "x":
                        print(Colors.CYAN)
                        group = "GALAXIES"
                        print(f"\nYou have chosen to search for {Colors.RESET}{Colors.B}{group}{Colors.BOFF}{Colors.CYAN}.")
                        while True:
                            choice = input(f"{Colors.CYAN}Search by {Colors.YELLOW}(s)ystem name{Colors.CYAN}, {Colors.GREEN}letter or phrase in name (lp){Colors.CYAN}?: {Colors.RESET}")
                            if choice not in ["s", "lp"]:
                                print(f"{Colors.BLACK}{Colors.REDB}\n!- INVALID CHOICE. PLEASE TRY AGAIN. -!{Colors.RESET}\n")
                            else:
                                runSearch(group, choice, mode)
                                break
                            
            # if the value is invalid and not one of the options, tell the user that and go again
            else:
                print(f"{Colors.BLACK}{Colors.REDB}\n!- INVALID CHOICE. PLEASE TRY AGAIN. -!{Colors.RESET}\n")

        elif mode == "w":

            # ask user what to write for
            choice2 = input(f"{Colors.RED}\n(O)utposts{Colors.WHITE}, {Colors.YELLOW}Star(g)ates{Colors.WHITE}, {Colors.GREEN}(T)rading Posts{Colors.WHITE}, {Colors.BLUE}Gala(x)ies{Colors.WHITE}, or {Colors.PURPLE}(S)ystems{Colors.WHITE}?: ")

            # if the value is "exit", break the loop and go back to the main menu
            if choice2 == "exit":
                break

            # if the value is one of the valid values, proceed and call runSearch
            elif choice2 in ["o", "g", "t", "s", "x"]:
                match choice2:
                    case "o":
                        group = "OUTPOSTS"
                        runSearch(group, choice2, mode)

                    case "g":
                        group = "STARGATES"
                        runSearch(group, choice2, mode)

                    case "t":
                        group = "TRADING POSTS"
                        runSearch(group, choice2, mode)

                    case "s":
                        group = "SYSTEMS"
                        runSearch(group, choice2, mode)

                    case "x":
                        group = "GALAXIES"
                        runSearch(group, choice2, mode)

            # if the value is invalid and not one of the options, tell the user that and go again
            else:
                print(f"{Colors.BLACK}{Colors.REDB}\n!- INVALID CHOICE. PLEASE TRY AGAIN. -!{Colors.RESET}\n")

        elif mode == "c":
            pass

def update():
    """
    Updates the database list variables in vars.py and makes sure the required files and folder exists.
    """

    # local variables
    path = "data/"
    requiredFiles = ["outposts.txt", "stargates.txt", "systems.txt", "trading_posts.txt"]

    # if the folder "data" doesn't exist, create it and let the user know that was done
    if not os.path.exists(os.path.join(path)):
        os.mkdir("data/")
        print(f"{Colors.YELLOW}* Created missing directory: data{Colors.RESET}")
    
    # if the files necessary for operation do not exist, create blank new ones and let the user know that was done
    missingFiles = set(requiredFiles) - set(os.listdir(path))
    for missingName in missingFiles:
        missingFile = os.path.join(path, missingName)
        with open(missingFile, "w") as newFile:
            newFile.write("")
        print(f"{Colors.YELLOW}* Created missing file: {missingName}{Colors.RESET}")

    # after it is made sure that the folder and the required files are created, go through each, read the data, and assign each to a variable in vars.py
    for file in requiredFiles:
            with open(os.path.join(path, file), 'r') as dataFile:
                try:
                    match file:
                        case "outposts.txt":
                            dic = dataFile.read()
                            vars.outposts = json.loads(dic)
                            data.append(vars.outposts)
                        case "stargates.txt":
                            dic = dataFile.read()
                            vars.stargates = json.loads(dic)
                            data.append(vars.stargates)
                        case "trading_posts.txt":
                            dic = dataFile.read()
                            vars.tradingPosts = json.loads(dic)
                            data.append(vars.tradingPosts)
                        case "systems.txt":
                            dic = dataFile.read()
                            vars.systems = json.loads(dic)
                            data.append(vars.systems)
                except json.decoder.JSONDecodeError as err:
                    pass
