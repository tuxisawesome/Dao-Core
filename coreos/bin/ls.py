def init(drivers, drivernames, configmgr, drivermgr):
    sys = drivers[drivernames.index("sys")]
    display = drivers[drivernames.index("display")]
    x = drivers[drivernames.index("input")].getinput("Directory to list? ")
    y = sys.dir(x)
    if y == 1:
        display.printline("Directory does not exist")
    elif y == 255:
        display.printline("An unknown error occoured")
    else:
        display.printline("")
        display.printline("Directory listing for: " + x)
        for i in y:
            display.printline(i)
        display.printline("")