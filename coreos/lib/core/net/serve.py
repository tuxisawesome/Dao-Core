def init(drivers,drivernames,configmgr,drivermgr,kernel):
    if not validcheck(kernel): return
    try:
        display = drivers[drivernames.index("net-connect")]
    except:
        print("!! Please place net-serve after net-connect.")
        return
    return

def validcheck(kernel):
    kargs = kernel.args
    for arg in kargs:
        if arg == "net=false":
            return False
    try:
        import socket
        return True
    except:
        return False
    
def socket(kernel):
    if validcheck(kernel):
        import socket as s
        return s
    return None