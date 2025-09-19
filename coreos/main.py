import time # Dao BIOS




v = "1.0"
class Modules:
    def net(x):
        if x.lower() == "net on":
            bios.configuration.net = True
            print("Net is on")
        elif x.lower() == "net off":
            bios.configuration.net = False
            print("Net is off")
        else:
            print(bios.configuration.net)

    def help(x):
        bios.branding()
        print("Commands: 'net [on/off], net, info, eval '[code]' '")
    
    def info(x): import os;print(os.uname())

    def selector(netx):
        bios.configuration.net = netx
        stop = False
        Modules.__dict__.keys()
        while not stop:
            x = input(">>> ").lower()
            if len(x) == 0:
                continue
            if x.split(" ")[0] in Modules.__dict__.keys():
                mod = x.split(" ")[0]
                bios.load_module(mod,x)
            
            elif x.startswith("about"):
                pass
            else:
                break

        args = x.split(" ")
        boot = args.pop(0)
        
        try:
            if bios.configuration.net:
                import requests
                import socket
            bootloader = bios.defload(boot,".") 
        except:
            print(boot + " is not a valid application.")
            Modules.selector(bios.configuration.net)
        try:
            bootloader.boot(args)
        except Exception as e:
            print("The operating system has reached a critical error and has reset.")
            print(e)# TODO: Fix
            bios.branding()
            Modules.selector(bios.configuration.net)


def startup():

    bios.branding()
    print("Network is on: " + str(bios.configuration.net))
    print("Press Ctrl + C within three seconds to change the boot order.")
    try:
        time.sleep(3)
        print("Booting 'boot.py'")
        try:
            if bios.configuration.net:
                import requests
            bios.defload("boot",".").boot([])
        except:
            print("The operating system has reached a critical error and has reset.")
    except:
        Modules.selector(bios.configuration.net)

class bios:
    class configuration:
        net = True
        evalglobals = {}
    
    def load_module(name,x):
        return Modules.__dict__.get(name).__call__(x)

    def defload(name, path):
        import sys
        sys.path = []
        sys.path.append(path)    
        return __import__(name.strip("\n"))
    def branding():
        print("Dao Bios")
        print("Version " + v)
    

if __name__ == "__main__":
    startup()