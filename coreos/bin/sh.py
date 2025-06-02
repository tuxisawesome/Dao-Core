def init(drivers, drivernames, configmgr, drivermgr):
    config = configmgr.readconfig("config.cfg")
    interactive = configmgr.getvalue(config, "interactive")
    display = drivers[drivernames.index("display")]
    if interactive == "0": interactive = False 
    else: interactive = True
    if interactive:
        continues = True
        while continues:
            x = drivers[drivernames.index("input")].getinput("$ ")
            if x == "": continue

            if x == "exit":
                continue

            if x == "poweroff":
                sys = drivers[drivernames.index("sys")]
                display.printline("*   This system is going down for shutdown NOW!")
                sys.powerdown()
            
            if x == "reset":
                sys = drivers[drivernames.index("sys")]
                display.printline("*   This system is restarting NOW!")
                sys.reset()
            
            if x == "help": 
                display.printline("WalterOS Shell")
                continue
            try:
                y = drivermgr.defload(x, "bin/")
            except:
                display.printline("File not found!")
                continue
            try:
                x = y.init(drivers, drivernames, configmgr, drivermgr)
                if x == "quit":
                    break
                else:
                    continue
            except:
                display.printline("File may be corrupted!\nPlease check the arguments the file is taking.")
                continue
            
    else:
        display.printline("!   Not an interactive shell, skipping...")

