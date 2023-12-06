import os, json, vars
from colors import Colors

data = []

def runSearch(category, method, mode="r"):
    def rData(dataList, mthd, qry):
        foundSomething = True
        print(Colors.CYAN + Colors.U)
        match mthd:
            case "g":
                matchFound = False
                print(f"FOUND:‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ {Colors.UOFF}")
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
                print(f"FOUND:‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ {Colors.UOFF}")
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
                print(f"FOUND:‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ {Colors.UOFF}")
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
                print(f"FOUND:‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ {Colors.UOFF}")
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
                print(f"FOUND:‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ {Colors.UOFF}")
                for entry in dataList:
                    if qry.lower() == entry['output']['system'].lower():
                        print(f"{Colors.YELLOW}{Colors.B}{entry['id']}{Colors.RESET} - {entry['system']}, {entry['galaxy']}, {Colors.YELLOW}OG:{Colors.RESET} {entry['output']['galaxy']}")
                        matchFound = True
                if matchFound:
                    foundSomething = True
                else:
                    foundSomething = False
            case "og":
                print(f"FOUND:‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ {Colors.UOFF}")
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
                
    def wData(dataList, mthd, qry):
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

    def cData(dataList, mthd, qry):
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

    if mode == "w":
        print(f"\n{Colors.BLACK}{Colors.REDB}!!* FUNCTION NOT IMPLETMENTED YET. *!!{Colors.RESET}")
    elif mode == "r":
        query = input(f"\n{Colors.YELLOW}{Colors.B}Input Query{Colors.RESET}: ")
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
        while True:
            qagain = input(f"{Colors.CYAN}{Colors.B}Would you like to query again? (y / n){Colors.RESET}: ")
            if qagain == "y":
                runSearch(category, method, mode)
                break
            elif qagain == "n":
                break
            else:
                print(f"{Colors.BLACK}{Colors.REDB}\n!- INVALID CHOICE. PLEASE TRY AGAIN. -!{Colors.RESET}\n")
    elif mode == "c":
        pass
    else:
        raise ValueError("Argument value not 'r', 'w', or 'c'.")

def rwcData(mode="r"):
    while True:
        choice2 = input(f"{Colors.RED}\n(O)utposts{Colors.WHITE}, {Colors.YELLOW}Star(g)ates{Colors.WHITE}, {Colors.GREEN}(T)rading Posts{Colors.WHITE}, {Colors.BLUE}Gala(x)ies{Colors.WHITE}, or {Colors.PURPLE}(S)ystems{Colors.WHITE}?: ")
        if choice2 == "exit":
            break
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
        else:
            print(f"{Colors.BLACK}{Colors.REDB}\n!- INVALID CHOICE. PLEASE TRY AGAIN. -!{Colors.RESET}\n")

def update():
    path = "data/"
    requiredFiles = ["outposts.txt", "stargates.txt", "systems.txt", "trading_posts.txt"]

    if not os.path.exists(os.path.join(path)):
        os.mkdir("data/")
        print(f"{Colors.YELLOW}* Created missing directory: data{Colors.RESET}")
    
    missingFiles = set(requiredFiles) - set(os.listdir(path))
    for missingName in missingFiles:
        missingFile = os.path.join(path, missingName)
        with open(missingFile, "w") as newFile:
            newFile.write("")
        print(f"{Colors.YELLOW}* Created missing file: {missingName}{Colors.RESET}")

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
