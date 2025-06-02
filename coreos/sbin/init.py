import sys
import drivermgr, configmgr

def start():
    mods = configmgr.readconfig("modules.cfg")
    init = configmgr.readconfig("init.cfg")
    config = configmgr.readconfig("config.cfg")
    # Establish constants
    ver = configmgr.getvalue(config, "version")
    verbosedrivers = configmgr.getvalue(config, "verbosedrivers")
    if verbosedrivers == 0: verbosedrivers = False 
    else: verbosedrivers = True


    # First load display module
    x = configmgr.getvalue(mods, "display")
    y = x.split("/")
    display = drivermgr.load(y[1],y[0])

    display.printline("Dao " + ver + " is starting up!")
    # load other modules
    drivers = []
    drivernames = []
    for mod in mods:
        modx = mod.split("=")
        keys = []
        vals = []
        for line in mods:
            x = line.split("=")
            keys.append(x[0])
            vals.append(x[1])
        y = vals[keys.index(modx[0])].strip("\n")
        yx = y.split("/")
        drv = drivermgr.load(yx[1],yx[0])
        drivernames.append(modx[0])
        drivers.append(drv)
        drv.init(drivers, drivernames, configmgr, drivermgr)
        if verbosedrivers:
            display.printline("*   Loaded module " + modx[0] + " from " + y)
    # find drivers like this: drivers[drivernames.index("[name]")]
    display.printline("*   Drivers Loaded Successfully")

    # Add key paths to PATH variable
    sys.path.append("usr/bin")
    sys.path.append("usr/local/bin")  



    # Load init programs
    initprogs = []
    initprognames = []
    for progs in init:
        progx = progs.split("=")
        keys = []
        vals = []
        for line in init:
            x = line.split("=")
            keys.append(x[0])
            vals.append(x[1])
        y = vals[keys.index(progx[0])]
        yx = y.split("/")
        drv = drivermgr.defload(yx[1],yx[0])
        if verbosedrivers:
            display.printline("*   Executing startup task " + progx[0] + " from " + y)
        drv.init(drivers, drivernames, configmgr, drivermgr)
        


    '''
    You can also use the default __import__ function as
    module = __import__(custom)
    '''