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
        print("Commands: '",end="")
        for item in Modules.__dict__.keys():
            if item.startswith("__") or item == "selector": continue
            print("[" + item + "], ",end="")
        print("'")

    def setenv(x):
        commands = x.split(" ")
        if len(commands) == 1: print("setenv bootargs [arguments]");return
        if commands[1] == "bootargs":
            commands.pop(0)
            commands.pop(0)
            bios.configuration.args = commands
        else:
            print("setenv bootargs [arguments]")

    def printargs(x):
        commands = x.split(" ")
        if len(commands) == 1: print("printargs");return
        if commands[1] == "bootargs": print(bios.configuration.args)
        else: print("printenv bootargs");return


    def bootflow(x=""):
        commands = x.split(" ")
        if len(commands) == 1:
            print("bootflow info\nbootflow list\nbootflow boot\nbootflow select [bootflow]");return
        if commands[1] == "select":
            bios.configuration.next_to_boot = commands[2]
        elif commands[1] == "info":
            print(bios.configuration.next_to_boot)
        elif commands[1] == "list":
            bootoptions = get_python_files_os("./")
            for option in bootoptions: print(option.rstrip(".py"))
        elif commands[1] == "boot":
            jump_to_os(bios.configuration.next_to_boot, bios.configuration.args)
            import sys;sys.exit(0)
        else:
            print("bootflow info\nbootflow list\nbootflow boot\nbootflow select [bootflow]")
        
    
    def info(x): import os;print(str(os.uname()))

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
                bios.branding()
            
        
        

def jump_to_os(boot,args):
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





def get_python_files_os(directory_path):
    import os
    python_files = []
    try:
        # List all entries in the directory
        all_entries = os.listdir(directory_path)
        for entry in all_entries:
            full_path = os.path.join(directory_path, entry)
            # Check if it's a file and ends with .py
            if os.path.isfile(full_path) and entry.endswith(".py"):
                python_files.append(entry)
    except:
        print(f"Error: The directory '{directory_path}' does not exist.")
    return python_files





class bios:

    
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
    

    class configuration:
        args = []
        next_to_boot = "boot"
        net = True
        evalglobals = {}


if __name__ == "__main__":
    startup()