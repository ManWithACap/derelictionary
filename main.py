import derelictionary
from colors import Colors

# print out a nice and pretty itty bitty super duper tiny title card that is definitely not absolutely gigantic
print(f"""{Colors.B}{Colors.CYAN}
    ╔════════════════════════════════════════════════════════════════════════════════════╗
    ║{Colors.RED}     ____{Colors.YELLOW}                     {Colors.MAGENTA}__ {Colors.PURPLE}_        {Colors.YELLOW}__   {Colors.GREEN}_                                    {Colors.CYAN}║
    ║{Colors.RED}    / __ \{Colors.YELLOW} ___{Colors.GREEN}   _____{Colors.BLUE} ___{Colors.MAGENTA}   / /{Colors.PURPLE}(_){Colors.RED}_____{Colors.YELLOW} / /_{Colors.GREEN} (_){Colors.BLUE}____{Colors.MAGENTA}   ____{Colors.PURPLE}   ______{Colors.RED} _____{Colors.YELLOW} __  __  {Colors.CYAN}║
    ║{Colors.RED}   / / / /{Colors.YELLOW}/ _ \{Colors.GREEN} / ___/{Colors.BLUE}/ _ \{Colors.MAGENTA} / /{Colors.PURPLE}/ /{Colors.RED}/ ___/{Colors.YELLOW}/ __/{Colors.GREEN}/ /{Colors.BLUE}/ __ \{Colors.MAGENTA} / __ \{Colors.PURPLE} / __  /{Colors.RED}/ ___/{Colors.YELLOW}/ / / /  {Colors.CYAN}║
    ║{Colors.RED}  / /_/ /{Colors.YELLOW}/  __/{Colors.GREEN}/ /{Colors.BLUE}   /  __/{Colors.MAGENTA}/ /{Colors.PURPLE}/ /{Colors.RED}/ /__{Colors.YELLOW} / /_{Colors.GREEN} / /{Colors.BLUE}/ /_/ /{Colors.MAGENTA}/ / / /{Colors.PURPLE}/ /_/ /{Colors.RED}/ /{Colors.YELLOW}   / /_/ /   {Colors.CYAN}║
    ║{Colors.RED} /_____/{Colors.YELLOW} \___/{Colors.GREEN}/_/{Colors.BLUE}    \___/{Colors.MAGENTA}/_/{Colors.PURPLE}/_/{Colors.RED} \___/{Colors.YELLOW} \__/{Colors.GREEN}/_/{Colors.BLUE} \____/{Colors.MAGENTA}/_/ /_/{Colors.PURPLE} \____/{Colors.RED}/_/{Colors.YELLOW}    \__, /    {Colors.CYAN}║
    ║{Colors.WHITE}                                                                         {Colors.YELLOW}/____/     {Colors.CYAN}║
    ║{Colors.WHITE}                                     {Colors.YELLOW}___   ____                                     {Colors.CYAN}║
    ║{Colors.WHITE}                              _   __{Colors.YELLOW}<  /  / __ \\                                    {Colors.CYAN}║
    ║{Colors.WHITE}                             | | / /{Colors.YELLOW}/ /  / / / /                                    {Colors.CYAN}║
    ║{Colors.WHITE}                             | |/ /{Colors.YELLOW}/ /{Colors.WHITE}_ {Colors.YELLOW}/ /_/ /                                     {Colors.CYAN}║
    ║{Colors.WHITE}                             |___/{Colors.YELLOW}/_/{Colors.WHITE}(_){Colors.YELLOW}\____/                                      {Colors.CYAN}║
    ╚════════════════════════════════════════════════════════════════════════════════════╝
    {Colors.BOFF}""")

# start while loop
while True:
    
    # update the data using the files
    derelictionary.update()
    
    # ask to read, search, write, or clear data in the user's derelictionary
    print(f"""{Colors.RED}
    1. Read data{Colors.GREEN}
    2. Write data{Colors.BLUE}
    3. Clear data{Colors.PURPLE}

    Answering with the keyword \"exit\" will back out of 
    an input question most of the time.{Colors.YELLOW}
    Please choose a number.
    """)
    choice1 = input(f"{Colors.RESET}> ")
    
    # match-case statement determines the course of action
    match choice1:
        case "1":
            print(f"{Colors.RED}{Colors.B}READ DATA{Colors.BOFF}")
            derelictionary.rwcData()
        case "2":
            print(f"{Colors.GREEN}{Colors.B}WRITE DATA{Colors.BOFF}")
            derelictionary.rwcData("w")
        case "3":
            print(f"{Colors.BLUE}{Colors.B}CLEAR DATA{Colors.BOFF}")
            derelictionary.rwcData("c")
        case "exit":
            break
        case _:
            print(f"{Colors.BLACK}{Colors.REDB}{Colors.B}\n!- INVALID CHOICE. PLEASE TRY AGAIN. -!{Colors.BOFF}{Colors.RESET}")