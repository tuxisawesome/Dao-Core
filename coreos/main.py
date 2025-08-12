import sys
sys.path.insert(1, 'sbin/')
import kernel

nfsk=False

kernel.init(nofsck=nfsk)