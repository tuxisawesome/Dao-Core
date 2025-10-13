
def init(drivers,drivernames,configmgr,drivermgr,kernel):
    if not validcheck(kernel): return
    try:
        display = drivers[drivernames.index("display")]
    except:
        print("!! Please place net-connect after display.")
        return
    connect(display=display,kernel=kernel)


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
    
def connect(display,kernel,ssid="",password=""):
    if not validcheck: return
    display.printline("**  Net-connect will assume that the internet is already connected to the machine.") 

