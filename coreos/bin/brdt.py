def init(drivers,drivernames,configmgr,drivermgr,kernel):
    display = drivers[drivernames.index("display")]
    fs = drivers[drivernames.index("vfs")]
    display.printline("BRDT 1.0\nMade with love by Walter Brobson")
    
    device = fs.RAMDisk(512,50)
    fs.mkfs.Lfs2(device)
    fs.mount(device,"mnt/")
    display.printline("Successfully mounted at /")
    with open('mnt/hello.txt', 'w') as f:
        f.write('Hello world')
    print(open('mnt/hello.txt').read())