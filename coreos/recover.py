def boot(args):
    print("Recovery mode")
    while True:
        x = input("? ")
        if x == "shell":
            return
        elif x == "help":
            print("Recovery mode\nCommands:\n[shell]        - Recovery shell\n[about]        - About recovery mode")
        elif x == "about":
            print("Recovery Mode 1.0\nType shell to flash new software or firmware.")

def init(drivers,drivernames,configmgr,drivermgr,kernel):
    display = drivers[drivernames.index("display")]
    display.printline("The recovery shell is not an application.")