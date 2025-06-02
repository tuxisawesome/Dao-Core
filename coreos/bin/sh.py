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

            if x == "exit": break
            
            if x == "help": 
                display.printline("WalterOS Shell")
                continue
            try:
                y = drivermgr.defload(x, "bin/")
            except ModuleNotFoundError:
                display.printline("File not found!")
                continue
            try:
                y.init(drivers, drivernames, configmgr, drivermgr)
            except AttributeError:
                display.printline("File may be corrupted!\nPlease check the arguments the file is taking.")
                continue
            except TypeError:
                display.printline("Attempted to load a driver file, skipping...")
                continue
            
    else:
        display.printline("!   Not an interactive shell, skipping...")

