import time
def startup():
    print("Dao Bios")
    print("Press Ctrl + C within three seconds to change the boot order.")
    try:
        time.sleep(3)
        print("Booting 'boot.py'")
        bios.defload("boot",".").boot([])
    except:
        stop = False
        while not stop:
            x = input(">>> ")
            if len(x) == 0:
                continue
            elif x == "help":
                print("DaoBios")
            else:
                break

        args = x.split(" ")
        boot = args.pop(0)
        try:
            bootloader = bios.defload(boot,".")    
        except:
            print("Error booting.")
            startup()
        bootloader.boot(args)


class bios:
    def defload(name, path):
        import sys
        sys.path.append(path)    
        return __import__(name.strip("\n"))
    

if __name__ == "__main__":
    startup()