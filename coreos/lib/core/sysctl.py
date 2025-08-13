def init(drivers, drivernames, configmgr, drivermgr,kernel):
    pass


def dir(path):
    try:
        import os
        contents = os.listdir(path)
        return contents
    except FileNotFoundError:
        return 1
    except Exception as e:
        return 255
    
def powerdown():
    import sys
    sys.exit(0)

def reset():
    import sys
    sys.exit(0)