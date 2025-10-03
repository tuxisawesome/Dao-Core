# Kernel parameters
### Basic list
#### Built-in parameters
```
configpath=[path]       Configures configuration path for config files.
driverpath=[path]       Configures driver path for driver files    
verbosedrivers=true     Turns on verbose drivers
panic=false             Turns off kernel panics - ADVANCED!
```
#### Application-programmed parameters
```
bin/sh:
    interactive=false       Disables shell

sbin/fsck:
    nofsck=true             Turns off file system continuity checking

lib/core/net/[net,serve]
    net=false               Turns off internet no matter if it is allowed or not in bios
```