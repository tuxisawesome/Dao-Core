#2.1
def init(drivers,drivernames,configmgr,drivermgr,kernel): #  FSCK - File System ChecK: A basic system integrity checker
    kargs = kernel.args
    for arg in kargs:
        if arg.startswith("nofsck="):
            if not kernel.sip:
                return
            else:
                continue
    v = 1.0
    display = drivers[drivernames.index("display")]
    helper = drivers[drivernames.index("helper")]
    display.printline("**  fsck " + str(v))
    if kernel.sip:
        display.printline("**  System integrity protection is enabled.")
    else:
        display.printline("**  System integrity protection is disabled.")
    hashdb = configmgr.readconfig("verifiedboot.cfg")
    sid = configmgr.getkeys(hashdb)
    for s in sid:
        x = isthere(s)
        if x == False:
            display.printline("!!! Core system file " + s + " missing! Halting...")
            kernel.panic("Core system file missing")
        else:
            with open(s, 'r') as x:
                p = x.readlines()
                z = ""
                for line in p:
                    z = z + line
                filehash = helper.sha256(z)
                if filehash != configmgr.getvalue(hashdb, s):
                    display.printline("!!! File hash check for " + s + " failed!")
                    kernel.panic("File hash check failed for " + s)
                else:
                    if kernel.verbosedrivers:
                        display.printline("** Check succeeded for " + s)
                x.close()
                

    
    display.printline("**  System integrity check success!")

def isthere(filename):
    try:
        with open(filename, "r") as p:
            p.close()
        return True
    except:
        return False