# Drivers
All programs get `drivers, drivernames, configmgr, drivermgr, kernel` passed to their init function. We omit it here.
### Core drivers
#### Print - Default text output (display)
Dependencies: None

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

#### Input - Default input read (input)
Dependencies: None

Format:
```
def init():
    (initialization code)

def getinput(prompt):
    (Gets input with prompt [prompt]) and returns string
```
#### Systemcontrol - System functions (sys)
Dependencies: None

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

### Networking Drivers
#### Net (net-connect)
Dependencies: display

Format:
```
def init():
    (Initialization code.)
    (May include connection to internet here.)

def validcheck(kernel):
    (Checks if device can connect to internet / Has devices to connect to internet / Is allowed to connect to internet)
    (Returns True if able to connect and False if unable.)

def connect(display,kernel,ssid,password):
    (Connects to the internet. Called from "init" function or other application.)
```

#### Serve (net-serve)
Dependencies: net-connect

Format:
```
def init():
    (Initialization code)

def validcheck(kernel):
    (Check to see if system is able to serve a webpage.)
    (Returns true if system is able, and False if system is unable.)

def socket(kernel):
    (Runs validcheck)
    (If system has webpage-serving capabilities, return a instance of "socket")
    (Else, return None)
```

### Shared Libraries
#### Helper (helper)
Dependencies: None

Format:
```
def init():
    (Initialization Code.)

def sha256(data: str) -> str:
    (Computes the SHA-256 hash of the input data)
    (Returns the hash of the data as a lowercase hexadecimal string)
```

#### Packagekit (packagekit)
Dependencies: net-connect

Format:
```
class configuration:
    repo_root = "https://raw.githubusercontent.com/tuxisawesome/DaoDownloader/refs/heads/main/" (Root of repository, can be changed at runtime)

def init():
    (Initialization Code)

def download_file(website,directoryfile,net,kernel,sys,createdirectory=False):
    (Downloads a file to a directory, creating the directory if necesary.)
    (Directoryfile is the file path.)

def install_app(website_root,apps,appnames,app,directory,display,net,kernel,sys,createdirectory=False):
    (A nice wrapper function for download_file that includes error handling.)

def system_update_backend(website_root,net,sysctl,kernel,display):
    (Installs every app in application list (that needs to be updated) for the system)

def remove_trailing_filename(path):
    (Removes the filename from a path.)

def sync_apps(display,net,sysctl,kernel):
    (Updates all apps with newer versions)

def read_repofile(file):
    (Reads a repofile from the internet. (File is a long string))

def install(app, website_root,net,sysctl,kernel,display,removal=False):
    (Nice wrapper for install_app, also removes apps if removal=True)
```