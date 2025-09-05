#1.0
def init(drivers,drivernames,configmgr,drivermgr,kernel):
    display = drivers[drivernames.index("display")]
    net = drivers[drivernames.index("net-connect")]
    argv = configmgr.getvalue(configmgr.readconfig("env.cfg"), "argv")
    if argv == "null":
        display.printline("Please provide a website argument.")
    else:
        response_code, response_content = net.get_web_data(argv,kernel)
        if response_code == -255:
            display.printline("Please enable networking and try again.")
            return
        display.printline("Response code: " + str(response_code))
        display.printline("Content below: ")
        display.printline(response_content)
    