sid = ["etc/config.cfg","etc/env.cfg","etc/init.cfg","etc/modules.cfg","etc/recovery.cfg","sbin/configmgr.py","sbin/drivermgr.py","sbin/init.py","sbin/fsck.py"]


def init(drivers,drivernames,configmgr,drivermgr): #  FSCK - File System ChecK: A basic system integrity checker
    v = 1.0 # Todo: check file hashes
    sys = drivers[drivernames.index("sys")]
    display = drivers[drivernames.index("display")]
    display.printline("**  fsck " + str(v))
    for s in sid:
        x = isthere(s)
        if x == False:
            display.printline("!!! Core system file " + s + " missing! Halting...")
            sys.powerdown()
    display.printline("**  System integrity check success!")
    
def isthere(filename):
    try:
        with open(filename, "r") as p:
            p.close()
        return True
    except:
        return False