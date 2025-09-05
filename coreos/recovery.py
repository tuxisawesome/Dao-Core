def boot(args):
    print("Recovery mode Shell")
    return

def init(drivers,drivernames,configmgr,drivermgr,kernel):
    display = drivers[drivernames.index("display")]
    display.printline("The recovery shell is not an application.")