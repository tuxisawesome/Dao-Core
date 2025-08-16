import time

net = True
v = "1.0"

def startup():

    bios.branding()
    print("Network is on: " + str(net))
    print("Press Ctrl + C within three seconds to change the boot order.")
    try:
        time.sleep(3)
        print("Booting 'boot.py'")
        try:
            if net:
                import requests
            bios.defload("boot",".").boot([])
        except:
            print("The operating system has reached a critical error and has reset.")
    except:
        selector(net)

def selector(netx):
        net = netx
        stop = False
        while not stop:
            x = input(">>> ").lower()
            if len(x) == 0:
                continue
            elif x == "help":
                bios.branding()
            elif x == "net on":
                net = True
                print("Net is on")
            elif x == "net off":
                net = False
                print("Net is off")
            elif x.startswith("net"):
                print(net)
            else:
                break

        args = x.split(" ")
        boot = args.pop(0)
        
        try:
            if net:
                import requests
            bootloader = bios.defload(boot,".") 
        except:
            print(boot + " is not a valid application.")
            selector(net)
        try:
            bootloader.boot(args)
        except:
            print("The operating system has reached a critical error and has reset.")
            bios.branding()
            selector()


class bios:
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