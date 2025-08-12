import sys

def init(display, init, verbosedrivers,configmgr,drivermgr,drivers,drivernames,nofsck=False):
    # Add key paths to PATH variable
    sys.path.append("usr/bin")
    sys.path.append("usr/local/bin")  
    sys.path.append("bin") 


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
        if progx[0] == "fsck":
            if nofsck:
                continue # Adds option for no file system checking in kernel requirements
        drv = drivermgr.defload(yx[1],yx[0])
        if verbosedrivers:
            display.printline("*   Executing startup task " + progx[0] + " from " + y)
        drv.init(drivers, drivernames, configmgr, drivermgr)

    
    

