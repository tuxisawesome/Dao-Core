def init(drivers,drivernames,configmgr,drivermgr,kernel):
    display = drivers[drivernames.index("display")]
    fs = drivers[drivernames.index("vfs")]
    display.printline("BRDT 1.0\nMade with love by Walter Brobson")
    
    device = fs.RAMDisk(512,50)
    x =fs.mkfs.Lfs2(device)
    if x == 1:
        display.printline("!!! Unable to create a filesystem on " + device);return
    x = fs.umount("/")
    if x == 1:
        display.printline("!!! Unable to unmount filesystem at /");return
    x = fs.mount(device,"/")
    if x == 1:
        display.printline("!!! Unable to mount the filesystem at /");return
    display.printline("Successfully mounted at /")
    with open('/hello.txt', 'w') as f:
        f.write('Hello world')
    print(open('/hello.txt').read())