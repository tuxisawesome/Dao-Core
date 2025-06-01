
def init(drivers, drivernames, configmgr, drivermgr):
    display = drivers[drivernames.index("display")]
    x = drivers[drivernames.index("input")].getinput("What would you like to print? ")
    display.printline(x)