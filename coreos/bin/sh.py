def init(drivers, drivernames, configmgr, drivermgr):
    print("hi")
    config = configmgr.readconfig("config.cfg")
    interactive = configmgr.getvalue(config, "interactive")
    display = drivers[drivernames.index("display")]
    if interactive == 0: interactive = False 
    else: interactive = True
    if interactive:
        continues = True
        while continues:
            x = drivers[drivernames.index("input")].getinput("$ ")
            print(x)
            y = drivermgr.defload(x, "bin/")
            print(y)
            try:
                y.init(drivers, drivernames, configmgr, drivermgr)
            except AttributeError:
                display.printline("File not found!")

