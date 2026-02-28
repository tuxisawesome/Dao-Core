#0.1
v = 0.1
repo_root = "https://raw.githubusercontent.com/tuxisawesome/DaoDownloader/refs/heads/main/"

def init(drivers,drivernames,configmgr,drivermgr,kernel):
    display = drivers[drivernames.index("display")]
    try:
        net = drivers[drivernames.index("net-connect")]
    except:
        display.printline("No internet driver found.");return
    interactive = drivers[drivernames.index("input")]
    sysctl = drivers[drivernames.index("sys")]
    try:
        packagekit = drivers[drivernames.index("packagekit")]
    except:
        display.printline("Package manager backend not found. Please reinstall the driver and reboot.")
    packagekit.configuration.repo_root = repo_root
    argv = configmgr.getvalue(configmgr.readconfig("env.cfg"), "argv")


    display.printline("AppGallery " + str(v))
    

    if argv == "-R" or argv == "-r":
        display.printline("!!! REMOVAL MODE !!!")
        removal_mode = True
    else:
        removal_mode = False
    if argv == "-s" or argv == "-S":
        display.printline("** Syncing (updating) on-device applications")
        packagekit.sync_apps(display,net,sysctl,kernel)
        display.printline("** Please restart or run 'env-reload' to properly push changes.")
        return
    if argv == "-u" or argv == "-U":
        display.printline("Please update AppGallery before using it to install or remove applications.")
        display.printline("Enter the following command to update: 'appgallery -S'")
        return

    display.printline("Please update AppGallery before using it to install or remove applications.")
    display.printline("Enter the following command to update: 'appgallery -S'")












