class Internet:
    network_active = False
    online = False
    wlan = None


def init(drivers,drivernames,configmgr,drivermgr,kernel):
    if not validcheck(kernel): return
    try:
        display = drivers[drivernames.index("display")]
    except:
        print("!! Please place net-connect after display.")
        return
    display.printline("** Loading net-connect...")
    import network
    import time
    Internet.wlan = network.WLAN(network.STA_IF)
    Internet.wlan.active(True)
    Internet.network_active = True
    display.printline("** Net-connect is loaded.")


def validcheck(kernel):
    kargs = kernel.args
    for arg in kargs:
        if arg == "net=false":
            return False
    try:
        import requests
    except:
        return False
    return True

def get_web_data(website,kernel):
    if not validcheck(kernel):
        return -255, None
    import requests
    try:
        response = requests.get(website)
    except Exception as e:
        print(e)
        return -1,None
    response_code=response.status_code
    response_content=response.content
    return response_code,response_content


def scan_networks(kernel):                            # Returns a list of nearby wifi stations.
    if not validcheck(kernel): return []
    ssidlist = Internet.wlan.scan()
    return ssidlist
    
    

def connect(display,kernel,ssid="",password=""):
    if not validcheck(kernel): return
    Internet.wlan.connect(ssid, password)
    display.printline("Connecting to " + ssid + "...")
    for i in range(20):
        if Internet.wlan.isconnected():
            display.printline("Connected to " + ssid + "!")
            Internet.online = True
            return
        time.sleep(1)
    display.printline("Failed to connect to " + ssid + ". Please check your credentials")

def status(kernel):
    if not validcheck(kernel): return None
    if Internet.wlan.status() == 3:
        Internet.online = True
    else:        Internet.online = False

    return Internet.wlan.status()
    # 0 : Not enabled
    # 1 : Scanning for network
    # 2 : Connecting to network
    # 3 : Connected to network
    # 4 : Connection failed

def network_info(kernel):                         # returns ifconfig but if not connected returns none
    if not validcheck(kernel): return None
    if Internet.wlan.isconnected():
        return Internet.wlan.ifconfig()
    else:
        return None

def disconnect(kernel):
    if not validcheck(kernel): return
    Internet.wlan.disconnect()
    Internet.wlan.active(False)
    Internet.online = False
    Internet.wlan.deinit() # Powers down the driver