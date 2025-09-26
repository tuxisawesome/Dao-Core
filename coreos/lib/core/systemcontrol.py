def init(drivers, drivernames, configmgr, drivermgr,kernel):
    pass

def mkdir(path):
    try:
        import os
        os.mkdir(path)
        return 0
    except:
        return 255
    
def makedirs(path):
    try:
        import os
        os.makedirs(path)
        return 0
    except:
        return 255

def dir(path):
    try:
        import os
        contents = os.listdir(path)
        return contents
    except FileNotFoundError:
        return 1
    except NotADirectoryError:
        return 2
    except Exception as e:
        return 255

    
def powerdown():
    import sys
    sys.exit(0)

def reset():
    import sys
    sys.exit(0)

def rmfile(full_path):
    import os
    os.remove(full_path)

def uname():
    import os;return str(os.uname())