# Drivers
All programs get `drivers, drivernames, configmgr, drivermgr` passed to their init function. We omit it here.
#### Print - Default text display
Format:
```
def init():
    (initialization code)

def print(text):
    (prints text on screen)

def clear():
    (clears screen)
```

#### Input - Default input read (Keyboard)
Format:
```
def init():
    (initialization code)

def getinput(prompt):
    (Gets input with prompt [prompt]) and returns string
```
#### System Control - System functions (sysctl)
Format:
```
def init():
    (initialization code)

def dir():
    (directory listing. Returns a list of directories)
    (returns list if exists, 1 if does not exist, 255 for other error)

def powerdown():
    (shutdown function. Should not return)

def reset():
    (reset function. should not return)
```