class Internet:
    network_active = True
    online = True
    wlan = None # No need, assumes internet is already connected.
def init(drivers,drivernames,configmgr,drivermgr,kernel):
    if not validcheck(kernel): return
    try:
        display = drivers[drivernames.index("display")]
    except:
        print("!! Please place net-connect after display.")
        return
    display.printline("** Net-connect will assume that the machine is already connected to the internet.")
    display.printline("** Values that are displayed will be dummy values.")
    

def validcheck(kernel):
    kargs = kernel.args
    for arg in kargs:
        if arg == "net=false":
            return False
    try:
        import requests
        return True
    except:
        return False

def scan_networks(kernel):
    return [(b"Internet already connected",0,0,0,0)]

def status(kernel):
    if validcheck(kernel): return 3 
    else: return 0

def network_info(kernel):
    return ['0.0.0.0','255,255,255,0','0.0.0.0','8.8.8.8']

def disconnect(kernel):
    pass

def get_web_data(website,kernel):
    if not validcheck(kernel):
        return -255, None
    import requests
    if website.startswith("http:"):
        verify = False
    else:
        verify = True
    try:
        response = requests.get(website,verify=verify)
    except Exception as e:
        print(e)
        return -1,None
    response_code=response.status_code
    response_content=response.content
    return response_code,response_content
    
def connect(display,kernel,ssid="",password=""):
    if not validcheck: return
    display.printline("**  Net-connect will assume that the internet is already connected to the machine.") 

