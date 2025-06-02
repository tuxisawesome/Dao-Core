def init(drivers, drivernames, configmgr, drivermgr):
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