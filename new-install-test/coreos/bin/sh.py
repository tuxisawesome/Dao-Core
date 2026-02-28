#0.1

repo_root = "https://raw.githubusercontent.com/tuxisawesome/DaoDownloader/refs/heads/main/"

def init(drivers, drivernames, configmgr, drivermgr,kernel):


    debug = True




    
    config = configmgr.readconfig("config.cfg")
    interactive = configmgr.getvalue(config, "interactive")
    display = drivers[drivernames.index("display")]
    imp = drivers[drivernames.index("input")]
    if interactive == "0": interactive = False 
    else: interactive = True
    kernel_arguments = kernel.args
    if "interactive=false" in kernel_arguments: interactive = False
    if interactive:
        firstrun(drivers, drivernames, configmgr, drivermgr,kernel)
    else:
        display.printline("!   Not an interactive shell, skipping...")


def firstrun(drivers, drivernames, configmgr, drivermgr,kernel):
    display = drivers[drivernames.index("display")]
    imp = drivers[drivernames.index("input")]
    system = drivers[drivernames.index("sys")]
    display.printline("Welcome to the Dao Installation Program!")
    display.printline("We will now update your system to make sure it is running the latest software.")
    display.printline("Would you like to: [i]nstall the latest updates, [a]ccess advanced options, or [e]xit the installer?")
    x = imp.getinput("[i/a/e]: ")
    if x == "i":
        display.printline("Installing updates...")
        system_update(drivers,drivernames,configmgr,drivermgr,kernel)
        display.printline("Updates installed successfully!")
        display.printline("Signing core system files...")
        sign(drivermgr)
        display.printline("Core system files signed successfully!")
        display.printline("Rebooting system to apply updates...")
        return
    elif x == "a":
        display.printline("Accessing advanced options...")
        # Here you would add code to show advanced options, such as partitioning the disk, configuring the network, etc.
        display.printline("Advanced options accessed successfully!")
        firstrun(drivers,drivernames,configmgr,drivermgr,kernel)
    elif x == "e":
        display.printline("Exiting installer. Goodbye!")
        return
    else:
        display.printline("Invalid option selected.")
        firstrun(drivers, drivernames, configmgr, drivermgr,kernel)




def sign(drivermgr):
    y = drivermgr.defload("bootsign", "bin/")

def system_update(drivers,drivernames,configmgr,drivermgr,kernel):
    display = drivers[drivernames.index("display")]
    net = drivers[drivernames.index("net-connect")]
    interactive = drivers[drivernames.index("input")]
    sysctl = drivers[drivernames.index("sys")]
    packagekit = drivers[drivernames.index("packagekit")]
    packagekit.configuration.repo_root = repo_root

    display.printline("System update")
    if True:
        x = packagekit.system_update_backend(repo_root + "system/",net,sysctl,kernel,display)
        if x == -255:
            display.printline("No internet.")
        if x == -1:
            display.printline("Server down.")
        if x == 0:
            display.printline("Please now run 'bootsign' in case any core system files changed.")


