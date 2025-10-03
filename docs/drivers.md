# Drivers
All programs get `drivers, drivernames, configmgr, drivermgr` passed to their init function. We omit it here.
#### Print - Default text display
Format:
```
def init():
    (initialization code)

def printline(text):
    (prints text on screen)

def clear():
    (clears screen)

def getdimmentions():
    (Gets dimmentions of screen), returns rows,columns
```

#### Input - Default input read (Keyboard)
Format:
```
def init():
    (initialization code)

def getinput(prompt):
    (Gets input with prompt [prompt]) and returns string
```
#### System Control - System functions (systemcontrol)
Format:
```
def init():
    (initialization code)

def mkdir(path):
    (Creates a directory.)
    (Returns 0 if directory creation is successfull, and 255 if it failed.)

def mkdirs(path):
    (Recursively creates directories)
    (Returns 0 if directory creation is successfull, and 255 if it failed.)

def dir():
    (directory listing. Returns a list of directories)
    (returns list if exists, 1 if does not exist, 255 for other error)

def powerdown():
    (shutdown function. Should not return)

def reset():
    (reset function. should not return)

def rmfile(full_path):
    (Removes a file.)

def uname():
    (Returns system information about the computer.)
```