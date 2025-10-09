def init(drivers,drivernames,configmgr,drivermgr,kernel):
    # Initialize VFS
    pass

def mount(device,mountpoint):
    import vfs
    vfs.mount(device,mountpoint)
    
def get_mounted_devices():
    import vfs
    list = vfs.mount()
    return list

def umount(mountpoint):
    import vfs
    vfs.umount(mountpoint)

class mkfs:
    def fat(device):
        import vfs
        vfs.VfsFat.mkfs(device)
    
    def Lfs1(device):
        import vfs
        vfs.VfsLfs1.mkfs(device)
    
    def Lfs2(device):
        import vfs
        vfs.VfsLfs2.mkfs(device)
    


class RAMDisk:
    def __init__(self, block_size, num_blocks):
        self.block_size = block_size
        self.data = bytearray(block_size * num_blocks)

    def readblocks(self, block_num, buf, offset=0):
        addr = block_num * self.block_size + offset
        for i in range(len(buf)):
            buf[i] = self.data[addr + i]

    def writeblocks(self, block_num, buf, offset=None):
        if offset is None:
            # do erase, then write
            for i in range(len(buf) // self.block_size):
                self.ioctl(6, block_num + i)
            offset = 0
        addr = block_num * self.block_size + offset
        for i in range(len(buf)):
            self.data[addr + i] = buf[i]

    def ioctl(self, op, arg):
        if op == 4: # block count
            return len(self.data) // self.block_size
        if op == 5: # block size
            return self.block_size
        if op == 6: # block erase
            return 0