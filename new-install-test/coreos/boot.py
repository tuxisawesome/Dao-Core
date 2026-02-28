def boot(args):
    
    import sys
    sys.path.insert(1, 'sbin/')
    import kernel
    kernel.main(args)

def init(drivers,drivernames,configmgr,drivermgr,kernel):
    pass