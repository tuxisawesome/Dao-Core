# Drivers
### Display drivers
#### Print - Default text display
Format:
```
def init():
    (initialization code)

def print(text):
    (print code)

def clear():
    (clears screen)
```

#### Input - Default input read (Keyboard)
Format:
```
def init():
    (initialization code)

def getinput(prompt):
    (Gets input with prompt [prompt])
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
    (shutdown function)

def reset():
    (reset function)
```