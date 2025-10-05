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
    print("It is now safe to turn off this computer.")
    while True:
        continue

def reset():
    import machine
    machine.reset()

def mkdir(path):
    try:
        import os
        os.mkdir(path)
        return 0
    except:
        return 255

def rmfile(full_path):
    import os
    os.remove(full_path)

def uname():
    import os;return str(os.uname())